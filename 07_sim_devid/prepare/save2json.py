#!/usr/bin/env python
"""Edit gpu workloads and save to a json file"""

import sys
from google.protobuf.internal.encoder import _VarintBytes
sys.path.append('../protobuf')
import GPUApp_pb2

outputFile = 'app_info.bin'

appList = []

#------------------------------------------------------------------------------
# cuda sdk 8.0:  ``$./run.sh devid``
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_matrixMul', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_vectorAdd', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_convolutionFFT2D', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_convolutionSeparable', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_convolutionTexture', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_dct8x8', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_dwtHaar1D', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_dxtc', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_stereoDisparity', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_binomialOptions', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_BlackScholes', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_quasirandomGenerator', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_SobolQRNG', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_c++11Cuda', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_concurrentKernels', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_eigenvalues', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_fastWalshTransform', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_FDTD3d', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_interval', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_lineOfSight', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_mergeSort', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_radixSortThrust', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_reduction', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_scalarProd', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_scan', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_segmentationTreeThrust', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_shflscan', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_sortingNetworks', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_threadFenceReduction', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_transpose', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_batchCUBLAS', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_boxFilterNPP', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_MCEstimatePiInlineP', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_MCEstimatePiInlineQ', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_MCEstimatePiP', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_MCEstimatePiQ', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_MCSingleAsianOptionP', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_simpleCUBLAS', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='cudasdk_simpleCUFFTcallback', dir='',cmd=''))


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
appList.append(GPUApp_pb2.GPUApp(name='poly_2dconv', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='poly_3dconv', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='poly_3mm', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='poly_atax', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='poly_bicg', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='poly_correlation', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='poly_covariance', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='poly_fdtd2d', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='poly_gemm', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='poly_gesummv', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='poly_mvt', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='poly_syr2k', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='poly_syrk', dir='',cmd=''))


#------------------------------------------------------------------------------
# lonestar 
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(name='lonestar_bh', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='lonestar_dmr', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='lonestar_mst', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='lonestar_sssp', dir='',cmd=''))

#------------------------------------------------------------------------------
# parboil 
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(name='parboil_bfs', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='parboil_cutcp', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='parboil_lbm', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='parboil_mriq', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='parboil_sgemm', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='parboil_stencil', dir='',cmd=''))


#------------------------------------------------------------------------------
# rodinia
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(name='rodinia_backprop', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='rodinia_b+tree', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='rodinia_dwt2d', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='rodinia_gaussian', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='rodinia_heartwall', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='rodinia_hybridsort', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='rodinia_hotspot', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='rodinia_lud', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='rodinia_lavaMD', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='rodinia_needle', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='rodinia_pathfinder', dir='',cmd=''))


#------------------------------------------------------------------------------
# shoc 
#------------------------------------------------------------------------------
appList.append(GPUApp_pb2.GPUApp(name='shoc_lev1BFS', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='shoc_lev1sort', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='shoc_lev1fft', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='shoc_lev1GEMM', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='shoc_lev1md5hash', dir='',cmd=''))
appList.append(GPUApp_pb2.GPUApp(name='shoc_lev1reduction', dir='',cmd=''))


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
