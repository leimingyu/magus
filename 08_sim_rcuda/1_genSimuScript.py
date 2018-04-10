#!/usr/bin/env python
import sys,os,stat,time,math,random
import copy
import socket
import multiprocessing as mp

from subprocess import check_call, STDOUT
from time import sleep

sys.path.append('./protobuf')
import GPUApp_pb2

DEVNULL = open(os.devnull, 'wb', 0) # no std out
#magus_debug = False 
magus_debug = True 

def gen_app_seq(apps_list, wait_time_list, outFile="xxx.sh", test_num = 0):
    file_content="#!/bin/bash" + "\n"

    pid = 1
    total_apps = len(apps_list) - 1
    
    count_jobs = 0
    for i, app in enumerate(apps_list):
        if i == 0:
            wait_time = 0 
        else:
            wait_time = wait_time_list[i - 1]   # add watiting time for current app 


        #app_cmd = str(app[1]) + ";" + str(app[2]) 
        #app_cmd = str(app[0]) # send the appName
        app_cmd = str(app) # send the appName


        #
        # call run_client.py, 
        # with options: app_cmd, wait time and & (running in bg)
        #
        file_content += "sleep " + str(wait_time) + "\n"
        file_content += "./run_client.py" + " \"" + app_cmd + "\" &\n"

        count_jobs = i

        if test_num <> 0 and i == test_num:
            break

    print("\n[LOG] Generate total jobs = {}.".format(count_jobs + 1))

    with open(outFile, "w+") as myfile:                                         
        myfile.write(file_content)

    st = os.stat(outFile)
    os.chmod(outFile, st.st_mode | stat.S_IEXEC)


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

    #print time.time()

    data = str(msg_to_pass) 
    print "[sending]:\n", data
    sock.sendall(data)

    #result = sock.recv(1024)
    #print result

    #
    # finish all the client work
    #
    sock.close()

def main():
    #
    # 1) read app info
    #
    #apps_list = get_appinfo('./prepare/app_info.bin')
    apps_list = get_appinfo('./1-prepare/bigjob_info_rcuda.bin')

    if magus_debug: 
        print "\n[DEBUG] Check 5 app info : "
        dump_applist(apps_list[:5]) # print the 1st 5 appinfo

    apps_num = len(apps_list)
    print("\n[LOG] Total GPU Applications : {}.".format(apps_num))


    #----------
    #  3 different app launch sequences
    #----------
    # test 1
    print "\ntest1"
    app_v1 = [v[0] for v in apps_list]
    print app_v1[:3]

    # test 2
    print "\ntest2"
    random.seed(a=321)
    idx = [i for i in xrange(0, apps_num)]
    #print idx
    random.shuffle(idx)
    #print idx
    app_v2 = [app_v1[i] for i in idx]
    print app_v2[:3]

    # test 3
    print "\ntest3"
    random.seed(a=830)
    idx = [i for i in xrange(0, apps_num)]
    #print idx
    random.shuffle(idx)
    #print idx
    app_v3 = [app_v1[i] for i in idx]
    print app_v3[:3]



    #
    # 2) schedule app starting time 
    #
    #apps_start_list = getAppStartTime(apps_num, interval_sec=1, pattern="fixed")
    apps_start_list = getAppStartTime(apps_num, interval_sec=5, pattern="fixed")

    if magus_debug:
        print "\n[DEBUG] App start time : "
        print apps_start_list
    
    #
    # obtain the waiting time between jobs
    #
    wait_time_list = [ (apps_start_list[i] - apps_start_list[i-1]) for i in xrange(1, apps_num)]

    if magus_debug:
        print "\n[DEBUG] App wait time : "
        print wait_time_list
        #print len(wait_time_list)

    #------------------------------
    # Generate script for clients 
    #------------------------------
    #gen_app_seq(app_v1, wait_time_list, outFile="2_runseq1_1s.sh")
    #gen_app_seq(app_v2, wait_time_list, outFile="2_runseq2_1s.sh")
    #gen_app_seq(app_v3, wait_time_list, outFile="2_runseq3_1s.sh")

    gen_app_seq(app_v1, wait_time_list, outFile="2_runseq1_5s.sh")
    gen_app_seq(app_v2, wait_time_list, outFile="2_runseq2_5s.sh")
    gen_app_seq(app_v3, wait_time_list, outFile="2_runseq3_5s.sh")


if __name__ == "__main__":
    main()
