#!/usr/bin/env python

import os
import stat

scriptDir="test_single"
if not os.path.exists(scriptDir):
    os.mkdir(scriptDir)

# app, app_keyword, app_cmd
appsInfo = [
["binopt",                "binomialOptions",       "../../13apps/binomialOptions/binomialOptions"],
["convfft2d",             "convolutionFFT2D",      "../../13apps/convolutionFFT2D/convolutionFFT2D"],
["interval",              "interval",              "../../13apps/interval/interval"],
["matrixMul",             "matrixMul",             "../../13apps/matrixMul/matrixMul"],
["MC_SingleAsianOptionP", "MC_SingleAsianOptionP", "../../13apps/MC_SingleAsianOptionP/MC_SingleAsianOptionP"],
["mergeSort",             "mergeSort",             "../../13apps/mergeSort/mergeSort"],
["quasirandomGenerator",  "quasirandomGenerator",  "../../13apps/quasirandomGenerator/quasirandomGenerator"],
["radixSortThrust",       "radixSortThrust",       "../../13apps/radixSortThrust/radixSortThrust"],
["reduction",             "reduction",             "../../13apps/reduction/reduction"],
["scan",                  "scan",                  "../../13apps/scan/scan"],
["SobolQRNG",             "SobolQRNG",             "../../13apps/SobolQRNG/SobolQRNG"],
["sortingNetworks",       "sortingNetworks",       "../../13apps/sortingNetworks/sortingNetworks"],
["transpose",             "transpose",             "../../13apps/transpose/transpose"]
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
    "ITER=20" + "\n" + \
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


