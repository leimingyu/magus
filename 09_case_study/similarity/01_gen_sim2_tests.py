#!/usr/bin/env python

import os
import stat
import numpy as np

scriptDir="./sim2_tests"
if not os.path.exists(scriptDir):
    os.mkdir(scriptDir)


def gen_sim2(current_dir, app1, app1_dir, app2, app2_dir, scriptDir='sim2_tests'):
    outFileName=str(app1)+"_"+str(app2)+".sh"
    #print outFileName
    outFile= str(scriptDir)+"/"+outFileName

    print "\nOutput file : %s\n"  % outFile

    test_content="#!/bin/bash" + "\n" + \
    "timeApp () {" + "\n" + \
    "appname=$1" + "\n" + \
    "runapp=$2" + "\n" + \
    "devid=$3" + "\n" + \
    " " + "\n" + \
    "ts=$(date +%s%N)" + "\n" + \
    " " + "\n" + \
    "$runapp $devid > /dev/null" + "\n" + \
    " " + "\n" + \
    "runtime_ms=$((($(date +%s%N) - $ts)/1000000))" + "\n" + \
    " " + "\n" + \
    "echo -e \"\\n$appname:$runtime_ms\" >> /tmp/magic_time_log" + "\n" + \
    "}" + "\n" + \
    " " + "\n" + \
    "if [ -f /tmp/magic_time_log ]" + "\n" + \
    "then" + "\n" + \
    "  rm /tmp/magic_time_log" + "\n" + \
    "fi" + "\n" + \
    "touch /tmp/magic_time_log" + "\n" + \
    " " + "\n" + \
    " " + "\n" + \
    "ITER=10" + "\n"+ \
    "app1_keyword=\"" + app1 + "\""  + "\n" + \
    "app1=$app1_keyword" + "\n" + \
    " " + "\n" + \
    "app2_keyword=\"" + app2 + "\""  + "\n" + \
    "app2=$app2_keyword" + "\n" + \
    " " + "\n" + \
    "for (( i=1; i<=$ITER; i++ )) " + "\n" + \
    "do" + "\n"  + \
    "  cd " + app1_dir + "\n" + \
    "  timeApp $app1_keyword ./run.sh 0 &"  + "\n" + \
    " " + "\n" + \
    "  cd " + current_dir + "/" + scriptDir + "\n" + \
    "  cd " + app2_dir + "\n" + \
    "  timeApp $app2_keyword ./run.sh 0 &"  + "\n" + \
    " " + "\n" + \
    "  wait" + "\n" + \
    " " + "\n" + \
    "  cd " + current_dir + "/" + scriptDir + "\n" + \
    "done" + "\n" + \
    " " + "\n" + \
    "currentFile=`basename \"$0\"`" + "\n" + \
    "echo -e \"\\nTest Done! ($currentFile)\\nCheck /tmp/magic_time_log\\n\"" + "\n" + \
    " " + "\n" + \
    "getAvg() " + "\n" + \
    "{" + "\n" + \
    "local keyWord=$1" + "\n" + \
    "local runtime=$(awk -v pat=\"$keyWord\"  '$0~pat{print}' /tmp/magic_time_log  | awk -F \":\" '{print $2}' | awk '{ total += $1 } END { print total/NR }')" + "\n" + \
    "echo $runtime" + "\n" + \
    "}" + "\n" + \
    " " + "\n" + \
    "app1_runtime=$(getAvg $app1_keyword)" + "\n" + \
    "app2_runtime=$(getAvg $app2_keyword)" + "\n" + \
    " " + "\n" + \
    "echo -e $app1\":\\t\"$app1_runtime\"\\n\"$app2\":\\t\"$app2_runtime\"\\n\"" + "\n" + \
    " " + "\n"





    



    with open(outFile, "w+") as myfile:
        myfile.write(test_content)

    st = os.stat(outFile)
    os.chmod(outFile, st.st_mode | stat.S_IEXEC)


#==============================================================================#
# Main
#
#==============================================================================#
current_dir = os.getcwd()
print "current dir : %s" % current_dir

top3_leastsim_dd = np.load('top3_leastsim.npy').item()
app2dir_dd = np.load('../app2dir_dd.npy').item()

for app, top3_list in top3_leastsim_dd.iteritems():
    #print app, top3_list
    print "\nGenerating script for %s\n" % app
    #print("least similar : {}".format(app,top3_list[0][0]))
    
    app1 = app
    app1_dir = app2dir_dd[app1]
    app1_dir = "../../" + app1_dir
    print app1_dir

    app2 = top3_list[0][0]
    app2_dir = app2dir_dd[app2]
    app2_dir = "../../" + app2_dir
    print app2_dir

    #
    # generate test script
    #

    #app1 = app1.replace("_", "-")
    app1 = app1.replace("+", "")

    #app2 = app2.replace("_", "-")
    app2 = app2.replace("+", "")
    #print app1, app2
    gen_sim2(current_dir, app1, app1_dir, app2, app2_dir)

    #break
