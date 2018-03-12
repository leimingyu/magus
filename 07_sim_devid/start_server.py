#!/usr/bin/env python
'''
1) based on
https://gist.github.com/micktwomey/606178
'''

import os,sys
import socket
import math
import time
import Queue
import ctypes
import operator

import numpy as np
import multiprocessing as mp

from multiprocessing import Pool, Value, Lock, Manager
from subprocess import check_call, STDOUT, CalledProcessError

# log
import logging
logging.basicConfig(level=logging.DEBUG)

# arguments
import argparse
parser = argparse.ArgumentParser(description='')
parser.add_argument('-s', dest='scheme', default='rr', help='rr/ll/sim')
parser.add_argument('-j', dest='jobs', default=0, help='jobs to simulate')
args = parser.parse_args()

# dict used for similarity scheme
app2cmd = None
app2dir = None
app2metric = None

# parameters
JobsPerGPU = 6
LARGE_NUM = 1e9

DEVNULL = open(os.devnull, 'wb', 0)  # no std out
magus_debug = False


def find_row_for_currentJob(GpuMetricStat_array, jobID):
    """
    Stat array is 32 x 2 where 1st col is status and 2nd col is the jobID
    """
    (rows, cols) = GpuMetricStat_array.shape

    target_row = 0
    FOUND_ROW = False
    for i in xrange(rows):
        # find the active job
        if GpuMetricStat_array[i,1] == jobID  and GpuMetricStat_array[i,0] == 1:
            target_row = i
            FOUND_ROW = True
            break

    if not FOUND_ROW:
        print "\n[ERROR] : No record for jobID in GpuMetricStat_dd! Something is wrong."
        sys.exit(1)
            
    return target_row




def check_availrow_metricarray(stat_array):
    """
    stat_array is 32 x 2 where 2 columns are status and jobID
    """
    avail_row = None 
    [rows, cols] = stat_array.shape
    for i in xrange(rows): # look for the 1st avail (0) row, and return the row
        if stat_array[i,0] == 0:
            avail_row = i
            break
    if avail_row is None:
        logger.info("[*** Warning ***] all 32 slots are busy")
        avial_row = 0
    return avail_row


def check_key(app2dir, app2cmd, app2metric):
    sameApps = True

    # read the keys for each dict
    key_dir = set(app2dir.keys())
    key_cmd = set(app2cmd.keys())
    key_metric = set(app2metric.keys())

    #
    # compare dir with cmd
    #
    if key_dir != key_cmd:
        print "[Error] keys in app2dir and app2cmd are different!"
        if len(key_dir) > len(key_cmd):
            print "[Error] Missing keys for key_cmd"

        if len(key_dir) < len(key_cmd):
            print "[Error] Missing keys for key_dir"

        belong2cmd = key_cmd - key_dir
        belong2dir = key_dir - key_cmd

        onlyincmd = list(belong2cmd)
        onlyindir = list(belong2dir)

        if onlyincmd:  # not empty
            print("[Error] Missing keys: {}".format(onlyincmd))

        if onlyindir:  # not empty
            print("[Error] Missing keys: {}".format(onlyindir))

    else:
        # print "Keys in app2dir and app2cmd match!"
        logging.info("Checking ... ")

    #
    # compare dir with metric
    #
    if key_dir != key_metric:
        print "[Error] keys in app2dir and app2metric are different!"
        if len(key_metric) > len(key_dir):
            print "[Error] Missing keys for key_dir"

        if len(key_metric) < len(key_dir):
            print "[Error] Missing keys for key_metric"

        belong2metric = key_metric - key_dir
        belong2dir = key_dir - key_metric

        onlyinmetric = list(belong2metric)
        onlyindir = list(belong2dir)

        if onlyinmetric:  # not empty
            print("[Error] Missing keys: {}".format(onlyinmetric))

        if onlyindir:  # not empty
            print("[Error] Missing keys: {}".format(onlyindir))

    else:
        # print "Keys in app2dir and app2metric match!"
        logging.info("Checking ... ")

    return sameApps


class cd:
    """
    Context manager for changing the current working directory
    """

    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


# def run_remote(app_dir, app_cmd, devid=0):
##    rcuda_select_dev = "RCUDA_DEVICE_" + str(devid) + "=mcx1.coe.neu.edu:" + str(devid)
##    cmd_str = rcuda_select_dev + " " + str(app_cmd)
##
##    startT = time.time()
# with cd(app_dir):
# try:
##            check_call(cmd_str, stdout=DEVNULL, stderr=STDOUT, shell=True)
# except CalledProcessError as e:
##            raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
##    endT = time.time()
##
# return [startT, endT]


