#!/usr/bin/env python

import os
import stat

scriptDir="test_single"
if not os.path.exists(scriptDir):
    os.mkdir(scriptDir)

# app, app_keyword, app_cmd
appsInfo = [
["batchCUBLAS",                "batchCUBLAS",       "../../test_apps/batchCUBLAS/batchCUBLAS"],
["BlackScholes",                "BlackScholes",       "../../test_apps/BlackScholes/BlackScholes"],
["boxFilterNPP",                "boxFilterNPP",       "../../test_apps/boxFilterNPP/boxFilterNPP"],
["conjugateGradient",                "conjugateGradient",       "../../test_apps/conjugateGradient/conjugateGradient"],
["convolutionSeparable",                "convolutionSeparable",       "../../test_apps/convolutionSeparable/convolutionSeparable"],
["dct8x8",                "dct8x8",       "../../test_apps/dct8x8/dct8x8"],
["FDTD3d",                "FDTD3d",       "../../test_apps/FDTD3d/FDTD3d"],
["histogram",                "histogram",       "../../test_apps/histogram/histogram"],
["nvgraph_Pagerank",                "nvgraph_Pagerank",       "../../test_apps/nvgraph_Pagerank/nvgraph_Pagerank"],
["simpleCUFFT_callback",                "simpleCUFFT_callback",       "../../test_apps/simpleCUFFT_callback/simpleCUFFT_callback"]
]


def genScriptSingle(app1, app1_keyword, app1_cmd, scriptDir):
    outFileName=str(app1)+".sh"
    #print outFileName
    outFile= str(scriptDir)+"/"+outFileName
    print outFile

    test_content="#!/bin/bash" + "\n" + \
    "app1=\""+str(app1)+"\"" + "\n" + \
    "app1_keyword=\""+str(app1_keyword)+"\"" + "\n" + \
    "app1_cmd=\""+str(app1_cmd)+"\"" + "\n" + \
    "\n" + \
    "ITER=100" + "\n" + \
    "\n" + \
    "if [ -f time_log ]" + "\n" + \
    "then" + "\n" + \
    "  rm time_log" + "\n" + \
    "fi" + "\n" + \
    "touch time_log" + "\n" + \
    "\n" + \
    "for (( i=1; i<=$ITER; i++ ))" + "\n" + \
    "do" + "\n" + \
    "  ../timeApp.sh ${app1_cmd} &" + "\n" + \
    "  wait" + "\n" + \
    "done" + "\n" + \
    "\n" + \
    "getAvg()" + "\n" + \
    "{" + "\n" + \
    "local keyWord=$1" + "\n" + \
    "local runtime=$(awk -v pat=\"$keyWord\"  \'$0~pat{print}\' time_log  | awk -F \":\" \'{print $2}\' | awk \'{ total += $1 } END { print total/NR }\')" + "\n" + \
    "echo $runtime" + "\n" + \
    "}" + "\n" + \
    "\n" + \
    "testName=$app1" + "\n" + \
    "" + "\n" + \
    "app1_runtime=$(getAvg $app1_keyword)" + "\n" + \
    "" + "\n" + \
    "echo -e $testName\": \\t\"$app1\": \"$app1_runtime" + "\n"
    



    with open(outFile, "w+") as myfile:
        myfile.write(test_content)

    st = os.stat(outFile)
    os.chmod(outFile, st.st_mode | stat.S_IEXEC)


#
# Main
#
N = len(appsInfo)
count = 0
for i in xrange(N):
    #print appsInfo[i]
    [app1, app1_keyword, app1_cmd] = appsInfo[i]
    print("\nScript ({}) : {} ...".format(count, app1))
    genScriptSingle(app1, app1_keyword, app1_cmd, scriptDir)
    print("Done!\n")
    count = count + 1

print("\nTotal generated scripts = {} at {}".format(count, scriptDir))


