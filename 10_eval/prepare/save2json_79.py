#!/usr/bin/env python
"""Edit gpu workloads and save to a json file"""

import sys
from google.protobuf.internal.encoder import _VarintBytes
sys.path.append('../protobuf')
import GPUApp_pb2

outputFile = 'app_info_79.bin'

appList = []

#------------------------------------------------------------------------------
# cuda sdk 8.0:  ``$./run.sh devid``
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_matrixMul',
    dir='../apps/devid_cudasdk80/0_Simple/matrixMul',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_vectorAdd',
    dir='../apps/devid_cudasdk80/0_Simple/vectorAdd',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_convolutionFFT2D',
    dir='../apps/devid_cudasdk80/3_Imaging/convolutionFFT2D',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_convolutionSeparable',
    dir='../apps/devid_cudasdk80/3_Imaging/convolutionSeparable',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_convolutionTexture',
    dir='../apps/devid_cudasdk80/3_Imaging/convolutionTexture',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_dct8x8',
    dir='../apps/devid_cudasdk80/3_Imaging/dct8x8',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_dwtHaar1D',
    dir='../apps/devid_cudasdk80/3_Imaging/dwtHaar1D',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_dxtc',
    dir='../apps/devid_cudasdk80/3_Imaging/dxtc',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_stereoDisparity',
    dir='../apps/devid_cudasdk80/3_Imaging/stereoDisparity',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_binomialOptions',
    dir='../apps/devid_cudasdk80/4_Finance/binomialOptions',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_BlackScholes',
    dir='../apps/devid_cudasdk80/4_Finance/BlackScholes',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_quasirandomGenerator',
    dir='../apps/devid_cudasdk80/4_Finance/quasirandomGenerator',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_SobolQRNG',
    dir='../apps/devid_cudasdk80/4_Finance/SobolQRNG',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_c++11Cuda',
    dir='../apps/devid_cudasdk80/6_Advanced/c++11_cuda',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_concurrentKernels',
    dir='../apps/devid_cudasdk80/6_Advanced/concurrentKernels',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_eigenvalues',
    dir='../apps/devid_cudasdk80/6_Advanced/eigenvalues',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_fastWalshTransform',
    dir='../apps/devid_cudasdk80/6_Advanced/fastWalshTransform',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_FDTD3d',
    dir='../apps/devid_cudasdk80/6_Advanced/FDTD3d',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_interval',
    dir='../apps/devid_cudasdk80/6_Advanced/interval',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_lineOfSight',
    dir='../apps/devid_cudasdk80/6_Advanced/lineOfSight',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_mergeSort',
    dir='../apps/devid_cudasdk80/6_Advanced/mergeSort',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_radixSortThrust',
    dir='../apps/devid_cudasdk80/6_Advanced/radixSortThrust',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_reduction',
    dir='../apps/devid_cudasdk80/6_Advanced/reduction',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_scalarProd',
    dir='../apps/devid_cudasdk80/6_Advanced/scalarProd',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_scan',
    dir='../apps/devid_cudasdk80/6_Advanced/scan',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_segmentationTreeThrust',
    dir='../apps/devid_cudasdk80/6_Advanced/segmentationTreeThrust',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_shflscan',
    dir='../apps/devid_cudasdk80/6_Advanced/shfl_scan',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_sortingNetworks',
    dir='../apps/devid_cudasdk80/6_Advanced/sortingNetworks',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_threadFenceReduction',
    dir='../apps/devid_cudasdk80/6_Advanced/threadFenceReduction',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_transpose',
    dir='../apps/devid_cudasdk80/6_Advanced/transpose',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_batchCUBLAS',
    dir='../apps/devid_cudasdk80/7_CUDALibraries/batchCUBLAS',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_boxFilterNPP',
    dir='../apps/devid_cudasdk80/7_CUDALibraries/boxFilterNPP',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_MCEstimatePiInlineP',
    dir='../apps/devid_cudasdk80/7_CUDALibraries/MC_EstimatePiInlineP',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_MCEstimatePiInlineQ',
    dir='../apps/devid_cudasdk80/7_CUDALibraries/MC_EstimatePiInlineQ',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_MCEstimatePiP',
    dir='../apps/devid_cudasdk80/7_CUDALibraries/MC_EstimatePiP',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_MCEstimatePiQ',
    dir='../apps/devid_cudasdk80/7_CUDALibraries/MC_EstimatePiQ',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_MCSingleAsianOptionP',
    dir='../apps/devid_cudasdk80/7_CUDALibraries/MC_SingleAsianOptionP',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_simpleCUBLAS',
    dir='../apps/devid_cudasdk80/7_CUDALibraries/simpleCUBLAS',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='cudasdk_simpleCUFFTcallback',
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
    name='poly_2dconv',
    dir='../apps/devid_poly/CUDA/2DCONV',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly_3dconv',
    dir='../apps/devid_poly/CUDA/3DCONV',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly_3mm',
    dir='../apps/devid_poly/CUDA/3MM',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly_atax',
    dir='../apps/devid_poly/CUDA/ATAX',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly_bicg',
    dir='../apps/devid_poly/CUDA/BICG',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly_correlation',
    dir='../apps/devid_poly/CUDA/CORR',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly_covariance',
    dir='../apps/devid_poly/CUDA/COVAR',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly_fdtd2d',
    dir='../apps/devid_poly/CUDA/FDTD-2D',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly_gemm',
    dir='../apps/devid_poly/CUDA/GEMM',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly_gesummv',
    dir='../apps/devid_poly/CUDA/GESUMMV',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly_mvt',
    dir='../apps/devid_poly/CUDA/MVT',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly_syr2k',
    dir='../apps/devid_poly/CUDA/SYR2K',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='poly_syrk',
    dir='../apps/devid_poly/CUDA/SYRK',
    cmd='./run.sh'))


