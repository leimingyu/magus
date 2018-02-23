#!/usr/bin/env python
"""Edit gpu workloads and save to a json file"""

import sys
from google.protobuf.internal.encoder import _VarintBytes
sys.path.append('../protobuf')
import GPUApp_pb2

outputFile = 'app_info.bin'

appList = []

#------------------------------------------------------------------------------
# cuda sdk 8.0
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(
    name='matrixMul',
    dir='../apps/rcuda_cusdk80/0_Simple/matrixMul',
    cmd='./matrixMul'))

appList.append(GPUApp_pb2.GPUApp(
    name='vectorAdd',
    dir='../apps/rcuda_cusdk80/0_Simple/vectorAdd',
    cmd='./vectorAdd'))

appList.append(GPUApp_pb2.GPUApp(
    name='convolutionFFT2D',
    dir='../apps/rcuda_cusdk80/3_Imaging/convolutionFFT2D',
    cmd='./convolutionFFT2D'))

appList.append(GPUApp_pb2.GPUApp(
    name='convolutionSeparable',
    dir='../apps/rcuda_cusdk80/3_Imaging/convolutionSeparable',
    cmd='./convolutionSeparable'))

appList.append(GPUApp_pb2.GPUApp(
    name='convolutionTexture',
    dir='../apps/rcuda_cusdk80/3_Imaging/convolutionTexture',
    cmd='./convolutionTexture'))

appList.append(GPUApp_pb2.GPUApp(
    name='dct8x8',
    dir='../apps/rcuda_cusdk80/3_Imaging/dct8x8',
    cmd='./dct8x8'))

appList.append(GPUApp_pb2.GPUApp(
    name='dct8x8',
    dir='../apps/rcuda_cusdk80/3_Imaging/dct8x8',
    cmd='./dct8x8'))

appList.append(GPUApp_pb2.GPUApp(
    name='dwtHaar1D',
    dir='../apps/rcuda_cusdk80/3_Imaging/dwtHaar1D',
    cmd='./dwtHaar1D'))

appList.append(GPUApp_pb2.GPUApp(
    name='dxtc',
    dir='../apps/rcuda_cusdk80/3_Imaging/dxtc',
    cmd='./dxtc'))

appList.append(GPUApp_pb2.GPUApp(
    name='HSOpticalFlow',
    dir='../apps/rcuda_cusdk80/3_Imaging/HSOpticalFlow',
    cmd='./HSOpticalFlow'))

appList.append(GPUApp_pb2.GPUApp(
    name='stereoDisparity',
    dir='../apps/rcuda_cusdk80/3_Imaging/stereoDisparity',
    cmd='./stereoDisparity'))

appList.append(GPUApp_pb2.GPUApp(
    name='binomialOptions',
    dir='../apps/rcuda_cusdk80/4_Finance/binomialOptions',
    cmd='./binomialOptions'))

appList.append(GPUApp_pb2.GPUApp(
    name='BlackScholes',
    dir='../apps/rcuda_cusdk80/4_Finance/BlackScholes',
    cmd='./BlackScholes'))

appList.append(GPUApp_pb2.GPUApp(
    name='quasirandomGenerator',
    dir='../apps/rcuda_cusdk80/4_Finance/quasirandomGenerator',
    cmd='./quasirandomGenerator'))

appList.append(GPUApp_pb2.GPUApp(
    name='SobolQRNG',
    dir='../apps/rcuda_cusdk80/4_Finance/SobolQRNG',
    cmd='./SobolQRNG'))

appList.append(GPUApp_pb2.GPUApp(
    name='c++11_cuda',
    dir='../apps/rcuda_cusdk80/6_Advanced/c++11_cuda',
    cmd='./c++11_cuda'))

appList.append(GPUApp_pb2.GPUApp(
    name='concurrentKernels',
    dir='../apps/rcuda_cusdk80/6_Advanced/concurrentKernels',
    cmd='./concurrentKernels'))

appList.append(GPUApp_pb2.GPUApp(
    name='eigenvalues',
    dir='../apps/rcuda_cusdk80/6_Advanced/eigenvalues',
    cmd='./eigenvalues'))

