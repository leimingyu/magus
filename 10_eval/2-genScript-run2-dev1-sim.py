#!/usr/bin/env python
import sys,os,stat,time,math,random,copy
import operator

from subprocess import check_call, STDOUT
from time import sleep

import numpy as np

sys.path.append('./protobuf')
import GPUApp_pb2

DEVNULL = open(os.devnull, 'wb', 0) # no std out
#magus_debug = False 
magus_debug = True 

def gen_app_seq(current_dir, apps_list, apps_dir, outFile="xxx.sh"):
    file_content="#!/bin/bash" + "\n"

    pid = 1
    total_apps = len(apps_list) - 1
    
    count_jobs = 0
    for i, app in enumerate(apps_list):
        #app_cmd = str(app[1]) + ";" + str(app[2]) 
        #app_cmd = str(app[0]) # send the appName
        app_cmd = str(app) # send the appName
        app_dir = apps_dir[i]

        #print app_cmd, app_dir


        #
        # options: app_cmd, wait time and & (running in bg)
        #
        file_content += "cd " + str(app_dir) + "\n"
        file_content += "./run.sh 0 &\n"
        file_content += "cd " + str(current_dir) + "\n\n"

        if i % 2 == 1:
            file_content += "wait\n\n"

        count_jobs = i


    #print("\n[LOG] Generate total jobs = {}.".format(count_jobs + 1))

    with open(outFile, "w+") as myfile:                                         
        myfile.write(file_content)

    st = os.stat(outFile)
    os.chmod(outFile, st.st_mode | stat.S_IEXEC)

#=============================================================================#
# pick combo to corun, based on similarity
#=============================================================================#
def find_index(appList_update, target_app_name):
    idx = None
    for i, appName in enumerate(appList_update):
        if appName == target_app_name:
            idx = i
            break
    return idx


