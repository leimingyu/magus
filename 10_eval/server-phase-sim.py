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
# 
#------------------------------------------------------------------------------
def concantenate_trace(trace1, trace2):
    trc1 = copy.deepcopy(trace1)
    trc2 = copy.deepcopy(trace2)
    
    prev_end = trc1[-1][2]
    
    offset = prev_end - trc2[0][1]
    
    for api in trc2:
        api[1] += offset
        api[2] += offset
        # append current (updated) api to prev trace
        trc1.append(api)
        
    #for i in trc1:
    #    print i
    
    return trc1

#------------------------------------------------------------------------------
# phase contention 
#------------------------------------------------------------------------------
def detect_phase_contention_timing(app1_trace, app2_trace):
	t1 = copy.deepcopy(app1_trace)
	t2 = copy.deepcopy(app2_trace)

	t1_start = t1[0][1]
	t2_start = t2[0][1]

	# offset t1 trace
	for i, api in enumerate(t1):
		api[1] -= t1_start
		api[2] -= t1_start

	# offset t2 trace
	for i, api in enumerate(t2):
		api[1] -= t2_start
		api[2] -= t2_start


	contention_count = 0
	contention_time = 0.

	for i, api in enumerate(t1):
		a1_type, a1_start, a1_end = api[:3]

		for app2 in t2:
			a2_type, a2_start, a2_end = app2[:3]

			OVLP = False
			ovlp_time = 0.

			if a2_start < a1_start < a2_end:
				OVLP = True
				if a1_end > a2_end:
					ovlp_time = a2_end - a1_start

				if a1_end < a2_end:
					ovlp_time = a1_end - a1_start


			if a2_start < a1_end < a2_end:
				OVLP = True
				if a1_start > a2_start:
					ovlp_time = a1_end - a1_start

				if a1_start < a2_start:
					ovlp_time = a1_end - a2_start



			if (a1_start < a2_start) and (a1_end > a2_end):
				OVLP = True
				ovlp_time = a2_end - a2_start

			if OVLP:
				if a1_type == a2_type:
					contention_count += 1
					contention_time += ovlp_time


	return contention_count, contention_time



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
def PrintGpuJobTable(GpuJobTable, total_jobs, jobid2name):
    print("JobID\tStart\tEnd\tDuration")
    start_list = []
    end_list = []
    for row in xrange(total_jobs):
        print("{}\t{}\t{}\t{}\t{}".format(GpuJobTable[row, 0],
            GpuJobTable[row, 1],
            GpuJobTable[row, 2],
            GpuJobTable[row, 2] - GpuJobTable[row, 1],
            jobid2name[row]))

        start_list.append(GpuJobTable[row, 1])
        end_list.append(GpuJobTable[row, 2])


    total_runtime = max(end_list) - min(start_list) 
    print("total runtime = {} (s)".format(total_runtime))


#-----------------------------------------------------------------------------#
# GPU Job Table 
#-----------------------------------------------------------------------------#
def FindNextJob(active_job_list, app2app_dist, waiting_list, app2trace_simplify_dd):
    ###
    ### continue to select app that appDur is the smallest
    ###
    ##app2_name= None

    ##for app in appDur_sorted_dd:
    ##    appName = app[0]
    ##    if appName in waiting_list:
    ##        app2_name = appName 
    ##        break

    job_name = active_job_list[0]
	
    if len(waiting_list) >= 2:
		curr_trace = app2trace_simplify_dd[job_name]
		a1, a2 = waiting_list[:2]

		trace1 = app2trace_simplify_dd[a1]
		trace2 = app2trace_simplify_dd[a2]

		new12 = concantenate_trace(trace1, trace2)
		new21 = concantenate_trace(trace2, trace1)

		(_, t12) = detect_phase_contention_timing(curr_trace, new12)
		(_, t21) = detect_phase_contention_timing(curr_trace, new21)

		if t12 > t21:
			return a2
		else:
			return a1

    else:
		#--------------------------# 
		# run similarity analysis
		#--------------------------# 
		dist_dd = app2app_dist[job_name] # get the distance dict
		dist_sorted = sorted(dist_dd.items(), key=operator.itemgetter(1))

		leastsim_app = None
		# the sorted in non-decreasing order, use reversed()
		for appname_and_dist in reversed(dist_sorted):
			sel_appname = appname_and_dist[0]
			if sel_appname in waiting_list: # find 1st app in the list, and exit
				leastsim_app = sel_appname
				break

		##print("\n{} <<select>> {}\n".format(job_name, leastsim_app))

		return leastsim_app




