#!/usr/bin/env python
'''
1) based on
https://gist.github.com/micktwomey/606178
'''

import os,socket,math,time
import Queue,ctypes
import logging

import numpy as np
import multiprocessing as mp


from multiprocessing import Pool,Value,Lock
from subprocess import check_call,STDOUT,CalledProcessError

DEVNULL = open(os.devnull, 'wb', 0) # no std out
magus_debug = False 


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


'''
def run_remote(app_dir, app_cmd, devid=0):
    rcuda_select_dev = "RCUDA_DEVICE_" + str(devid) + "=mcx1.coe.neu.edu:" + str(devid)
    cmd_str = rcuda_select_dev + " " + str(app_cmd)

    #
    #
    #
    startT = time.time()
    with cd(app_dir):
        #print os.getcwd()
        #print app_dir
        try:
            check_call(cmd_str, stdout=DEVNULL, stderr=STDOUT, shell=True)
        except CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    endT = time.time()
    
    return [startT, endT]
    '''

def run_remote(app_dir, app_cmd, devid=0):
    #rcuda_select_dev = "RCUDA_DEVICE_" + str(devid) + "=mcx1.coe.neu.edu:" + str(devid)
    cmd_str = app_cmd + " " + str(devid)

    startT = time.time()
    with cd(app_dir):
        #print os.getcwd()
        #print app_dir
        #print cmd_str
        try:
            check_call(cmd_str, stdout=DEVNULL, stderr=STDOUT, shell=True)
        except CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {} ({})".format(e.cmd, e.returncode, e.output, app_dir))

    endT = time.time()
    
    return [startT, endT]