def gen_app_seq_sim(current_dir, apps_list, apps_dir_dd, app2app_dist, outFile="xxx.sh"):
    file_content="#!/bin/bash" + "\n"

    pid = 1
    total_apps = len(apps_list) - 1

    appList_update = copy.deepcopy(apps_list)
    
    count_jobs = 0
    for i, app in enumerate(apps_list):

        if i == 0: # add start timer
            file_content += "ts=$(date +%s%N)\n"

        app_name = str(app) # send the appName
        app_dir  = apps_dir_dd[app_name]
        #print app_name, app_dir

        dist_dd = app2app_dist[app_name]

        if app_name in appList_update:
            #print app_name
            # select the least similar app to corun: the largest euclidean dist
            # non-decreasing order
            dist_dd_sorted = sorted(dist_dd.items(), key=operator.itemgetter(1))

            leastsim_app = None
            for appname_and_dist in reversed(dist_dd_sorted):
                sel_appname = appname_and_dist[0]
                if sel_appname in appList_update:
                    leastsim_app = sel_appname

            #print("combo : {} + {}\n".format(app_name, leastsim_app))

            if leastsim_app is None:
                # the only app left
                file_content += "cd " + str(app_dir) + "\n"
                file_content += "./run.sh 0 &\n"
                file_content += "cd " + str(current_dir) + "\n\n"

            else:

                #==========#
                # generate script for the combo 
                #==========#

                # options: app_cmd, wait time and & (running in bg)
                file_content += "cd " + str(app_dir) + "\n"
                file_content += "./run.sh 0 &\n"
                file_content += "cd " + str(current_dir) + "\n\n"

                app2_dir = apps_dir_dd[leastsim_app]
                file_content += "cd " + str(app2_dir) + "\n"
                file_content += "./run.sh 0 &\n"
                file_content += "cd " + str(current_dir) + "\n\n"

                file_content += "wait\n\n"

                #========#
                # remove the combo
                #========#
                app_idx = find_index(appList_update, app_name)   # remove current app
                if app_idx is None:
                    print "Something is wrong!"
                    sys.exit(1)
                else:
                    del appList_update[app_idx]

                app_idx = find_index(appList_update, leastsim_app)  # remove the combo target
                if app_idx is None:
                    print "Something is wrong!"
                    sys.exit(1)
                else:
                    del appList_update[app_idx]

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
    #=========================================================================#
    #[1] read app name and app dir 
    #    randomize their index for different sequences
    #=========================================================================#
    #apps_list = get_appinfo('./prepare/app_info.bin')
    apps_list = get_appinfo('./prepare/app_info_79.bin')
    #apps_list = get_appinfo('./prepare/app_info_v1.bin')
    #apps_list = get_appinfo('./prepare/bigjob_info_rcuda.bin')

    ##if magus_debug: 
    ##    print "\n[DEBUG] Check 5 app info : "
    ##    dump_applist(apps_list[:5]) # print the 1st 5 appinfo

    ##apps_num = len(apps_list)
    ##print("\n[log] Total GPU Applications : {}.".format(apps_num))

    #
    # use 78 instead of 79
    #
    print("del the last app {}".format(apps_list[-1]))
    del apps_list[-1]
    apps_num = len(apps_list)
    print("\n[LOG] Total GPU Applications : {}.".format(apps_num))



    #----------
    #  3 different app launch sequences
    #----------
    app_name = [v[0] for v in apps_list]
    app_dir  = [v[1] for v in apps_list]
    #print app_name[:3]
    #print app_dir[:3]


    # test 2
    print "\n[log]test1 : randomize the index\n"
    random.seed(a=1010)
    idx = [i for i in xrange(0, apps_num)]
    #print idx
    random.shuffle(idx)
    #print idx
    app_v1     = [app_name[i] for i in idx]
    app_v1_dir = [app_dir[i] for i in idx]
    app_v1_dir_dd = {}
    for i in idx:
        appName = app_v1[i]
        appDir = app_v1_dir[i]
        app_v1_dir_dd[appName] = appDir



    ##for appName in app_v1:
    ##    print appName 

    # test 2
    print "\n[log]test2 : randomize the index\n"
    random.seed(a=321)
    idx = [i for i in xrange(0, apps_num)]
    random.shuffle(idx)
    app_v2     = [app_name[i] for i in idx]
    app_v2_dir = [app_dir[i] for i in idx]
    #print app_v2[:3]
    app_v2_dir_dd = {}
    for i in idx:
        appName = app_v2[i]
        appDir = app_v2_dir[i]
        app_v2_dir_dd[appName] = appDir

    # test 3
    print "\n[log]test3 : randomize the index\n"
    random.seed(a=830)
    idx = [i for i in xrange(0, apps_num)]
    random.shuffle(idx)
    app_v3     = [app_name[i] for i in idx]
    app_v3_dir = [app_dir[i] for i in idx]
    #print app_v3[:3]
    app_v3_dir_dd = {}
    for i in idx:
        appName = app_v3[i]
        appDir = app_v3_dir[i]
        app_v3_dir_dd[appName] = appDir


    #=========================================================================#
    # [2] read app metrics
    #       update their euclidean dist for similarity approach
    #=========================================================================#
    app2metric_dd = np.load("../07_sim_devid/similarity/app2metric_dd.npy").item()

    if len(app2metric_dd) == len(app_name):
        print "\n[log] The length of app_name and app2metric_dd matches!"


    FOUND_ERROR = False
    for key, _ in app2metric_dd.iteritems():
        if key not in app_name:
            print("\n[Warning] {} not found in app_name!\n".format(key))
            FOUND_ERROR = True

    if FOUND_ERROR:
        print("\n[Warning] Please check the previous error messages!\nExiting!\n")
        #sys.exit(1)
    else:
        print "\n[log] Names in app_name and app2metric_dd matches!\n"
        print "\n[log] Good Job!\n"



    #=====================================#
    # compute the euclidean distance between app metrics
    #=====================================#
    print "\n[log] Compute euclidean dist between apps.\n"
    app2app_dist = {}
    for app1, metric1 in app2metric_dd.iteritems():
        curApp_dist = {}
        m1 = metric1.as_matrix()
        for app2, metric2 in app2metric_dd.iteritems():
            if app1 <> app2:
                m2 = metric2.as_matrix()
                curApp_dist[app2] = np.linalg.norm(m1 - m2) 

        app2app_dist[app1] = curApp_dist

    print "\n[log] Finish computing dist.\n"


    ##for key, app_dist in app2app_dist.iteritems():
    ##    print key
    ##    print app_dist
    ##    break


    #=========================================================================#
    # [3] generate script based on the similarity 
    #=========================================================================#
    print "\n"
    current_dir = os.getcwd()
    
    print "(similarity) Generating script => [single device, run2] sequence 1 "
    gen_app_seq_sim(current_dir, app_v1, app_v1_dir_dd, app2app_dist, outFile="runseq1_dev1_sim.sh")

    print "(similarity) Generating script => [single device, run2] sequence 2 "
    gen_app_seq_sim(current_dir, app_v2, app_v2_dir_dd, app2app_dist, outFile="runseq2_dev1_sim.sh")

    print "(similarity) Generating script => [single device, run2] sequence 3 "
    gen_app_seq_sim(current_dir, app_v3, app_v3_dir_dd, app2app_dist, outFile="runseq3_dev1_sim.sh")

    print "All Done!"


if __name__ == "__main__":
    main()
