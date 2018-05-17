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


    app_dir = app2dir_dd[appName]
    app_cmd = "./run.sh"
    target_dev = 0

    #[startT, endT] = run_test(jobID)
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


#-----------------------------------------------------------------------------#
# GPU Job Table 
#-----------------------------------------------------------------------------#
def FindNextJob(active_job_list, app2app_dist, waiting_list, app2newfeat_dd):
    job_name = active_job_list[0]
    #print job_name, "\n"

    #--------------------------# 
    # run similarity analysis
    #--------------------------# 
    dist_dd = app2app_dist[job_name] # get the distance dict
    dist_sorted = sorted(dist_dd.items(), key=operator.itemgetter(1))

    #print dist_sorted, "\n"
    #print waiting_list

    leastsim_app = None
    # the sorted in non-decreasing order, use reversed()
    for appname_and_dist in reversed(dist_sorted):
        sel_appname = appname_and_dist[0]
        if sel_appname in waiting_list: # find 1st app in the list, and exit
            leastsim_app = sel_appname
            break

    ##print("\n{} <<select>> {}\n".format(job_name, leastsim_app))

    return leastsim_app


def InitTwoJobs(waiting_list, appDur_sorted_dd, cpuTime_sorted_dd):
    # sorted in increasing order
    app1_name = None

    # find the largest cpuTime 
    large_cpuTime_app = [None, None]
    for app in reversed(cpuTime_sorted_dd):
        (appName, appCpuTime) = app
        if appName in waiting_list:
            large_cpuTime_app[0] = appName 
            large_cpuTime_app[1] = appCpuTime 
            break

    app1_name = large_cpuTime_app[0]

    # check whether appDur is smaller than the cpuTime 
    HAS_SMALL = False
    for app in appDur_sorted_dd:
        (appName, appDur) = app
        if appName in waiting_list:
            if appDur < large_cpuTime_app[1]:
                app2_name = appName
                HAS_SMALL = True
                break

    if HAS_SMALL:
        return [app1_name, app2_name]


    # if there is no smaller choice, select the shorted appDur to corun
    app2_name = appDur_sorted_dd[0][0]

    return [app1_name, app2_name]
        

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
    #    jobid           starT       endT
    #       0             1           2
    #       1             1.3         2.4
    #       2             -           -
    #       ...
    #----------------------------------------------------------------------
    maxJobs = 10000
    #rows, cols = maxJobs, 3  # note: init with a large prefixed table
    rows, cols = maxJobs, 4  # note: init with a large prefixed table
    d_arr = mp.Array(ctypes.c_double, rows * cols)
    arr = np.frombuffer(d_arr.get_obj())
    GpuJobTable = arr.reshape((rows, cols))


    #===================#
    # 1) read app info
    #===================#
    #app2dir    = np.load('../07_sim_devid/similarity/app2dir_dd.npy').item()
    #app2cmd    = np.load('../07_sim_devid/similarity/app2cmd_dd.npy').item()
    app2metric = np.load('../07_sim_devid/similarity/app2metric_dd.npy').item()
    #app2trace  = np.load('../07_sim_devid/perfmodel/app2trace_dd.npy').item()

    # [appDur, cpuTime, gpuTime, threads_max, threads_avg, reg_max, reg_avg, sm_max, sm_avg, trans_max, trans_avg]
    app2newfeat_dd = np.load('./case_studies/app2newfeat_dd.npy').item()

    #print len(app2dir), len(app2cmd), len(app2metric), len(app2trace)

    appsList = get_appinfo('./prepare/app_info_79.bin')
    #print appsList[0]
    app2dir_dd = {}
    for v in appsList:
        app2dir_dd[v[0]] = v[1] 



    #=====================================#
    # compute the euclidean distance between app metrics
    #=====================================#
    logger.debug("Compute euclidean dist between apps.")

    app2app_dist = {}
    for app1, metric1 in app2metric.iteritems():
        curApp_dist = {}
        m1 = metric1.as_matrix()
        for app2, metric2 in app2metric.iteritems():
            if app1 <> app2:
                m2 = metric2.as_matrix()
                curApp_dist[app2] = np.linalg.norm(m1 - m2) 

        app2app_dist[app1] = curApp_dist

    logger.debug("Finish computing distance.")


    #=========================================================================#
    # 
    #=========================================================================#
    
    ##launch_list = ['shoc_lev1reduction', 
    ##        'poly_correlation', 
    ##        'cudasdk_interval', 
    ##        'cudasdk_MCEstimatePiInlineQ', 
    ##        'cudasdk_convolutionTexture', 
    ##        'poly_2dconv',
    ##        'cudasdk_MCSingleAsianOptionP',
    ##        'poly_syrk',
    ##        'cudasdk_segmentationTreeThrust',
    ##        'poly_gemm',
    ##        'poly_3mm'] 

    launch_list = ['shoc_lev1reduction', 
            'poly_correlation', 
            'cudasdk_interval', 
            'cudasdk_MCEstimatePiInlineQ' 
            ] 


    apps_num = len(launch_list)
    logger.debug("Total GPU Applications = {}.".format(apps_num))

    #====================#
    # sort
    #====================#
    
    # [appDur, cpuTime, gpuTime, threads_max, threads_avg, reg_max, reg_avg, sm_max, sm_avg, trans_max, trans_avg]
    appDur_dd = {}
    cpuTime_dd = {}
    for i in launch_list:
        appDur, cpuTime = app2newfeat_dd[i][:2]
        appDur_dd[i] = appDur
        cpuTime_dd[i] = cpuTime 

    appDur_sorted = sorted(appDur_dd.items(), key=operator.itemgetter(1))
    cpuTime_sorted = sorted(cpuTime_dd.items(), key=operator.itemgetter(1))

    #print "appDur:\n", appDur_sorted
    #print "cpuTime:\n", cpuTime_sorted

    

    #==================================#
    # 
    #==================================#
    appQueList = copy.deepcopy(launch_list)
    waiting_list = copy.deepcopy(appQueList)

    name2indx_dd = {}
    indx2name_dd = {}
    for i in xrange(apps_num):
        name2indx_dd[appQueList[i]] = i   # find the original index using the app name
        indx2name_dd[i] = appQueList[i]   # find the original index using the app name


    ##print appQueList[:3], "\n"



    #==================================#
    # 4) create independent processes 
    #==================================#
    workers = []


    #==================================#
    # 5) run the apps in the queue 
    #==================================#
    MAXCORUN = 2
    activeJobs = 0
    jobID = -1

    active_job_list = [] # keep track of job name
    name2jobid = {}   # use the application to find the jobID
    jobid2name = {}

    #========================#
    # start with the 1st job
    #========================#
    firsttwojobs = InitTwoJobs(waiting_list, appDur_sorted, cpuTime_sorted)
    #print firsttwojobs 
    #appName = waiting_list[0]

    #
    # app1 + app2
    #
    for i, appName in enumerate(firsttwojobs):
        jobID += 1 
        activeJobs += 1

        active_job_list.append(appName) # add app to the active job list 
        app_idx = waiting_list.index(appName) # remove the app from the waiting list
        del waiting_list[app_idx]

        name2jobid[appName] = jobID
        jobid2name[jobID] = appName 

        process = Process(target=run_work, args=(jobID, GpuJobTable, appName, app2dir_dd))
        process.daemon = False
        workers.append(process)
        process.start()


    #time.sleep(100)


    apps_num_minus_one = apps_num - 1
    for i in xrange(2, apps_num):
        Dispatch = False
        
        if activeJobs < MAXCORUN:
            Dispatch = True

        if Dispatch:
            # there are two cases:
            # 1) there is no active job running, directly schedule the job
            # 2) there is 1 active job (max 2), use similarity 
            if len(active_job_list) == 1:
                #pos = active_job_list[0]
                #job_name = indx2name_dd[pos] 

                leastsim_app = find_least_sim(active_job_list, app2app_dist, waiting_list)

                if leastsim_app is None:
                    logger.debug("[Warning] leastsim_app is None!")
                else:
                    #
                    # run the selected app
                    #
                    activeJobs += 1
                    jobID += 1
                    active_job_list.append(leastsim_app) # add app to the active job list
                    leastsim_idx = waiting_list.index(leastsim_app) # del app from list
                    del waiting_list[leastsim_idx]
                    name2jobid[leastsim_app] = jobID # update name to jobID
                    jobid2name[jobID] =leastsim_app 

                    process = Process(target=run_work, args=(jobID, GpuJobTable,
                        leastsim_app, app2dir_dd))
                    process.daemon = False
                    workers.append(process)
                    process.start()
            
        else:
            #=================================#
            # the active jobs reach limit, wait
            #=================================#
            while True:
                #
                # spin
                #
                break_loop = False

                current_running_jobs = 0
                jobs2del = []

                for jobname in active_job_list:
                    jid = name2jobid[jobname]
                    if GpuJobTable[jid, 3] == 1: # check the status, if one is done
                        jobs2del.append(jid)  # add the jobID
                        break_loop = True

                if break_loop:
                    activeJobs -= 1

                    # update
                    if jobs2del:
                        for job_id in jobs2del:
                            appname = jobid2name[job_id]
                            del_idx = active_job_list.index(appname)
                            del active_job_list[del_idx]

                    break # stop spinning, exit while loop
                
            #------------------------------------
            # after spinning, schedule the work
            #------------------------------------

            # for the last application, go directly schedule it
            if i == apps_num_minus_one:
                leastsim_app = waiting_list[0]
            else:
                #leastsim_app = find_least_sim(active_job_list, app2app_dist, waiting_list)
                anotherApp = FindNextJob(active_job_list, app2app_dist, waiting_list, app2newfeat_dd)

            activeJobs += 1
            jobID += 1
            active_job_list.append(leastsim_app) # add app to the active job list
            leastsim_idx = waiting_list.index(leastsim_app) # del app from list
            del waiting_list[leastsim_idx]
            name2jobid[leastsim_app] = jobID # update name to jobID
            jobid2name[jobID] =leastsim_app 

            process = Process(target=run_work, args=(jobID, GpuJobTable,
                leastsim_app, app2dir_dd))
            process.daemon = False
            workers.append(process)
            process.start()


        #if i == 1: break


    #=========================================================================#
    # end of running all the jobs
    #=========================================================================#

    for p in workers:
        p.join()


    #if not waiting_list:
    #    logger.debug("[Warning] waiting_list should be empty at last.")


    total_jobs = jobID + 1
    PrintGpuJobTable(GpuJobTable, total_jobs)

    if total_jobs <> apps_num:
        logger.debug("[Warning] job number doesn't match.")




if __name__ == "__main__":
    main()