appList.append(GPUApp_pb2.GPUApp(
    name='fastWalshTransform',
    dir='../apps/rcuda_cusdk80/6_Advanced/fastWalshTransform',
    cmd='./fastWalshTransform'))

appList.append(GPUApp_pb2.GPUApp(
    name='FDTD3d',
    dir='../apps/rcuda_cusdk80/6_Advanced/FDTD3d',
    cmd='./FDTD3d'))

appList.append(GPUApp_pb2.GPUApp(
    name='interval',
    dir='../apps/rcuda_cusdk80/6_Advanced/interval',
    cmd='./interval'))

appList.append(GPUApp_pb2.GPUApp(
    name='mergeSort',
    dir='../apps/rcuda_cusdk80/6_Advanced/mergeSort',
    cmd='./mergeSort'))

appList.append(GPUApp_pb2.GPUApp(
    name='radixSortThrust',
    dir='../apps/rcuda_cusdk80/6_Advanced/radixSortThrust',
    cmd='./radixSortThrust'))

appList.append(GPUApp_pb2.GPUApp(
    name='reduction',
    dir='../apps/rcuda_cusdk80/6_Advanced/reduction',
    cmd='./reduction'))

appList.append(GPUApp_pb2.GPUApp(
    name='scalarProd',
    dir='../apps/rcuda_cusdk80/6_Advanced/scalarProd',
    cmd='./scalarProd'))

appList.append(GPUApp_pb2.GPUApp(
    name='scan',
    dir='../apps/rcuda_cusdk80/6_Advanced/scan',
    cmd='./scan'))

appList.append(GPUApp_pb2.GPUApp(
    name='shfl_scan',
    dir='../apps/rcuda_cusdk80/6_Advanced/shfl_scan',
    cmd='./shfl_scan'))

appList.append(GPUApp_pb2.GPUApp(
    name='sortingNetworks',
    dir='../apps/rcuda_cusdk80/6_Advanced/sortingNetworks',
    cmd='./sortingNetworks'))

appList.append(GPUApp_pb2.GPUApp(
    name='threadFenceReduction',
    dir='../apps/rcuda_cusdk80/6_Advanced/threadFenceReduction',
    cmd='./threadFenceReduction'))

appList.append(GPUApp_pb2.GPUApp(
    name='transpose',
    dir='../apps/rcuda_cusdk80/6_Advanced/transpose',
    cmd='./transpose'))

appList.append(GPUApp_pb2.GPUApp(
    name='batchCUBLAS',
    dir='../apps/rcuda_cusdk80/7_CUDALibraries/batchCUBLAS',
    cmd='./batchCUBLAS'))

appList.append(GPUApp_pb2.GPUApp(
    name='MC_EstimatePiInlineP',
    dir='../apps/rcuda_cusdk80/7_CUDALibraries/MC_EstimatePiInlineP',
    cmd='./MC_EstimatePiInlineP'))

appList.append(GPUApp_pb2.GPUApp(
    name='MC_EstimatePiInlineQ',
    dir='../apps/rcuda_cusdk80/7_CUDALibraries/MC_EstimatePiInlineQ',
    cmd='./MC_EstimatePiInlineQ'))

appList.append(GPUApp_pb2.GPUApp(
    name='MC_EstimatePiP',
    dir='../apps/rcuda_cusdk80/7_CUDALibraries/MC_EstimatePiP',
    cmd='./MC_EstimatePiP'))

appList.append(GPUApp_pb2.GPUApp(
    name='MC_EstimatePiQ',
    dir='../apps/rcuda_cusdk80/7_CUDALibraries/MC_EstimatePiQ',
    cmd='./MC_EstimatePiQ'))

appList.append(GPUApp_pb2.GPUApp(
    name='MC_SingleAsianOptionP',
    dir='../apps/rcuda_cusdk80/7_CUDALibraries/MC_SingleAsianOptionP',
    cmd='./MC_SingleAsianOptionP'))

