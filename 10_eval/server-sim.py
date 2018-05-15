#!/usr/bin/env python

import os,sys
import operator, copy, random, time, ctypes
import numpy as np

import multiprocessing as mp
from multiprocessing import Process, Lock, Manager, Value, Pool

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("[server]")


from subprocess import check_call, STDOUT, CalledProcessError
DEVNULL = open(os.devnull, 'wb', 0)  # no std out

sys.path.append('./protobuf')
import GPUApp_pb2

#app2cmd = None
#app2dir = None
app2metric = None
app2trace = None

lock = Lock()
manager = Manager()


#------------------------------------------------------------------------------
# read appinfo from protobuf
#------------------------------------------------------------------------------
def get_appinfo(app_info_file):
    from google.protobuf.internal.decoder import _DecodeVarint32
    # [name, dir, cmd]
    read_app_list = [] 
    with open(app_info_file, 'rb') as f:
        buf = f.read()
        n = 0
        while n < len(buf):
            msg_len, new_pos = _DecodeVarint32(buf, n)
            n = new_pos
            msg_buf = buf[n:n+msg_len]
            n += msg_len
            curApp = GPUApp_pb2.GPUApp()
            curApp.ParseFromString(msg_buf)
            read_app_list.append([curApp.name, curApp.dir, curApp.cmd])
    return read_app_list

#-----------------------------------------------------------------------------#
# go to dir 
#-----------------------------------------------------------------------------#
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


#-----------------------------------------------------------------------------#
# Run incoming workload
#-----------------------------------------------------------------------------#
def run_remote(app_dir, app_cmd, devid=0):
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


def run_test(jobID):
    startT = time.time()
    time.sleep(jobID * 2 + 1)
    endT = time.time()

    return [startT, endT]


#-----------------------------------------------------------------------------#
# 
#-----------------------------------------------------------------------------#
def run_mp(lock, appQueList, total_jobs, jobID, app2dir_dd, GpuJobTable, pid):

    startT = time.time()

    ##for i in xrange(10):
    ##    lock.acquire() 
    ##    corun.value -= 1
    ##    print corun.value

    ##    #if corun.value <= 1:
    ##    #    break_loop = True
    ##    lock.release() 

    ##    if corun.value <= 1:
    ##        print corun.value
    ##        break


        

    while True:
        lock.acquire() 
        #corun.value -= 1
        #print corun.value
        cur_app = appQueList[0]
        del appQueList[0]
        total_jobs.value -= 1
        print pid, cur_app
        lock.release() 


        if total_jobs.value <=1:
            break


    ##STOP = False

    ##while True:
    ##    lock.acquire() 
    ##    corun.value -= 1
    ##    if corun.value == 0:
    ##        STOP = True
    ##    lock.release() 

    ##    if STOP:
    ##        break

    endT = time.time()

    print pid, startT, endT, endT - startT


#-----------------------------------------------------------------------------#
# Run incoming workload
#-----------------------------------------------------------------------------#
def run_work(jobID, GpuJobTable, appName, app2dir_dd):
    GpuJobTable[jobID, 0] = jobID 
    GpuJobTable[jobID, 3] = 0 

    #=========================#
    # run the application 
    #=========================#

    ## [startT, endT] = run_test(jobID)

    app_dir = app2dir_dd[appName]
    app_cmd = "./run.sh"
    target_dev = 0

    [startT, endT] = run_remote(app_dir=app_dir, app_cmd=app_cmd, devid=target_dev)

    logger.debug("jodID:{} \t start: {}\t end: {}\t duration: {}".format(jobID, 
        startT, endT, endT - startT))


    #=========================#
    # update gpu job table
    #
    # 5 columns:
    #    jobid      gpu     starT       endT
    #=========================#
    # mark the job is done, and update the timing info
    GpuJobTable[jobID, 1] = startT 
    GpuJobTable[jobID, 2] = endT 
    GpuJobTable[jobID, 3] = 1   # done



#-----------------------------------------------------------------------------#
# Run incoming workload
#-----------------------------------------------------------------------------#
def handleWorkload(lock, activeJobs, jobID, appName, app2dir_dd, GpuJobTable):
    '''
    schedule workloads on the gpu
    '''
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("(Job-%r)" % (jobID))

    try:
        with lock:
            activeJobs.value += 1
            print jobID, activeJobs.value 

        app_dir = app2dir_dd[appName]
        #print appName
        #print app_dir 

        app_cmd = "./run.sh"
        target_dev = 0

        #=========================#
        # run the application 
        #=========================#
        [startT, endT] = run_remote(app_dir=app_dir, app_cmd=app_cmd, devid=target_dev)
        logger.debug("start: {}\t end: {}\t duration: {}".format(startT, endT, endT - startT))

        #=========================#
        # update gpu job table
        #
        # 5 columns:
        #    jobid      gpu     starT       endT
        #=========================#
        # mark the job is done, and update the timing info
        GpuJobTable[jobID, 0] = jobID 
        GpuJobTable[jobID, 1] = startT 
        GpuJobTable[jobID, 2] = endT 

        with lock:
            activeJobs.value -= 1


    except BaseException:
        logger.exception("Problem handling request")
    finally:
        logger.debug("Done.")


