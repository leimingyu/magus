#!/usr/bin/env python
"""
 schedule rcuda apps
"""
#from __future__ import print_function
import sys
#sys.path.insert(0, './protobuf')
sys.path.append('./protobuf')

import GPUApp_pb2
import os
#import argparse
import multiprocessing as mp
import time
from subprocess import check_call, STDOUT
#import logging # logging multiprocessing 
import math
import random


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


def run_mp(timingQ, app_dir, app_cmd):
    """
    Run multiprocessing
    """
    startT = time.time()
    with cd(app_dir):
        #print os.getcwd()
        check_call(app_cmd, stdout=DEVNULL, stderr=STDOUT, shell=True)
    endT = time.time()
    #print("{} to {} = {:.3f} seconds".format(startT, endT, endT - startT))
    timingQ.put([startT, endT])



'''
def run_remote(app_dir, *args):
    """
    go to app dir, and run mp for the app
    """
    arg_num = len(args)

    timingQ = mp.Queue()

    if arg_num > 0:
        cmd_str = ' '.join(str(e) for e in args)
        #multiprocessing.log_to_stderr(logging.DEBUG)
        p = mp.Process(target=run_mp, args=(timingQ, app_dir, cmd_str))
        p.start()

    else:
        sys.exit('<Error : run_remote> No application is specified!')

    [startT, endT] = timingQ.get()
    return [startT, endT]
    #print("{} to {} = {:.3f} seconds".format(startT, endT, endT - startT))
    '''


def run_remote(app_dir, app_cmd, devid=0):
    rcuda_select_dev = "RCUDA_DEVICE_0=mcx1.coe.neu.edu:" + str(devid)
    cmd_str = rcuda_select_dev + " " + str(app_cmd)

    timingQ = mp.Queue()

    p = mp.Process(target=run_mp, args=(timingQ, app_dir, cmd_str))
    p.start()

    [startT, endT] = timingQ.get()

    return [startT, endT]

    #run_remote(app_dir, rcuda_select_dev, app_cmd)


#------------------------------------------------------------------------------
# tests
#------------------------------------------------------------------------------
''' def test1_run2():
    run_remote('../apps/rcuda_cusdk80/0_Simple/matrixMul/', './matrixMul')
    run_remote('../apps/rcuda_cusdk80/0_Simple/vectorAdd/', './vectorAdd')

def test2_selDev():
    [startT, endT] = run_remote('../apps/rcuda_cusdk80/0_Simple/matrixMul/', 
            'RCUDA_DEVICE_0=mcx1.coe.neu.edu:0', './matrixMul')
    print("{} to {} = {:.3f} seconds".format(startT, endT, endT - startT))

    [startT, endT] = run_remote('../apps/rcuda_cusdk80/0_Simple/vectorAdd/', 
            'RCUDA_DEVICE_0=mcx1.coe.neu.edu:1', './vectorAdd')
    print("{} to {} = {:.3f} seconds".format(startT, endT, endT - startT)) '''




def test3_fixedT(maxjobs = 10):
    count = 0
    while True:
        # run job
        # wait for a fixed interval
        # check termination
        print count
        #time.sleep(1)
        time.sleep(0.1)
        count = count + 1
        if count == maxjobs:
            break
    print "Done!"
        

def nextTime(rateParameter):
    return -math.log(1.0 - random.random()) / rateParameter

def test4_poissonDist():
# http://preshing.com/20111007/how-to-generate-random-timings-for-a-poisson-process/
    print sum([nextTime(1/40.0) for i in xrange(1000000)]) / 1000000
    print sum([random.expovariate(1/40.0) for i in xrange(1000000)]) / 1000000
    
def test5_wk(total_jobs, interval_sec=1, rate=1, pattern="fixed"):
    if total_jobs <=0:
       sys.exit('<Error> total_jobs can not be zero or negative!')

    if type(total_jobs) <> int:
       sys.exit('<Error> total_jobs should be integer.!')

    jobs_start_table = []

    if pattern == "fixed":
        jobs_start_table = [i*interval_sec for i in xrange(total_jobs)]
    elif pattern == "poisson":
        jobs_start_table = [random.expovariate(rate) for i in xrange(total_jobs)]
        jobs_start_table.sort()
    else:
       sys.exit('<Error : run_remote> No application is specified!')

    print jobs_start_table

#------------------------------------------------------------------------------
# tests 
#------------------------------------------------------------------------------
def tests():
    #test1_run2()
    #test2_selDev()
    #test3_fixedT()
    test4_poissonDist()
    #test5_wk(10,interval_sec=2, pattern="fixed")
    #test5_wk(10, rate=1/5.0, pattern="poisson")


#------------------------------------------------------------------------------
# 1) get app info
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


def dump_dd(input_dd):
    for key, value in input_dd.iteritems():
        print key
        print value

def dump_applist(input_list):
    for app in input_list:
        print str(app[0]) + " : [" + str(app[1]) + ", " + str(app[2]) + "]"

#------------------------------------------------------------------------------
# 2) workload pattern for start time
#------------------------------------------------------------------------------
def getAppStartTime(total_jobs, interval_sec=1, pattern="fixed"):
    if total_jobs <= 0:
        sys.exit('<Error> total_jobs can not be zero or negative!')
    if type(total_jobs) <> int:
        sys.exit('<Error> total_jobs should be integer.!')
    jobs_start_table = []
    if pattern == "fixed":
        jobs_start_table = [i*interval_sec for i in xrange(total_jobs)]
    elif pattern == "poisson":
        rate = 1 / float(interval_sec)
        jobs_start_table = [random.expovariate(rate) for i in xrange(total_jobs)]
        jobs_start_table.sort()
    else:
        sys.exit('<Error : getAppStartTime()> Wrong pattern is specified!')
    return jobs_start_table


#------------------------------------------------------------------------------
# 3) dispatch work from the client 
#------------------------------------------------------------------------------
def client_dispatch_apps(apps_list, wait_time_list):

    from time import sleep

    print "\nDispatching gpu applications"

    ### to-do: shuffle the order of input apps
    pid = 1
    total_apps = len(apps_list) - 1

    for app in apps_list:
        # 1) start the job at the background
        target_dev = 0

        #[startT, endT]= run_remote(app_dir = app[1], app_cmd = app[2], devid = target_dev) 


        # 2) terminate if it is the last job
        if pid > total_apps: 
            break

        # 3) wait for a certain time to schedule the next job
        wait_time = wait_time_list[pid - 1]
        sleep(wait_time)
        #print str(pid) + " : wait for " + str(wait_time) + " (s) to start next"

        pid = pid + 1

#------------------------------------------------------------------------------
# main func 
#------------------------------------------------------------------------------
def main(args):
    #tests()

    #
    # 1) read app_info
    #

    apps_list = get_appinfo('./prepare/app_info.bin')
    if magus_debug: dump_applist(apps_list)

    apps_num = len(apps_list)
    print "Total GPU Applications : " + str(apps_num)

    #
    # 2) figure out the application start time
    #
    #apps_start_list = getAppStartTime(apps_num, interval_sec=2, pattern="fixed")
    apps_start_list = getAppStartTime(apps_num, interval_sec=2, pattern="poisson")
    print apps_start_list

    wait_time_list = [ (apps_start_list[i] - apps_start_list[i-1]) for i in xrange(1, apps_num)]
    #print wait_time_list
    print len(wait_time_list)

    # 3) schedule apps
    client_dispatch_apps(apps_list, wait_time_list)

if __name__ == "__main__":
    main(sys.argv[1:])