def run_remote(app_dir, app_cmd, devid=0):
    #rcuda_select_dev = "RCUDA_DEVICE_" + str(devid) + "=mcx1.coe.neu.edu:" + str(devid)
    cmd_str = app_cmd + " " + str(devid)

    startT = time.time()
    with cd(app_dir):
        # print os.getcwd()
        # print app_dir
        # print cmd_str
        try:
            check_call(cmd_str, stdout=DEVNULL, stderr=STDOUT, shell=True)
        except CalledProcessError as e:
            raise RuntimeError(
                "command '{}' return with error (code {}): {} ({})".format(
                    e.cmd, e.returncode, e.output, app_dir))

    endT = time.time()

    return [startT, endT]


class Server(object):
    def __init__(self, hostname, port):
        self.logger = logging.getLogger("server")
        self.hostname = hostname
        self.port = port
        #self.gpuNum = 1         # Note:  gpus in cluster
        self.gpuNum = 2        # Note:  gpus in cluster
        #self.gpuNum = 12         # Note:  gpus in cluster
        self.lock = Lock()
        self.manager = Manager()

    def find_least_loaded_node(self, GpuJobs_dd):
        with self.lock:
            # sort the dd in ascending order
            sorted_stat = sorted(
                GpuJobs_dd.items(),
                key=operator.itemgetter(1))
            # print sorted_stat
            target_dev = int(sorted_stat[0][0])  # the least loaded gpu
            target_dev_jobs = int(sorted_stat[0][1])
        return target_dev, target_dev_jobs


    #-------------------------------------------------------------------------#
    # 
    #-------------------------------------------------------------------------#
    def scheduler(self, appName, jobID, GpuJobs_dd, GpuMetric_dd, GpuMetricStat_dd, scheme='rr'):
        """
        Decide whitch gpu to allocate the job.
        """
        self.logger.debug("(Monitoring)")
        target_dev = 0

        #--------------------------------
        # check current GPU Node Status
        #--------------------------------
        with self.lock:
            print("\nGpuID\tActiveJobs")
            for key, value in dict(GpuJobs_dd).iteritems():
                print("{}\t{}".format(key, value))

        if scheme == 'rr':  # round-robin
            target_dev = jobID % self.gpuNum

        elif scheme == 'll':  # least load
            target_dev, _ = self.find_least_loaded_node(GpuJobs_dd)

        elif scheme == 'sim':  # similarity-based scheme
            # print app2metric[appName]
            appMetric = app2metric[appName].as_matrix()
            #print appMetric 
            #print appMetric.size

            #-------------------------#
            # check gpu node metrics
            # 1) use 'll' to find the vacant node
            # 2) Given all nodes are busy, select node with the least euclidean
            # distance
            #-------------------------#
            current_dev, current_jobs = self.find_least_loaded_node(GpuJobs_dd)

            if current_jobs == 0:
                target_dev = current_dev
                
                #-------------------------#
                # add job metrics to the GpuMetric
                # update GpuMetricStat
                #-------------------------#
                with self.lock:
                    # if there is no jobs on current device, use the 1st row
                    avail_row = 0

                    #------------------#
                    # add metric to the GpuMetric
                    #------------------#
                    GpuMetric_array = GpuMetric_dd[target_dev]
                    #print type(GpuMetric_array)
                    #print "\norg:"
                    #print GpuMetric_array[avail_row,:]
                    GpuMetric_array[avail_row,:] = appMetric 
                    #print "\nafter:"
                    #print GpuMetric_array[avail_row,:]
                    GpuMetric_dd[target_dev] = GpuMetric_array 

                    #print "\n\nUpdated Metric : "
                    #print GpuMetric_dd[target_dev]

                    #------------------#
                    # update stat in GpuMetricStat (32 x 2, stat + jobID)
                    #------------------#
                    GpuMetricStat_array = GpuMetricStat_dd[target_dev]
                    GpuMetricStat_array[avail_row, : ] = np.array([1, jobID])
                    GpuMetricStat_dd[target_dev] = GpuMetricStat_array 

                    #print "\n\nUpdated Metric Stat : "
                    #print GpuMetricStat_dd[target_dev]
                    
                    #avail_row = check_availrow_metricarray(stat_array)

            elif current_jobs > 0:
                #
                # select the least similar GPU node to run 
                #


                #
                # what is each GPU's (max) metric ?  
                #
                with self.lock:
                    print "\nCheck GpuMetric_dd\n"
                    #for key, value in GpuMetric_dd.iteritems():
                    #    print key

                    min_dist = LARGE_NUM # a quite large number

                    for i in xrange(self.gpuNum): 
                        #
                        # max column metric for each gpu in the numpy array
                        currentGpuMetric = np.amax(GpuMetric_dd[i], axis=0)

                        # 
                        # euclidian dist (currentGpuMetric, appMetric)
                        dist = np.linalg.norm(currentGpuMetric - appMetric)
                        print "euclidian dist: %f  ( GPU %d )" % (dist, i)

                        #
                        # select the least dist 
                        if dist < min_dist:
                            min_dist =  dist
                            target_dev = i

                    #
                    # after selection,  1) add current appMetric to GpuMetric
                    #                   2) update GpuMetricStat

                    # =====================
                    # find the row to write
                    # =====================
                    avail_row = check_availrow_metricarray(GpuMetric_dd[target_dev])


                    #========================
                    # add metric to the GpuMetric
                    #========================
                    GpuMetric_array = GpuMetric_dd[target_dev]
                    GpuMetric_array[avail_row,:] = appMetric 
                    GpuMetric_dd[target_dev] = GpuMetric_array 

                    #========================
                    # update stat in GpuMetricStat (32 x 2, stat + jobID)
                    #========================
                    GpuMetricStat_array = GpuMetricStat_dd[target_dev]
                    GpuMetricStat_array[avail_row, : ] = np.array([1, jobID])
                    GpuMetricStat_dd[target_dev] = GpuMetricStat_array 

                #
                # log
                #
                self.logger.debug("\n[Similarity] select GPU %r\n", target_dev)


                    
            else:
                self.logger.debug(
                    "[Error!] gpu node job is negative! Existing...")
                sys.exit(1)

        else:
            self.logger.debug("Unknown scheduling scheme!")
            sys.exit(1)

        return target_dev


    #-------------------------------------------------------------------------#
    # 
    #-------------------------------------------------------------------------#
    def PrintGpuJobTable(self, GpuJobTable, total_jobs):
        #--------------------------------------------------------------
        # gpu job table : 5 columns
        #    jobid      gpu     status      starT       endT
        #--------------------------------------------------------------
        print("JobID\tGPU\tStatus\tStart\t\t\tEnd\t\t\tDuration")
        for row in xrange(total_jobs):
            print("{}\t{}\t{}\t{}\t\t{}\t\t{}".format(GpuJobTable[row, 0],
                                                      GpuJobTable[row, 1],
                                                      GpuJobTable[row, 2],
                                                      GpuJobTable[row, 3],
                                                      GpuJobTable[row, 4],
                                                      GpuJobTable[row, 4] - GpuJobTable[row, 3]))

    #-------------------------------------------------------------------------#
    # Run incoming workload
    #-------------------------------------------------------------------------#
    def handleWorkload(self, connection, address, jobID,
                       GpuJobTable, GpuJobs_dd, GpuMetric_dd, GpuMetricStat_dd):
        '''
        schedule workloads on the gpu
        '''
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger("process-%r" % (address,))

        try:
            #logger.debug("Connected %r at %r", connection, address)
            logger.debug("Connected")
            while True:
                #--------------------------------------------------------------
                # 1) receive data
                #--------------------------------------------------------------
                data = connection.recv(1024)
                if data == "":
                    logger.debug("Socket closed remotely")
                    break

                if data == "end_simulation":
                    RunServer = False

                logger.debug("Received data %r", data)

                appName = data

                #------------------------------------#
                # 2) get the app_dir, app_cmd
                #------------------------------------#
                app_dir = app2dir[appName]
                app_cmd = app2cmd[appName]

                #data_split = data.split(';')
                # print data_split
                #app_dir, app_cmd = data_split[0], data_split[1]
                # print app_dir, app_cmd

                #--------------------------------------------------------------
                # 3) scheduler : with different schemes
                #--------------------------------------------------------------
                target_gpu = self.scheduler(appName, jobID, 
                        GpuJobs_dd, GpuMetric_dd, GpuMetricStat_dd,
                        scheme=args.scheme)

                self.logger.debug("TargetGPU-%r", target_gpu)

                #-----------------------------------------
                # 4) update gpu job table
                # (columns)   jobid      gpu     status      starT       endT
                #-----------------------------------------
                # Assign job to the target GPU
                GpuJobTable[jobID, 0] = jobID
                GpuJobTable[jobID, 1] = target_gpu
                GpuJobTable[jobID, 2] = 0

                #--------------------------------------------------------------
                # 5) add job to Gpu Node
                #--------------------------------------------------------------
                with self.lock:
                    GpuJobs_dd[target_gpu] = GpuJobs_dd[target_gpu] + 1


                #--------------------------------------------------------------
                # 6) work on the job
                #--------------------------------------------------------------
                [startT, endT] = run_remote(app_dir=app_dir, app_cmd=app_cmd, devid=target_gpu)
                #print("{} to {} = {:.3f} seconds".format(startT, endT, endT - startT))
                self.logger.debug(
                    "(Job {}) {} to {} = {:.3f} seconds".format(
                        jobID, startT, endT, endT - startT))

                #--------------------------------------------------------------
                # The job is done!
                #--------------------------------------------------------------

                #--------------------------------------------------------------
                # 7) delete the job, update GpuMetric 
                #--------------------------------------------------------------
                with self.lock:
                    GpuJobs_dd[target_gpu] = GpuJobs_dd[target_gpu] - 1 

                    #========================
                    # Find the corresponding row for the current jobID 
                    #========================
                    GpuMetricStat_array = GpuMetricStat_dd[target_gpu]
                    #
                    # find the right row to update
                    myrow = find_row_for_currentJob(GpuMetricStat_array, jobID)
                    #
                    # reset the metric stat
                    GpuMetricStat_array[myrow, : ] = np.array([0, -1])
                    GpuMetricStat_dd[target_gpu] = GpuMetricStat_array 
                    #
                    # del metric in the GpuMetric / reset to zeros
                    GpuMetric_array = GpuMetric_dd[target_gpu]
                    GpuMetric_array[myrow,:] = np.zeros((1,26))
                    GpuMetric_dd[target_gpu] = GpuMetric_array 


                #--------------------------------------------------------------
                # 8) update gpu job table
                #
                # 5 columns:
                #    jobid      gpu     status      starT       endT
                #--------------------------------------------------------------
                # mark the job is done, and update the timing info
                GpuJobTable[jobID, 2] = 1  # done
                GpuJobTable[jobID, 3] = startT
                GpuJobTable[jobID, 4] = endT

                #self.logger.debug("%r ", GpuJobTable[:5,:])

                # job_q.put(int(data))

                # for elem in list(job_q.queue):
                #    print elem

                #print("current queue size : {}".format(job_q.qsize()))
                #
                # 1) as we receive data, we put into the queue
                # (don't work on that asap)
                #job_param = None
                # if not job_q.empty():
                #    job_param = job_q.get()
                #    print("work on {}".format(job_param))

                #print("after dequeue size : {}".format(job_q.qsize()))

                # 2) start a new process
                #newjob = mp.Process(target=foo, args=(int(data),))
                # newjob.start()

                # run_job()

                #result = pool.apply_async(foo, (2000 * int(data), ))
                #[startT, endT] = result.get()

                # connection.sendall(data) # send feedback
                #logger.debug("Sent data")
        except BaseException:
            logger.exception("Problem handling request")
        finally:
            logger.debug("Closing socket")
            connection.close()

    #--------------------------------------------------------------------------
    # server start
    #--------------------------------------------------------------------------
    def start(self):
        # read app2metric_dd, app2dir_dd, app2cmd_dd
        global app2dir
        global app2cmd
        global app2metric

        app2dir = np.load('./similarity/app2dir_dd.npy').item()
        app2cmd = np.load('./similarity/app2cmd_dd.npy').item()

        if args.scheme == "rr":
            self.logger.info("Round-Robin Scheduling")

        if args.scheme == "ll":
            self.logger.info("Least loaded Scheduling")

        if args.scheme == "sim":
            self.logger.info("Similarity Scheduling")
            app2metric = np.load('./similarity/app2metric_dd.npy').item()
            if check_key(app2dir, app2cmd, app2metric):
                self.logger.info("Looks good!")

        self.logger.debug("listening")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # resue socket address
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.hostname, self.port))
        self.socket.listen(1)

        #----------------------------------------------------------------------
        # 1) gpu job table : 5 columns
        #----------------------------------------------------------------------
        #----------------------------------------------------------------------
        #
        #    jobid      gpu     status      starT       endT
        #       0       0           1       1           2
        #       1       1           1       1.3         2.4
        #       2       0           0       -           -
        #       ...
        #----------------------------------------------------------------------
        maxJobHist = 10000
        rows, cols = maxJobHist, 5  # note: init with a large prefixed table
        d_arr = mp.Array(ctypes.c_double, rows * cols)
        arr = np.frombuffer(d_arr.get_obj())
        GpuJobTable = arr.reshape((rows, cols))

        #----------------------------------------------------------------------
        # 2) gpu node status: 1 columns
        #----------------------------------------------------------------------
        #----------------------------------------------------------------------
        #    GPU_Node(rows)     ActiveJobs
        #       0               0
        #       1               0
        #       2               0
        #       ...
        #----------------------------------------------------------------------
        GpuJobs_dd = self.manager.dict()
        # print type(GpuJobs_dd)

        for i in xrange(self.gpuNum):
            GpuJobs_dd[i] = 0

        #----------------------------------------------------------------------
        # 3) gpu node metrics
        #
        # for each gpu, allocate 32 (max jobs per gpu) x 26 (metrics for earch
        # jobs)
        #----------------------------------------------------------------------
        GpuMetric_dd = self.manager.dict()

        #GpuMetric_dd[0] = 'hello'

        for i in xrange(self.gpuNum):
            GpuMetric_dd[i] = np.zeros((JobsPerGPU, 26))

        ##print GpuMetric_dd[0]
        ##GpuMetric_dd[0] = np.ones(26) 
        ##print "\n updated"
        ##print GpuMetric_dd[0]

        #----------------------------------------------------------------------
        # 4) gpu node metrics status
        #
        # for each gpu, allocate 32 (max jobs per gpu) x 2 ( status + jobID )
        #----------------------------------------------------------------------
        GpuMetricStat_dd = self.manager.dict()

        for i in xrange(self.gpuNum):
            np_array = np.zeros((JobsPerGPU, 2))
            np_array[:,1] = -1  # the 2nd col for jobID is init with -1
            GpuMetricStat_dd[i] = np_array





        # print len(GpuMetric_dd)
        # print GpuMetric_dd[0].shape

        # for key, value in dict(GpuJobs_dd).iteritems():
        # print key, value

        #self.logger.debug("%r ", type(gpuTable))
        #self.logger.debug("%r ", gpuTable.dtype)
        #self.logger.debug("%r ", gpuTable[:])

        total_jobs = int(args.jobs) # Note: Flag to terminate simulation

        jobID = -1

        #----------------------------------------------------------------------
        # keep listening to the clients
        #----------------------------------------------------------------------
        while True:
            #target_gpu = 0

            conn, address = self.socket.accept()

            jobID = jobID + 1
            #self.logger.debug("Got connection : %r at %r ( job %r )", conn, address, jobID)
            self.logger.debug("Got connection : %r ( job %r )", address, jobID)

            #-----------------------------------------
            # schedule the workload to the target GPU
            #-----------------------------------------
            process = mp.Process(target=self.handleWorkload,
                                 args=(conn, address, jobID, 
                                     GpuJobTable, GpuJobs_dd,
                                     GpuMetric_dd, GpuMetricStat_dd))

            process.daemon = False
            process.start()
            self.logger.debug("Started process %r", process)

            #------------------------------------------------------------------
            # Check the timing trace for all the GPU jobs
            #------------------------------------------------------------------
            if jobID == total_jobs - 1:  # jobID starts from 0
                process.join()  # make sure the last process ends

                # wait for 30s
                self.logger.debug("\n\nWait 30 seconds before ending.\n\n")
                time.sleep(30)

                self.logger.debug("\n\nEnd Simulation\n\n")
                if maxJobHist < total_jobs:
                    self.logger.debug(
                        "\n\nError! The total_jobs exceeds the limit!\n\n")
                self.PrintGpuJobTable(GpuJobTable, total_jobs)

                ##
                # also print the Gpu Node Status
                ##
                # with self.lock:
                #    print("\nGpuID\tActiveJobs")
                #    for gid in xrange(self.gpuNum):
                #        print("{}\t{}".format(gid, GpuNodeStatus[gid, 0]))


if __name__ == "__main__":

    if int(args.jobs) <=0 :
        logging.info("Simulation jobs should be >= 1. (Existing!)")
        sys.exit(1)

    server = Server("0.0.0.0", 9000)
    try:
        logging.info("Listening")
        server.start()
    except BaseException:
        logging.exception("Unexpected exception")
    finally:
        logging.info("Shutting down")
        for process in mp.active_children():
            logging.info("Shutting down process %r", process)
            process.terminate()
            process.join()
    logging.info("All done")