#-----------------------------------------------------------------------------#
# GPU Job Table 
#-----------------------------------------------------------------------------#
def PrintGpuJobTable(GpuJobTable, total_jobs):
    print("JobID\tStart\tEnd\tDuration")
    for row in xrange(total_jobs):
        print("{}\t{}\t{}\t{}".format(GpuJobTable[row, 0],
            GpuJobTable[row, 1],
            GpuJobTable[row, 2],
            GpuJobTable[row, 2] - GpuJobTable[row, 1]))

    total_runtime =  GpuJobTable[total_jobs - 1, 2] - GpuJobTable[0,1]
    print("total runtime = {} (s)".format(total_runtime))

#=============================================================================#
# main program
#=============================================================================#
def main():
    #global app2dir
    #global app2cmd
    global app2metric
    global app2trace


    #-------------------------------------------------------------------------#
    # GPU Job Table 
    #-------------------------------------------------------------------------#
    #    jobid           starT       endT   status
    #       0             1           2
    #       1             1.3         2.4
    #       2             -           -
    #       ...
    #----------------------------------------------------------------------
    maxJobs = 10000
    rows, cols = maxJobs, 4  # note: init with a large prefixed table
    d_arr = mp.Array(ctypes.c_double, rows * cols)
    arr = np.frombuffer(d_arr.get_obj())
    GpuJobTable = arr.reshape((rows, cols))


    #===================#
    # 1) read app info
    #===================#
    #app2dir    = np.load('../07_sim_devid/similarity/app2dir_dd.npy').item()
    #app2cmd    = np.load('../07_sim_devid/similarity/app2cmd_dd.npy').item()

    app2metric_dd = np.load('../07_sim_devid/similarity/app2metric_dd.npy').item()
    #app2trace  = np.load('../07_sim_devid/perfmodel/app2trace_dd.npy').item()

    #print len(app2dir), len(app2cmd), len(app2metric), len(app2trace)

    #app_iobound_dd = np.load('./case_studies/app_iobound_dd.npy').item()

    #=========================================================================#
    # set up the launch order list
    #=========================================================================#
    appsList = get_appinfo('./prepare/app_info_79.bin')
    #print appsList

    app2dir_dd = {}
    for v in appsList:
        app2dir_dd[v[0]] = v[1] 

    #==========#
    # test 1 : for shoc reduction
    #==========#

    launch_list = ['shoc_lev1reduction', 
            'poly_correlation', 
            'cudasdk_interval', 
            'cudasdk_MCEstimatePiInlineQ', 
            'cudasdk_convolutionTexture', 
            'poly_2dconv',
            'cudasdk_MCSingleAsianOptionP',
            'poly_syrk',
            'cudasdk_segmentationTreeThrust',
            'poly_gemm',
            'poly_3mm'] 




    apps_num = len(launch_list)
    logger.debug("Total GPU Applications = {}.".format(apps_num))


    appQueList = copy.deepcopy(launch_list)  # application running queue

    workers = [] # for mp processes


    #==================================#
    # run the apps in the queue 
    #==================================#
    MAXCORUN = 2
    activeJobs = 0
    jobID = -1

    current_jobid_list = []
    active_jobname = []


    #--------------#
    # start from the first job in the queue
    #--------------#
    activeJobs += 1
    jobID += 1
    current_jobid_list.append(jobID)
    appName = appQueList[0]  # get the app
    active_jobname.append(appName)

    process = Process(target=run_work, args=(jobID, GpuJobTable, appName, app2dir_dd))
    process.daemon = False
    workers.append(process)
    process.start()


    for i in xrange(1, apps_num):
        Dispatch = False 

        if activeJobs < MAXCORUN:
            Dispatch = True

        #print("iter {} dispatch={}".format(i, Dispatch))

        if Dispatch:
            #-------------------#
            # select the least similar app to run
            #-------------------#
            target_app = active_jobname[0]
            app2


            activeJobs += 1
            jobID += 1
            current_jobid_list.append(jobID)

            appName = appQueList[i] 

            process = Process(target=run_work, args=(jobID, GpuJobTable, appName, app2dir_dd))

            process.daemon = False
            #logger.debug("Start %r", process)
            workers.append(process)
            process.start()

        else:
            # spin
            while True:
                break_loop = False

                current_running_jobs = 0
                jobs2del = []

                for jid in current_jobid_list:
                    if GpuJobTable[jid, 3] == 1: # check the status, if one is done
                        jobs2del.append(jid)
                        break_loop = True

                if break_loop:
                    activeJobs -= 1

                    # update
                    if jobs2del:
                        for id2del in jobs2del:
                            del_idx = current_jobid_list.index(id2del)
                            del current_jobid_list[del_idx]
                    break

            #------------------------------------
            # after spinning, schedule the work
            #------------------------------------

            #print("iter {}: activeJobs = {}".format(i, activeJobs))
            activeJobs += 1
            jobID += 1
            current_jobid_list.append(jobID)
            #print("iter {}: activeJobs = {}".format(i, activeJobs))

            appName = appQueList[i] 
            process = Process(target=run_work, args=(jobID, GpuJobTable, appName, app2dir_dd))

            process.daemon = False
            #logger.debug("Start %r", process)
            workers.append(process)
            process.start()


    #=========================================================================#
    # end of running all the jobs
    #=========================================================================#


    for p in workers:
        p.join()


    total_jobs = jobID + 1
    PrintGpuJobTable(GpuJobTable, total_jobs)

    if total_jobs <> apps_num:
        logger.debug("[Warning] job number doesn't match.")


if __name__ == "__main__":
    main()