#------------------------------------------------------------------------------
# lonestar 
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(
    name='lonestar_bh',
    dir='../apps/devid_lonestar/apps/bh',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='lonestar_dmr',
    dir='../apps/devid_lonestar/apps/dmr',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='lonestar_mst',
    dir='../apps/devid_lonestar/apps/mst',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='lonestar_sssp',
    dir='../apps/devid_lonestar/apps/sssp',
    cmd='./run.sh'))

#------------------------------------------------------------------------------
# parboil 
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(
    name='parboil_bfs',
    dir='../apps/devid_parboil/benchmarks/bfs',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='parboil_cutcp',
    dir='../apps/devid_parboil/benchmarks/cutcp',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='parboil_lbm',
    dir='../apps/devid_parboil/benchmarks/lbm',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='parboil_mriq',
    dir='../apps/devid_parboil/benchmarks/mri-q',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='parboil_sgemm',
    dir='../apps/devid_parboil/benchmarks/sgemm',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='parboil_stencil',
    dir='../apps/devid_parboil/benchmarks/stencil',
    cmd='./run.sh'))

#------------------------------------------------------------------------------
# rodinia
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(
    name='rodinia_backprop',
    dir='../apps/devid_rodinia/backprop',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='rodinia_b+tree',
    dir='../apps/devid_rodinia/b+tree',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='rodinia_dwt2d',
    dir='../apps/devid_rodinia/dwt2d',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='rodinia_gaussian',
    dir='../apps/devid_rodinia/gaussian',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='rodinia_heartwall',
    dir='../apps/devid_rodinia/heartwall',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='rodinia_hybridsort',
    dir='../apps/devid_rodinia/hybridsort',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='rodinia_hotspot',
    dir='../apps/devid_rodinia/hotspot',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='rodinia_lud',
    dir='../apps/devid_rodinia/lud',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='rodinia_lavaMD',
    dir='../apps/devid_rodinia/lavaMD',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='rodinia_needle',
    dir='../apps/devid_rodinia/nw',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='rodinia_pathfinder',
    dir='../apps/devid_rodinia/pathfinder',
    cmd='./run.sh'))

#------------------------------------------------------------------------------
# shoc 
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(
    name='shoc_lev1BFS',
    dir='../apps/devid_shoc/src/cuda/level1/bfs',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc_lev1sort',
    dir='../apps/devid_shoc/src/cuda/level1/sort',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc_lev1fft',
    dir='../apps/devid_shoc/src/cuda/level1/fft',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc_lev1GEMM',
    dir='../apps/devid_shoc/src/cuda/level1/gemm',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc_lev1md5hash',
    dir='../apps/devid_shoc/src/cuda/level1/md5hash',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc_lev1reduction',
    dir='../apps/devid_shoc/src/cuda/level1/reduction',
    cmd='./run.sh'))


#------------------------------------------------------------------------------
# others 
#------------------------------------------------------------------------------



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