def InitTwoJobs(waiting_list, appDur_sorted_dd, cpuTime_sorted_dd, app2app_dist, app2newfeat_dd, DEVLMT = 57344):
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

    #print len(waiting_list)

    # there are 3 apps in the queue
    # [appDur, cpuTime, gpuTime, threads_max, threads_avg, reg_max, reg_avg, sm_max, sm_avg, trans_max, trans_avg]
    if len(waiting_list) == 3:
		#app1_avg_threads = app2newfeat_dd[app1_name][4]  # avg threads
		#print app1_avg_threads
		[c1, c2] = [i for i in waiting_list if i <> app1_name]
		c1_threads = app2newfeat_dd[c1][4]  # avg threads
		c2_threads = app2newfeat_dd[c2][4]  # avg threads

		if c1_threads>DEVLMT and c2_threads > DEVLMT:
			ratio = float(c1_threads/c2_threads)
			if ratio > 1.5:
				return [app1_name, c2]  # select app with less threads
			if ratio < 0.67:
				return [app1_name, c1]  # select app with less threads






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


    ## if there is no smaller choice, select the shortest appDur to corun
    #app2_name = appDur_sorted_dd[0][0]


	# if there is no smaller choice, run with similarity

    #--------------------------# 
    # run similarity analysis
    #--------------------------# 
    dist_dd = app2app_dist[app1_name] # get the distance dict
    dist_sorted = sorted(dist_dd.items(), key=operator.itemgetter(1))

    # the sorted in non-decreasing order, use reversed()
    for appname_and_dist in reversed(dist_sorted):
        sel_appname = appname_and_dist[0]
        if sel_appname in waiting_list: # find 1st app in the list, and exit
            app2_name = sel_appname
            break

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
    app_seq_list = []
    for v in appsList:
        app2dir_dd[v[0]] = v[1] 
        app_seq_list.append(v[0])


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
    app2trace_simplify_dd = np.load('./case_studies/app2trace_simplify_dd.npy').item()






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

    ##launch_list = ['shoc_lev1reduction', 
    ##        'poly_correlation', 
    ##        'cudasdk_interval', 
    ##        'cudasdk_MCEstimatePiInlineQ' 
    ##        ] 

    ##launch_list = copy.deepcopy(app_seq_list)


    #=========================================================================#
    # sensitive cases:
    #=========================================================================#

    #launch_list = ['rodinia_pathfinder', 'lonestar_mst', 'cudasdk_MCEstimatePiQ']
    #launch_list = ['cudasdk_transpose', 'cudasdk_MCEstimatePiInlineQ', 'cudasdk_reduction']
    #launch_list = ['cudasdk_boxFilterNPP', 'cudasdk_simpleCUBLAS', 'cudasdk_shflscan']
    #launch_list = ['poly_bicg', 'cudasdk_MCEstimatePiP', 'rodinia_lud']
    #launch_list = ['cudasdk_dxtc', 'rodinia_needle', 'cudasdk_matrixMul']
    #launch_list = ['cudasdk_MCEstimatePiInlineP', 'poly_atax', 'parboil_mriq']
    #launch_list = ['shoc_lev1reduction', 'poly_gemm', 'cudasdk_simpleCUFFTcallback']
    #launch_list = ['rodinia_hotspot', 'shoc_lev1sort', 'cudasdk_scalarProd']
    #launch_list = ['parboil_stencil', 'cudasdk_MCSingleAsianOptionP', 'rodinia_lavaMD']
    #launch_list = ['rodinia_gaussian', 'rodinia_backprop', 'cudasdk_vectorAdd']
    #launch_list = ['parboil_sgemm', 'cudasdk_concurrentKernels', 'cudasdk_lineOfSight']

    #-------------
    # run4
    #-------------

    #launch_list = ['shoc_lev1sort', 'parboil_stencil', 'cudasdk_MCEstimatePiP', 'poly_atax']
    #launch_list = ['rodinia_lavaMD', 'cudasdk_matrixMul', 'cudasdk_MCEstimatePiQ', 'cudasdk_shflscan']
    #launch_list = ['cudasdk_boxFilterNPP', 'cudasdk_vectorAdd', 'parboil_sgemm', 'rodinia_pathfinder']
    #launch_list = ['cudasdk_reduction', 'rodinia_lud', 'lonestar_mst', 'rodinia_hotspot']
    #launch_list = ['cudasdk_lineOfSight', 'rodinia_gaussian', 'parboil_mriq', 'cudasdk_MCEstimatePiInlineP']
    #launch_list = ['shoc_lev1reduction', 'poly_bicg', 'rodinia_needle', 'cudasdk_simpleCUBLAS']
    #launch_list = ['cudasdk_dxtc', 'cudasdk_MCEstimatePiInlineQ', 'rodinia_backprop', 'cudasdk_transpose']
    launch_list = ['cudasdk_scalarProd', 'cudasdk_concurrentKernels', 'cudasdk_MCSingleAsianOptionP', 'poly_gemm']

    #-------------
    # run5
    #-------------
    #launch_list = ['poly_bicg', 'cudasdk_dxtc', 'parboil_sgemm', 'cudasdk_MCSingleAsianOptionP', 'cudasdk_MCEstimatePiInlineP']
    #launch_list = ['cudasdk_reduction', 'rodinia_lavaMD', 'shoc_lev1sort', 'poly_gemm', 'cudasdk_MCEstimatePiInlineQ']
    #launch_list = ['rodinia_gaussian', 'cudasdk_lineOfSight', 'cudasdk_boxFilterNPP', 'cudasdk_shflscan', 'cudasdk_scalarProd']
    #launch_list = ['cudasdk_concurrentKernels', 'rodinia_backprop', 'lonestar_mst', 'cudasdk_vectorAdd', 'rodinia_pathfinder']
    #launch_list = ['cudasdk_transpose', 'rodinia_lud', 'cudasdk_MCEstimatePiP', 'parboil_mriq', 'rodinia_needle']
    #launch_list = ['cudasdk_simpleCUFFTcallback', 'parboil_stencil', 'poly_atax', 'cudasdk_simpleCUBLAS', 'rodinia_hotspot']





    #
    # robust cases:
    #
    #launch_list = ['cudasdk_BlackScholes', 'poly_covariance', 'shoc_lev1fft']
    #launch_list = ['shoc_lev1md5hash', 'shoc_lev1BFS','cudasdk_stereoDisparity'] 
    #launch_list = ['cudasdk_convolutionFFT2D', 'cudasdk_convolutionSeparable', 'cudasdk_sortingNetworks']
    #launch_list = ['cudasdk_dwtHaar1D', 'cudasdk_binomialOptions', 'poly_correlation']
    #launch_list = ['poly_fdtd2d', 'poly_syr2k', 'cudasdk_dct8x8'] 
    #launch_list = ['cudasdk_fastWalshTransform', 'cudasdk_convolutionTexture','cudasdk_FDTD3d']





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
    firsttwojobs = InitTwoJobs(waiting_list, appDur_sorted, cpuTime_sorted, app2app_dist, app2newfeat_dd)
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

                anotherApp = FindNextJob(active_job_list, app2app_dist, waiting_list, app2trace_simplify_dd)
                #anotherApp = FindNextJob(waiting_list, appDur_sorted)


                if anotherApp is None:
                    logger.debug("[Warning] anotherApp is None!")
                else:
                    #
                    # run the selected app
                    #
                    activeJobs += 1
                    jobID += 1
                    active_job_list.append(anotherApp) # add app to the active job list
                    leastsim_idx = waiting_list.index(anotherApp) # del app from list
                    del waiting_list[leastsim_idx]

                    name2jobid[anotherApp] = jobID # update name to jobID
                    jobid2name[jobID] = anotherApp 

                    process = Process(target=run_work, args=(jobID, GpuJobTable,
                        anotherApp, app2dir_dd))
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
                anotherApp = waiting_list[0]
            else:
                anotherApp = FindNextJob(active_job_list, app2app_dist, waiting_list, app2trace_simplify_dd)
                #anotherApp = FindNextJob(waiting_list, appDur_sorted)

            activeJobs += 1
            jobID += 1
            active_job_list.append(anotherApp) # add app to the active job list
            leastsim_idx = waiting_list.index(anotherApp) # del app from list
            del waiting_list[leastsim_idx]

            name2jobid[anotherApp] = jobID # update name to jobID
            jobid2name[jobID] = anotherApp

            process = Process(target=run_work, args=(jobID, GpuJobTable,
                anotherApp, app2dir_dd))
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
    PrintGpuJobTable(GpuJobTable, total_jobs, jobid2name)

    if total_jobs <> apps_num:
        logger.debug("[Warning] job number doesn't match.")




if __name__ == "__main__":
    main()
