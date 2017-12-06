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
# 
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