appList.append(GPUApp_pb2.GPUApp(
    name='simpleCUBLAS',
    dir='../apps/rcuda_cusdk80/7_CUDALibraries/simpleCUBLAS',
    cmd='./simpleCUBLAS'))

#------------------------------------------------------------------------------
# nupar 
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(
    name='parIIR',
    dir='../apps/rcuda_nupar/CUDA/IIR',
    cmd='./parIIR 10240'))

#------------------------------------------------------------------------------
# polybench 
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(
    name='2DCONV',
    dir='../apps/rcuda_poly/CUDA/2DCONV',
    cmd='./2DConvolution.exe'))

appList.append(GPUApp_pb2.GPUApp(
    name='3DCONV',
    dir='../apps/rcuda_poly/CUDA/3DCONV',
    cmd='./3DConvolution.exe'))

''' appList.append(GPUApp_pb2.GPUApp(
    name='2MM',
    dir='../apps/rcuda_poly/CUDA/2MM',
    cmd='./2mm.exe')) '''

appList.append(GPUApp_pb2.GPUApp(
    name='3MM',
    dir='../apps/rcuda_poly/CUDA/3MM',
    cmd='./3mm.exe'))

appList.append(GPUApp_pb2.GPUApp(
    name='ATAX',
    dir='../apps/rcuda_poly/CUDA/ATAX',
    cmd='./atax.exe'))

appList.append(GPUApp_pb2.GPUApp(
    name='BICG',
    dir='../apps/rcuda_poly/CUDA/BICG',
    cmd='./bicg.exe'))

appList.append(GPUApp_pb2.GPUApp(
    name='CORR',
    dir='../apps/rcuda_poly/CUDA/CORR',
    cmd='./correlation.exe'))

appList.append(GPUApp_pb2.GPUApp(
    name='COVAR',
    dir='../apps/rcuda_poly/CUDA/COVAR',
    cmd='./covariance.exe'))

appList.append(GPUApp_pb2.GPUApp(
    name='FDTD-2D',
    dir='../apps/rcuda_poly/CUDA/FDTD-2D',
    cmd='./fdtd2d.exe'))

appList.append(GPUApp_pb2.GPUApp(
    name='GEMM',
    dir='../apps/rcuda_poly/CUDA/GEMM',
    cmd='./gemm.exe'))

appList.append(GPUApp_pb2.GPUApp(
    name='GESUMMV',
    dir='../apps/rcuda_poly/CUDA/GESUMMV',
    cmd='./gesummv.exe'))

appList.append(GPUApp_pb2.GPUApp(
    name='MVT',
    dir='../apps/rcuda_poly/CUDA/MVT',
    cmd='./mvt.exe'))

appList.append(GPUApp_pb2.GPUApp(
    name='SYR2K',
    dir='../apps/rcuda_poly/CUDA/SYR2K',
    cmd='./syr2k.exe'))

appList.append(GPUApp_pb2.GPUApp(
    name='SYRK',
    dir='../apps/rcuda_poly/CUDA/SYRK',
    cmd='./syrk.exe'))

#------------------------------------------------------------------------------
# lonestar 
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(
    name='bh',
    dir='../apps/rcuda_lonestar/apps/bh',
    cmd='./bh 30000 50 0'))

appList.append(GPUApp_pb2.GPUApp(
    name='dmr',
    dir='../apps/rcuda_lonestar/apps/dmr',
    cmd='./dmr  ../../inputs/250k.2 20'))

appList.append(GPUApp_pb2.GPUApp(
    name='mst',
    dir='../apps/rcuda_lonestar/apps/mst',
    cmd='./mst ../../inputs/LSGINPUTS/rmat12.sym.gr'))

appList.append(GPUApp_pb2.GPUApp(
    name='sssp',
    dir='../apps/rcuda_lonestar/apps/sssp',
    cmd='./sssp ../../inputs/USA-road-d.FLA.gr'))

#------------------------------------------------------------------------------
# parboil 
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(
    name='bfs',
    dir='../apps/rcuda_parboil/benchmarks/bfs',
    cmd='./bfs -i ../../datasets/bfs/NY/input/graph_input.dat  -o out.dat'))

