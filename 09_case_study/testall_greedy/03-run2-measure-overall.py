#!/usr/bin/env python

import os
import stat
import numpy as np
import shutil

scriptDir="./run2_overall"
if not os.path.exists(scriptDir):
    os.mkdir(scriptDir)
else:
    # remove and mkdir agian
    shutil.rmtree(scriptDir)
    os.mkdir(scriptDir)



def gen_run2(current_dir, app1, app1_dir, app2, app2_dir, scriptDir='run2_overall'):
    outFileName=str(app1)+"_"+str(app2)+".sh"
    #print outFileName
    outFile= str(scriptDir)+"/"+outFileName

    print "\nOutput file : %s\n"  % outFile
    test_content="#!/bin/bash" + "\n" + \
    "ITER=5" + "\n"+ \
    "for (( i=1; i<=$ITER; i++ )) " + "\n" + \
    "do" + "\n"  + \
    "  echo \"iter : $i\"" + "\n"  + \
    "  ts=$(date +%s%N)" + "\n"  + \
    "  cd " + app1_dir + "\n" + \
    "  ./run.sh 0 > /dev/null &"  + "\n" + \
    " " + "\n" + \
    "  cd " + current_dir + "/" + scriptDir + "\n" + \
    "  cd " + app2_dir + "\n" + \
    "  ./run.sh 0 > /dev/null &"  + "\n" + \
    " " + "\n" + \
    "  wait" + "\n" + \
    "  runtime_ms=$((($(date +%s%N) - $ts)/1000000))" +  "\n" + \
    "  echo -e \"\\n$runtime_ms\"" +  "\n" + \
    " " + "\n" + \
    "  cd " + current_dir + "/" + scriptDir + "\n" + \
    "done" + "\n" + \
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

#top3_leastsim_dd = np.load('top3_leastsim.npy').item()
app2dir_dd = np.load('../app2dir_dd.npy').item()


for app1, _ in app2dir_dd.iteritems():
    ##print "\nGenerating script for %s\n" % app1

    ##for app2, _ in app2dir_dd.iteritems():
    ##    if app2 <> app1:
    ##        a1 = app1
    ##        a1_dir = app2dir_dd[a1]
    ##        a1_dir = "../../" + a1_dir
    ##        print a1_dir
    ##       
    ##        a2 = app2 
    ##        a2_dir = app2dir_dd[a2]
    ##        a2_dir = "../../" + a2_dir
    ##        print a2_dir
    ##        
    ##        #app1 = app1.replace("_", "-")
    ##        a1 = a1.replace("+", "")
    ##        
    ##        #app2 = app2.replace("_", "-")
    ##        a2 = a2.replace("+", "")
    ##        print a1, a2

    ##        gen_run2(current_dir, a1, a1_dir, a2, a2_dir)
    ##        #break

    #if app1 == "cudasdk_batchCUBLAS": 
    #if app1 == "cudasdk_binomialOptions": 
    #if app1 == "cudasdk_BlackScholes": 
    #if app1 == "cudasdk_boxFilterNPP": 
    #if app1 == "cudasdk_c++11Cuda": 
    if app1 == "cudasdk_concurrentKernels": 
    #if app1 == "cudasdk_convolutionFFT2D": 
    #if app1 == "cudasdk_convolutionSeparable": 
    #if app1 == "cudasdk_convolutionTexture": 
    #if app1 == "cudasdk_dct8x8": 
    #if app1 == "cudasdk_dwtHaar1D": 
    #if app1 == "cudasdk_dxtc": 
    #if app1 == "cudasdk_eigenvalues": 
    #if app1 == "cudasdk_fastWalshTransform": 
    #if app1 == "cudasdk_FDTD3d": 
    #if app1 == "cudasdk_interval": 
    #if app1 == "cudasdk_lineOfSight": 
    #if app1 == "cudasdk_matrixMul": 
    #if app1 == "cudasdk_MCEstimatePiInlineP": 
    #if app1 == "cudasdk_MCEstimatePiInlineQ": 
    #if app1 == "cudasdk_MCSingleAsianOptionP": 
    #if app1 == "cudasdk_mergeSort": 
    #if app1 == "cudasdk_quasirandomGenerator": 
    #if app1 == "cudasdk_radixSortThrust": 
    #if app1 == "cudasdk_reduction": 
    #if app1 == "cudasdk_scalarProd": 
    #if app1 == "cudasdk_scan": 
    #if app1 == "cudasdk_segmentationTreeThrust": 
    #if app1 == "cudasdk_shflscan": 
    #if app1 == "cudasdk_simpleCUBLAS": 
    #if app1 == "cudasdk_simpleCUFFTcallback": 
    #if app1 == "cudasdk_SobolQRNG": 
    #if app1 == "cudasdk_sortingNetworks": 
    #if app1 == "cudasdk_stereoDisparity": 
    #if app1 == "cudasdk_threadFenceReduction": 
    #if app1 == "cudasdk_transpose": 
    #if app1 == "cudasdk_vectorAdd": 
    #if app1 == "lonestar_bh": 
    #if app1 == "lonestar_sssp": 
    #if app1 == "lonestar_dmr": 
    #if app1 == "lonestar_mst": 
    #if app1 == "parboil_bfs": 
    #if app1 == "parboil_cutcp": 
    #if app1 == "parboil_lbm": 
    #if app1 == "parboil_mriq":
    #if app1 == "parboil_sgemm":
    #if app1 == "parboil_stencil":
    #if app1 == "poly_2dconv":
    #if app1 == "poly_3mm": 
    #if app1 == "poly_fdtd2d": 
    #if app1 in ["poly_3dconv", "poly_atax", "poly_bicg", "poly_correlation", "poly_covariance", "poly_gemm", "poly_gesummv", "poly_mvt", "poly_syr2k", "poly_syrk"]:

    #if app1 == "shoc_lev1sort": 
    #if app1 == "shoc_lev1reduction": 

    #if app1 in ["rodinia_backprop", "rodinia_b+tree", "rodinia_dwt2d", "rodinia_gaussian", "rodinia_heartwall", "rodinia_hotspot", "rodinia_hybridsort", "rodinia_lavaMD", "rodinia_lud", "rodinia_needle", "rodinia_pathfinder"]:
    #if app1 in ["shoc_lev1BFS","shoc_lev1fft", "shoc_lev1GEMM", "shoc_lev1md5hash", "shoc_lev1reduction", "shoc_lev1sort"]:

    #if app1 == "lonestar_dmr": 
    #if app1 == "cudasdk_MCEstimatePiP": 
    #if app1 == "cudasdk_MCEstimatePiQ": 
    #if app1 == "cudasdk_stereoDisparity": 
        print "\nGenerating script for %s\n" % app1
        for app2, _ in app2dir_dd.iteritems():
            if app2 <> app1:
                a1 = app1
                a1_dir = app2dir_dd[a1]
                a1_dir = "../../" + a1_dir
                print a1_dir
               
                a2 = app2 
                a2_dir = app2dir_dd[a2]
                a2_dir = "../../" + a2_dir
                print a2_dir
                
                #app1 = app1.replace("_", "-")
                a1 = a1.replace("+", "")
                
                #app2 = app2.replace("_", "-")
                a2 = a2.replace("+", "")
                print a1, a2

                gen_run2(current_dir, a1, a1_dir, a2, a2_dir, scriptDir=scriptDir)
                #break
    #break
