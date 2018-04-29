#!/usr/bin/env python
"""Edit gpu workloads and save to a json file"""

import sys
from google.protobuf.internal.encoder import _VarintBytes
sys.path.append('../protobuf')
import GPUApp_pb2

outputFile = 'app_info_v1.bin'

appList = []

#------------------------------------------------------------------------------
# cuda sdk 8.0:  ``$./run.sh devid``
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-matrixMul',
    dir='../apps/devid_cudasdk80/0_Simple/matrixMul',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-vectorAdd',
    dir='../apps/devid_cudasdk80/0_Simple/vectorAdd',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-convolutionFFT2D',
    dir='../apps/devid_cudasdk80/3_Imaging/convolutionFFT2D',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-convolutionSeparable',
    dir='../apps/devid_cudasdk80/3_Imaging/convolutionSeparable',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-convolutionTexture',
    dir='../apps/devid_cudasdk80/3_Imaging/convolutionTexture',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-dct8x8',
    dir='../apps/devid_cudasdk80/3_Imaging/dct8x8',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-dwtHaar1D',
    dir='../apps/devid_cudasdk80/3_Imaging/dwtHaar1D',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-dxtc',
    dir='../apps/devid_cudasdk80/3_Imaging/dxtc',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-histogram',
    dir='../apps/devid_cudasdk80/3_Imaging/histogram',
    cmd='./run.sh'))


appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-HSOpticalFlow',
    dir='../apps/devid_cudasdk80/3_Imaging/HSOpticalFlow',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-stereoDisparity',
    dir='../apps/devid_cudasdk80/3_Imaging/stereoDisparity',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-binomialOptions',
    dir='../apps/devid_cudasdk80/4_Finance/binomialOptions',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-BlackScholes',
    dir='../apps/devid_cudasdk80/4_Finance/BlackScholes',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-quasirandomGenerator',
    dir='../apps/devid_cudasdk80/4_Finance/quasirandomGenerator',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-SobolQRNG',
    dir='../apps/devid_cudasdk80/4_Finance/SobolQRNG',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-c++11_cuda',
    dir='../apps/devid_cudasdk80/6_Advanced/c++11_cuda',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-concurrentKernels',
    dir='../apps/devid_cudasdk80/6_Advanced/concurrentKernels',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-eigenvalues',
    dir='../apps/devid_cudasdk80/6_Advanced/eigenvalues',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-fastWalshTransform',
    dir='../apps/devid_cudasdk80/6_Advanced/fastWalshTransform',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-FDTD3d',
    dir='../apps/devid_cudasdk80/6_Advanced/FDTD3d',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-interval',
    dir='../apps/devid_cudasdk80/6_Advanced/interval',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-lineOfSight',
    dir='../apps/devid_cudasdk80/6_Advanced/lineOfSight',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-mergeSort',
    dir='../apps/devid_cudasdk80/6_Advanced/mergeSort',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-radixSortThrust',
    dir='../apps/devid_cudasdk80/6_Advanced/radixSortThrust',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-reduction',
    dir='../apps/devid_cudasdk80/6_Advanced/reduction',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-scalarProd',
    dir='../apps/devid_cudasdk80/6_Advanced/scalarProd',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-scan',
    dir='../apps/devid_cudasdk80/6_Advanced/scan',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-segmentationTreeThrust',
    dir='../apps/devid_cudasdk80/6_Advanced/segmentationTreeThrust',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-shfl_scan',
    dir='../apps/devid_cudasdk80/6_Advanced/shfl_scan',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-sortingNetworks',
    dir='../apps/devid_cudasdk80/6_Advanced/sortingNetworks',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-threadFenceReduction',
    dir='../apps/devid_cudasdk80/6_Advanced/threadFenceReduction',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-transpose',
    dir='../apps/devid_cudasdk80/6_Advanced/transpose',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-batchCUBLAS',
    dir='../apps/devid_cudasdk80/7_CUDALibraries/batchCUBLAS',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-boxFilterNPP',
    dir='../apps/devid_cudasdk80/7_CUDALibraries/boxFilterNPP',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-MC_EstimatePiInlineP',
    dir='../apps/devid_cudasdk80/7_CUDALibraries/MC_EstimatePiInlineP',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-MC_EstimatePiInlineQ',
    dir='../apps/devid_cudasdk80/7_CUDALibraries/MC_EstimatePiInlineQ',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-MC_EstimatePiP',
    dir='../apps/devid_cudasdk80/7_CUDALibraries/MC_EstimatePiP',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-MC_EstimatePiQ',
    dir='../apps/devid_cudasdk80/7_CUDALibraries/MC_EstimatePiQ',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-MC_SingleAsianOptionP',
    dir='../apps/devid_cudasdk80/7_CUDALibraries/MC_SingleAsianOptionP',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-simpleCUBLAS',
    dir='../apps/devid_cudasdk80/7_CUDALibraries/simpleCUBLAS',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk-simpleCUFFT_callback',
    dir='../apps/devid_cudasdk80/7_CUDALibraries/simpleCUFFT_callback',
    cmd='./run.sh'))

###------------------------------------------------------------------------------
### nupar 
###------------------------------------------------------------------------------
##appList.append(GPUApp_pb2.GPUApp(
##    name='parIIR',
##    dir='../apps/rcuda_nupar/CUDA/IIR',
##    cmd='./parIIR 10240'))