appList.append(GPUApp_pb2.GPUApp(
    name='cutcp',
    dir='../apps/rcuda_parboil/benchmarks/cutcp',
    cmd='./cutcp -i ../../datasets/cutcp/small/input/watbox.sl40.pqr  -o out_small'))

appList.append(GPUApp_pb2.GPUApp(
    name='lbm',
    dir='../apps/rcuda_parboil/benchmarks/lbm',
    cmd='./lbm 1 -i ../../datasets/lbm/short/input/120_120_150_ldc.of  -o out'))

appList.append(GPUApp_pb2.GPUApp(
    name='mri-q',
    dir='../apps/rcuda_parboil/benchmarks/mri-q',
    cmd='./mri-q -i ../../datasets/mri-q/small/input/32_32_32_dataset.bin'))

appList.append(GPUApp_pb2.GPUApp(
    name='sgemm',
    dir='../apps/rcuda_parboil/benchmarks/sgemm',
    cmd='./sgemm  -i ../../datasets/sgemm/small/input/matrix1.txt,../../datasets/sgemm/small/input/matrix2.txt,../../datasets/sgemm/small/input/matrix2t.txt'))

appList.append(GPUApp_pb2.GPUApp(
    name='stencil',
    dir='../apps/rcuda_parboil/benchmarks/stencil',
    cmd='./stencil -i ../../datasets/stencil/small/input/128x128x32.bin 128 128 32 1001'))

#------------------------------------------------------------------------------
# rodinia
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(
    name='backprop',
    dir='../apps/rcuda_rodinia/backprop',
    cmd='./backprop 65536'))

appList.append(GPUApp_pb2.GPUApp(
    name='b+tree',
    dir='../apps/rcuda_rodinia/b+tree',
    cmd='./b+tree.out file ../data/b+tree/mil.txt command ../data/b+tree/command.txt'))

appList.append(GPUApp_pb2.GPUApp(
    name='dwt2d',
    dir='../apps/rcuda_rodinia/dwt2d',
    cmd='./dwt2d rgb.bmp -d 1024x1024 -f -5 -l 3'))


appList.append(GPUApp_pb2.GPUApp(
    name='gaussian',
    dir='../apps/rcuda_rodinia/gaussian',
    cmd='./gaussian -s 16'))

appList.append(GPUApp_pb2.GPUApp(
    name='heartwall',
    dir='../apps/rcuda_rodinia/heartwall',
    cmd='./heartwall ../data/heartwall/test.avi 20'))


appList.append(GPUApp_pb2.GPUApp(
    name='hotspot',
    dir='../apps/rcuda_rodinia/hotspot',
    cmd='./hotspot 512 2 2 ../data/hotspot/temp_512 ../data/hotspot/power_512 output.out'))

appList.append(GPUApp_pb2.GPUApp(
    name='lavaMD',
    dir='../apps/rcuda_rodinia/lavaMD',
    cmd='./lavaMD -boxes1d 10'))


appList.append(GPUApp_pb2.GPUApp(
    name='lud',
    dir='../apps/rcuda_rodinia/lud',
    cmd='cuda/lud_cuda -s 256 -v'))

appList.append(GPUApp_pb2.GPUApp(
    name='needle',
    dir='../apps/rcuda_rodinia/nw',
    cmd='./needle 2048 10'))


appList.append(GPUApp_pb2.GPUApp(
    name='pathfinder',
    dir='../apps/rcuda_rodinia/pathfinder',
    cmd='./pathfinder 100000 100 20'))

#------------------------------------------------------------------------------
# others 
#------------------------------------------------------------------------------

''' appList.append(GPUApp_pb2.GPUApp(
    name='',
    dir='../apps/rcuda_others/',
    cmd='')) '''



with open(outputFile, 'wb') as f:
    for curApp in appList:
        size = curApp.ByteSize()
        f.write(_VarintBytes(size))
        f.write(curApp.SerializeToString())



#
#
#print "1st"
##print read_app_list[0]
#curApp = read_app_list[0]
#print curApp.dir
#print curApp.cmd
#
#print "2nd"
#print read_app_list[1]