class Server(object):
    def __init__(self, hostname, port):
        import logging
        self.logger = logging.getLogger("server")
        self.hostname = hostname
        self.port = port
        self.gpuNum = 12         # Note:  gpus in cluster
        self.lock = Lock()

    def scheduler(self, jobID, GpuNodeStatus, scheme = 'rr'):
        self.logger.debug("(Monitoring)")
        target_dev = 0

        #--------------------------------
        # check current GPU Node Status
        #--------------------------------
        with self.lock:
            print("\nGpuID\tActiveJobs")
            for gid in xrange(self.gpuNum):
                print("{}\t{}".format(gid, GpuNodeStatus[gid, 0]))
            print('\n')

        # round-robin
        if scheme == 'rr':
            target_dev = jobID % self.gpuNum

        return target_dev

    
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


    #--------------------------------------------------------------------------
    # run gpu job 
    #--------------------------------------------------------------------------
    def handleWorkload(self, connection, address, jobID, GpuJobTable, GpuNodeStatus):
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

                data_split = data.split(';')
                #print data_split

                app_dir, app_cmd = data_split[0], data_split[1]
                #print app_dir, app_cmd

                #--------------------------------------------------------------
                # 2) Scheduler 
                #--------------------------------------------------------------
                target_gpu = self.scheduler(jobID, GpuNodeStatus, scheme='rr')
                self.logger.debug("Target GPU-%r ", target_gpu)


                #-----------------------------------------
                # 2) update gpu job table 
                #
                # 5 columns:
                #    jobid      gpu     status      starT       endT 
                #-----------------------------------------
                # Assign job to the target GPU
                GpuJobTable[jobID, 0] = jobID
                GpuJobTable[jobID, 1] = target_gpu 
                GpuJobTable[jobID, 2] = 0 

                #--------------------------------------------------------------
                # 3) add job to Gpu Node
                #--------------------------------------------------------------
                with self.lock:
                    GpuNodeStatus[target_gpu, 0] = GpuNodeStatus[target_gpu, 0] + 1



                #------------------------------------------------------------------
                # 3) work on the job 
                #------------------------------------------------------------------
                [startT, endT]= run_remote(app_dir = app_dir, app_cmd = app_cmd, devid = target_gpu) 
                #print("{} to {} = {:.3f} seconds".format(startT, endT, endT - startT))






                #print("{} to {} = {:.3f} seconds".format(startT, endT, endT - startT))
                self.logger.debug("(Job {}) {} to {} = {:.3f} seconds".format(jobID, startT, endT, endT - startT))



                #--------------------------------------------------------------
                # The job is done! 
                #--------------------------------------------------------------

                #--------------------------------------------------------------
                # 4) delete the job to Gpu Node Status 
                #--------------------------------------------------------------
                with self.lock:
                    GpuNodeStatus[target_gpu, 0] = GpuNodeStatus[target_gpu, 0] - 1

                #------------------------------------------------------------------
                # update job timing table 
                #------------------------------------------------------------------
                ##jobTimingTable[jobID, 0] = 1  # done
                ##jobTimingTable[jobID, 1] = startT
                ##jobTimingTable[jobID, 2] = endT
                ##self.logger.debug("%r ", jobTimingTable[:])


                #--------------------------------------------------------------
                # update gpu job table 
                #
                # 5 columns:
                #    jobid      gpu     status      starT       endT 
                #--------------------------------------------------------------
                # mark the job is done, and update the timing info
                GpuJobTable[jobID, 2] = 1  # done
                GpuJobTable[jobID, 3] = startT 
                GpuJobTable[jobID, 4] = endT 

                #self.logger.debug("%r ", GpuJobTable[:5,:])



                #job_q.put(int(data))

                #for elem in list(job_q.queue):
                #    print elem

                #print("current queue size : {}".format(job_q.qsize()))
                #
                ## 1) as we receive data, we put into the queue 
                ## (don't work on that asap)
                #job_param = None
                #if not job_q.empty():
                #    job_param = job_q.get()
                #    print("work on {}".format(job_param))

                #print("after dequeue size : {}".format(job_q.qsize()))

                # 2) start a new process
                #newjob = mp.Process(target=foo, args=(int(data),))
                #newjob.start()

                #run_job()

                #result = pool.apply_async(foo, (2000 * int(data), ))
                #[startT, endT] = result.get()


                #connection.sendall(data) # send feedback
                #logger.debug("Sent data")
        except:
            logger.exception("Problem handling request")
        finally:
            logger.debug("Closing socket")
            connection.close()


    #--------------------------------------------------------------------------
    # server start
    #--------------------------------------------------------------------------
    def start(self):
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
        rows, cols = maxJobHist,5 # note: init with a large prefixed table
        d_arr = mp.Array(ctypes.c_double, rows*cols)
        arr = np.frombuffer(d_arr.get_obj())
        GpuJobTable = arr.reshape((rows,cols))

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
        rows, cols = self.gpuNum, 1
        d_arr = mp.Array(ctypes.c_double, rows*cols)
        arr = np.frombuffer(d_arr.get_obj())
        GpuNodeStatus = arr.reshape((rows,cols))


        #self.logger.debug("%r ", type(gpuTable))
        #self.logger.debug("%r ", gpuTable.dtype)
        #self.logger.debug("%r ", gpuTable[:])

        

        

        total_jobs = 5 # Note: Flag to terminate simulation
        jobID= -1

        #----------------------------------------------------------------------
        # keep listening to the clients
        #----------------------------------------------------------------------
        while True:
            target_gpu = 0
            conn, address = self.socket.accept()
            jobID = jobID + 1
            #self.logger.debug("Got connection : %r at %r ( job %r )", conn, address, jobID)
            self.logger.debug("Got connection : %r ( job %r )", address, jobID)





            #-----------------------------------------
            # schedule the workload to the target GPU 
            #-----------------------------------------
            process = mp.Process(target=self.handleWorkload, 
                    args=(conn, address, jobID, GpuJobTable, GpuNodeStatus))

            process.daemon = False 
            process.start()
            self.logger.debug("Started process %r", process)




            #------------------------------------------------------------------
            # Check the timing trace for all the GPU jobs 
            #------------------------------------------------------------------
            if jobID == total_jobs - 1: # jobID starts from 0
                process.join() # make sure the last process ends
                self.logger.debug("\n\nEnd Simulation\n\n")
                if maxJobHist < total_jobs:
                    self.logger.debug("\n\nError! The total_jobs exceeds the limit!\n\n")
                self.PrintGpuJobTable(GpuJobTable, total_jobs)

                #
                # also print the Gpu Node Status
                #
                with self.lock:
                    print("\nGpuID\tActiveJobs")
                    for gid in xrange(self.gpuNum):
                        print("{}\t{}".format(gid, GpuNodeStatus[gid, 0]))


            


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    server = Server("0.0.0.0", 9000)

    try:
        logging.info("Listening")
        server.start()
    except:
        logging.exception("Unexpected exception")
    finally:
        logging.info("Shutting down")
        for process in mp.active_children():
            logging.info("Shutting down process %r", process)
            process.terminate()
            process.join()
    logging.info("All done")
