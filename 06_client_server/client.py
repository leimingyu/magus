#!/usr/bin/env python
import sys,os
import socket
import time
import math
import random
import multiprocessing as mp

from subprocess import check_call, STDOUT
from time import sleep

sys.path.append('./protobuf')
import GPUApp_pb2

DEVNULL = open(os.devnull, 'wb', 0) # no std out
#magus_debug = False 
magus_debug = True 

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


#------------------------------------------------------------------------------
# print appinfo in the list 
#------------------------------------------------------------------------------
def dump_applist(input_list):
    for app in input_list:
        print str(app[0]) + " : [" + str(app[1]) + ", " + str(app[2]) + "]"


#------------------------------------------------------------------------------
# workload pattern for start time
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
# send msg to server 
#------------------------------------------------------------------------------
def send2server(msg_to_pass, sleeptime):
    time_to_sleep = float(sleeptime)

    # wait for starting
    time.sleep(time_to_sleep)

    # start connection
    # create socket for ipv4 with tcp 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect(("localhost", 9000))
    #sock.connect(("155.33.203.180", 9000))

    print time.time()

    data = str(msg_to_pass) 
    print "send : ", data
    sock.sendall(data)

    #result = sock.recv(1024)
    #print result

    #
    # finish all the client work
    #
    sock.close()

def main():
    #
    # read app info
    #
    apps_list = get_appinfo('./prepare/app_info.bin')

    if magus_debug: 
        dump_applist(apps_list[:5]) # print the 1st 5 appinfo

    apps_num = len(apps_list)
    print "Total GPU Applications : " + str(apps_num)

    #
    # schedule app starting time 
    #
    apps_start_list = getAppStartTime(apps_num, interval_sec=1, pattern="fixed")

    if magus_debug:
        print apps_start_list
    
    #
    # obtain the waiting time between jobs
    #
    wait_time_list = [ (apps_start_list[i] - apps_start_list[i-1]) for i in xrange(1, apps_num)]

    if magus_debug:
        print wait_time_list
        print len(wait_time_list)

    #
    # send commands to server 
    #
    pid = 1
    total_apps = len(apps_list) - 1
    
    for i, app in enumerate(apps_list):
        if i == 0:
            wait_time = 0 
        else:
            wait_time = wait_time_list[i - 1] 

        app_cmd = str(app[1]) + ";" + str(app[2]) 
        #print app_cmd

        # sending cmd to server
        send2server(app_cmd, wait_time)
        break



if __name__ == "__main__":
    main()
