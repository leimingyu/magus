#!/usr/bin/env python

import os,sys
import operator
import copy
import random
import time
import numpy as np

from multiprocessing import Process, Lock, Manager, Value

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


#-----------------------------------------------------------------------------#
# Run incoming workload
#-----------------------------------------------------------------------------#
def handleWorkload(lock, corun, jobID, appName, app2dir_dd):
    '''
    schedule workloads on the gpu
    '''
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("(Job-%r)" % (jobID))

    try:
        with lock:
            corun.value = corun.value + 1

        print appName
        app_dir = app2dir_dd[appName]
        print app_dir 

        app_cmd = "./run.sh"
        target_dev = 0

        #=========================#
        # 
        #=========================#
        [startT, endT] = run_remote(app_dir=app_dir, app_cmd=app_cmd, devid=target_dev)


    except BaseException:
        logger.exception("Problem handling request")
    finally:
        logger.debug("Done.")


def main():
    #global app2dir
    #global app2cmd
    global app2metric
    global app2trace


    #===================#
    # 1) read app info
    #===================#
    #app2dir    = np.load('../07_sim_devid/similarity/app2dir_dd.npy').item()
    #app2cmd    = np.load('../07_sim_devid/similarity/app2cmd_dd.npy').item()
    app2metric = np.load('../07_sim_devid/similarity/app2metric_dd.npy').item()
    app2trace  = np.load('../07_sim_devid/perfmodel/app2trace_dd.npy').item()

    #print len(app2dir), len(app2cmd), len(app2metric), len(app2trace)

    appsList = get_appinfo('./prepare/app_info_79.bin')
    print appsList[0]

    #print appNameList

    #============================#
    # 2) randomize the app order 
    #============================#
    app_name = [v[0] for v in appsList]
    app_dir  = [v[1] for v in appsList]
    #print app_name
    #print app_dir 

    apps_num = len(appsList)
    logger.debug("Total GPU Applications = {}.".format(apps_num))
    

    random.seed(a=1010)
    idx = [i for i in xrange(0, apps_num)]
    #print idx
    random.shuffle(idx)
    #print idx
    app_seq        = [app_name[i] for i in idx]
    app_seq_dir    = [app_dir[i] for i in idx]
    app2dir_dd = {}
    for i in idx:
        appName = app_seq[i]
        appDir  = app_seq_dir[i]
        app2dir_dd[appName] = appDir


    #print app_seq[:2]
    #print app_seq_dir[:2]

    #==================================#
    # 3) shared variable for workqueue 
    #==================================#
    appQueList = manager.list()
    #appQueList = list(appQueList)

    #print type(appQueList)
    #print len(appQueList)

    for app in app_seq:
        appQueList.append(app)

    #print len(appQueList)
    #print app_seq[:3]
    #print appQueList[:3]
    #del appQueList[1]
    #print appQueList[:3]

    #==================================#
    # 4) run the apps in the queue 
    #==================================#
    MAXCORUN = 2
    #corun = 0
    corun = Value('i',0) 

    jobID = -1

    while appQueList:
        Dispatch = False 

        with lock:
            if corun.value <= MAXCORUN:
                Dispatch = True

        if Dispatch:
            jobID = jobID + 1

            cur_app = appQueList[0]
            del appQueList[0]

            logger.debug("Run {}".format(cur_app))

            process = Process(target=handleWorkload,
                                 args=(lock, corun, jobID, cur_app, app2dir_dd))

            process.daemon = False
            logger.debug("Start %r", process)
            process.start()
            process.join()

            #logger.debug("corun = %r", corun.value)

        break



if __name__ == "__main__":
    main()