#------------------------------------------------------------------------------
# polybench 
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(
    name='poly-2DCONV',
    dir='../apps/devid_poly/CUDA/2DCONV',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly-3DCONV',
    dir='../apps/devid_poly/CUDA/3DCONV',
    cmd='./run.sh'))

''' appList.append(GPUApp_pb2.GPUApp(
    name='2MM',
    dir='../apps/devid_poly/CUDA/2MM',
    cmd='./2mm.exe')) '''

appList.append(GPUApp_pb2.GPUApp(
    name='poly-3MM',
    dir='../apps/devid_poly/CUDA/3MM',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly-ATAX',
    dir='../apps/devid_poly/CUDA/ATAX',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly-BICG',
    dir='../apps/devid_poly/CUDA/BICG',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly-CORR',
    dir='../apps/devid_poly/CUDA/CORR',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly-COVAR',
    dir='../apps/devid_poly/CUDA/COVAR',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly-FDTD-2D',
    dir='../apps/devid_poly/CUDA/FDTD-2D',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly-GEMM',
    dir='../apps/devid_poly/CUDA/GEMM',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly-GESUMMV',
    dir='../apps/devid_poly/CUDA/GESUMMV',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly-MVT',
    dir='../apps/devid_poly/CUDA/MVT',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly-SYR2K',
    dir='../apps/devid_poly/CUDA/SYR2K',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly-SYRK',
    dir='../apps/devid_poly/CUDA/SYRK',
    cmd='./run.sh'))

#------------------------------------------------------------------------------
# lonestar 
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(
    name='lonestar-bh',
    dir='../apps/devid_lonestar/apps/bh',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='lonestar-dmr',
    dir='../apps/devid_lonestar/apps/dmr',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='lonestar-mst',
    dir='../apps/devid_lonestar/apps/mst',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='lonestar-sssp',
    dir='../apps/devid_lonestar/apps/sssp',
    cmd='./run.sh'))

#------------------------------------------------------------------------------
# parboil 
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(
    name='parboil-bfs',
    dir='../apps/devid_parboil/benchmarks/bfs',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='parboil-cutcp',
    dir='../apps/devid_parboil/benchmarks/cutcp',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='parboil-lbm',
    dir='../apps/devid_parboil/benchmarks/lbm',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='parboil-mri-q',
    dir='../apps/devid_parboil/benchmarks/mri-q',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='parboil-sgemm',
    dir='../apps/devid_parboil/benchmarks/sgemm',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='parboil-stencil',
    dir='../apps/devid_parboil/benchmarks/stencil',
    cmd='./run.sh'))

#------------------------------------------------------------------------------
# rodinia
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(
    name='rodinia-backprop',
    dir='../apps/devid_rodinia/backprop',
    cmd='./run.sh'))

'''appList.append(GPUApp_pb2.GPUApp(
    name='b+tree',
    dir='../apps/devid_rodinia/b+tree',
    cmd='./run.sh')) '''

appList.append(GPUApp_pb2.GPUApp(
    name='rodinia-dwt2d',
    dir='../apps/devid_rodinia/dwt2d',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='rodinia-gaussian',
    dir='../apps/devid_rodinia/gaussian',
    cmd='./run.sh'))

'''appList.append(GPUApp_pb2.GPUApp(
    name='heartwall',
    dir='../apps/devid_rodinia/heartwall',
    cmd='./heartwall ../data/heartwall/test.avi 20')) '''

'''appList.append(GPUApp_pb2.GPUApp(
    name='hotspot',
    dir='../apps/devid_rodinia/hotspot',
    cmd='./hotspot 512 2 2 ../data/hotspot/temp_512 ../data/hotspot/power_512 output.out')) '''

appList.append(GPUApp_pb2.GPUApp(
    name='rodinia-lavaMD',
    dir='../apps/devid_rodinia/lavaMD',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='rodinia-lud',
    dir='../apps/devid_rodinia/lud',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='rodinia-needle',
    dir='../apps/devid_rodinia/nw',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='rodinia-pathfinder',
    dir='../apps/devid_rodinia/pathfinder',
    cmd='./run.sh'))

#------------------------------------------------------------------------------
# shoc 
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(
    name='shoc-bfs',
    dir='../apps/devid_shoc/src/cuda/level1/bfs',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc-fft',
    dir='../apps/devid_shoc/src/cuda/level1/fft',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc-gemm',
    dir='../apps/devid_shoc/src/cuda/level1/gemm',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc-md',
    dir='../apps/devid_shoc/src/cuda/level1/md',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc-md5hash',
    dir='../apps/devid_shoc/src/cuda/level1/md5hash',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc-neuralnet',
    dir='../apps/devid_shoc/src/cuda/level1/neuralnet',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc-reduction',
    dir='../apps/devid_shoc/src/cuda/level1/reduction',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc-scan',
    dir='../apps/devid_shoc/src/cuda/level1/scan',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc-sort',
    dir='../apps/devid_shoc/src/cuda/level1/sort',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc-spmv',
    dir='../apps/devid_shoc/src/cuda/level1/spmv',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc-stencil2d',
    dir='../apps/devid_shoc/src/cuda/level1/stencil2d',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc-triad',
    dir='../apps/devid_shoc/src/cuda/level1/triad',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc-qtclustering',
    dir='../apps/devid_shoc/src/cuda/level2/qtclustering',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc-s3d',
    dir='../apps/devid_shoc/src/cuda/level2/s3d',
    cmd='./run.sh'))

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
