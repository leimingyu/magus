#!/usr/bin/env python
import sys,os,stat,time,math,random
import copy
import socket
import multiprocessing as mp
import numpy as np

from subprocess import check_call, STDOUT
from time import sleep

sys.path.append('./protobuf')
import GPUApp_pb2

DEVNULL = open(os.devnull, 'wb', 0) # no std out
#magus_debug = False 
magus_debug = True 

def gen_app_seq(current_dir, run2_list, app2dir_dd, outFile="xxx.sh"):
    file_content="#!/bin/bash" + "\n"


    for i, run2_combo in enumerate(run2_list):
        app1, app2 = run2_combo
        app1_dir = app2dir_dd[app1]

        if app2:
            app2_dir = app2dir_dd[app2]

        if i == 0: # add start timer
            file_content += "ts=$(date +%s%N)\n"

        #
        # options: app_cmd, wait time and & (running in bg)
        #
        file_content += "cd " + str(app1_dir) + "\n"
        file_content += "./run.sh 0 &\n"
        file_content += "cd " + str(current_dir) + "\n\n"

        if app2:
            file_content += "cd " + str(app2_dir) + "\n"
            file_content += "./run.sh 0 &\n"
            file_content += "cd " + str(current_dir) + "\n\n"

        file_content += "wait\n\n"


    #print("\n[LOG] Generate total jobs = {}.".format(count_jobs + 1))

    #
    # wait and update the end timer
    #
    file_content += "wait\n\n"
    file_content += "runtime_ms=$((($(date +%s%N) - $ts)/1000000))\n"
    file_content += "echo -e \"\\n=> Total Runtime (ms):$runtime_ms\""
    

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
    apps_list = get_appinfo('./prepare/app_info_79.bin')

    app2dir_dd = {}
    for curr_app in apps_list:
        #print curr_app
        appname, appdir = curr_app[:2]
        app2dir_dd[appname] = appdir
    #print app2dir_dd


    #
    # 2) read run2 list
    #
    run2_seq1 = np.load('./case_studies/run2_mat1.npy')
    run2_seq2 = np.load('./case_studies/run2_mat2.npy')
    run2_seq3 = np.load('./case_studies/run2_mat3.npy')
    #print run2_seq1


    #------------------------------
    # Generate script for clients 
    #------------------------------
    print "\n"
    current_dir = os.getcwd()
    
    print "Generating script => [single device, run2] sequence 1"
    gen_app_seq(current_dir, run2_seq1, app2dir_dd, outFile="runseq1_dev1_newSel.sh")

    ##print "Generating script => [single device, run2] sequence 2"
    ##gen_app_seq(current_dir, app_v2, app_v2_dir, outFile="runseq2_dev1_baseline.sh")

    ##print "Generating script => [single device, run2] sequence 3"
    ##gen_app_seq(current_dir, app_v2, app_v2_dir, outFile="runseq3_dev1_baseline.sh")

    ##print "All Done!"


if __name__ == "__main__":
    main()
