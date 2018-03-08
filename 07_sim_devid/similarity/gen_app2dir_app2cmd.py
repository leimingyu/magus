#!/usr/bin/env python
"""Indexing app dir and cmd in data dict."""

import os
import sys
import pandas as pd
import numpy as np


app2dir_dd = {}
app2cmd_dd = {}

#------------------------------------------------------------------------------
# cuda sdk 8.0:  ``$./run.sh devid``
#------------------------------------------------------------------------------

app2dir_dd['cudasdk_matrixMul'] = '../apps/devid_cudasdk80/0_Simple/matrixMul'
app2cmd_dd['cudasdk_matrixMul'] = './run.sh'

app2dir_dd['cudasdk_vectorAdd'] = '../apps/devid_cudasdk80/0_Simple/vectorAdd'
app2cmd_dd['cudasdk_vectorAdd'] = './run.sh'

app2dir_dd['cudasdk_convolutionFFT2D'] = '../apps/devid_cudasdk80/3_Imaging/convolutionFFT2D'
app2cmd_dd['cudasdk_convolutionFFT2D'] = './run.sh'

app2dir_dd['cudasdk_convolutionSeparable'] = '../apps/devid_cudasdk80/3_Imaging/convolutionSeparable'
app2cmd_dd['cudasdk_convolutionSeparable'] = './run.sh'

app2dir_dd['cudasdk_convolutionTexture'] = '../apps/devid_cudasdk80/3_Imaging/convolutionTexture'
app2cmd_dd['cudasdk_convolutionTexture'] = './run.sh'

app2dir_dd['cudasdk_dct8x8'] = '../apps/devid_cudasdk80/3_Imaging/dct8x8'
app2cmd_dd['cudasdk_dct8x8'] = './run.sh'

app2dir_dd['cudasdk_dwtHaar1D'] = '../apps/devid_cudasdk80/3_Imaging/dwtHaar1D'
app2cmd_dd['cudasdk_dwtHaar1D'] = './run.sh'

app2dir_dd['cudasdk_dxtc'] = '../apps/devid_cudasdk80/3_Imaging/dxtc'
app2cmd_dd['cudasdk_dxtc'] = './run.sh'

app2dir_dd['cudasdk_stereoDisparity'] = '../apps/devid_cudasdk80/3_Imaging/stereoDisparity'
app2cmd_dd['cudasdk_stereoDisparity'] = './run.sh'

app2dir_dd['cudasdk_binomialOptions'] = '../apps/devid_cudasdk80/4_Finance/binomialOptions'
app2cmd_dd['cudasdk_binomialOptions'] = './run.sh'

app2dir_dd['cudasdk_BlackScholes'] = '../apps/devid_cudasdk80/4_Finance/BlackScholes'
app2cmd_dd['cudasdk_BlackScholes'] = './run.sh'

app2dir_dd['cudasdk_quasirandomGenerator'] = '../apps/devid_cudasdk80/4_Finance/quasirandomGenerator'
app2cmd_dd['cudasdk_quasirandomGenerator'] = './run.sh'

app2dir_dd['cudasdk_SobolQRNG'] = '../apps/devid_cudasdk80/4_Finance/SobolQRNG'
app2cmd_dd['cudasdk_SobolQRNG'] = './run.sh'

app2dir_dd['cudasdk_c++11Cuda'] = '../apps/devid_cudasdk80/6_Advanced/c++11_cuda'
app2cmd_dd['cudasdk_c++11Cuda'] = './run.sh'

app2dir_dd['cudasdk_concurrentKernels'] = '../apps/devid_cudasdk80/6_Advanced/concurrentKernels'
app2cmd_dd['cudasdk_concurrentKernels'] = './run.sh'

app2dir_dd['cudasdk_eigenvalues'] = '../apps/devid_cudasdk80/6_Advanced/eigenvalues'
app2cmd_dd['cudasdk_eigenvalues'] = './run.sh'

app2dir_dd['cudasdk_fastWalshTransform'] = '../apps/devid_cudasdk80/6_Advanced/fastWalshTransform'
app2cmd_dd['cudasdk_fastWalshTransform'] = './run.sh'

app2dir_dd['cudasdk_FDTD3d'] = '../apps/devid_cudasdk80/6_Advanced/FDTD3d'
app2cmd_dd['cudasdk_FDTD3d'] = './run.sh'

app2dir_dd['cudasdk_interval'] = '../apps/devid_cudasdk80/6_Advanced/interval'
app2cmd_dd['cudasdk_interval'] = './run.sh'

app2dir_dd['cudasdk_lineOfSight'] = '../apps/devid_cudasdk80/6_Advanced/lineOfSight'
app2cmd_dd['cudasdk_lineOfSight'] = './run.sh'

app2dir_dd['cudasdk_mergeSort'] = '../apps/devid_cudasdk80/6_Advanced/mergeSort'
app2cmd_dd['cudasdk_mergeSort'] = './run.sh'

app2dir_dd['cudasdk_radixSortThrust'] = '../apps/devid_cudasdk80/6_Advanced/radixSortThrust'
app2cmd_dd['cudasdk_radixSortThrust'] = './run.sh'

app2dir_dd['cudasdk_reduction'] = '../apps/devid_cudasdk80/6_Advanced/reduction'
app2cmd_dd['cudasdk_reduction'] = './run.sh'

app2dir_dd['cudasdk_scalarProd'] = '../apps/devid_cudasdk80/6_Advanced/scalarProd'
app2cmd_dd['cudasdk_scalarProd'] = './run.sh'

app2dir_dd['cudasdk_scan'] = '../apps/devid_cudasdk80/6_Advanced/scan'
app2cmd_dd['cudasdk_scan'] = './run.sh'

app2dir_dd['cudasdk_segmentationTreeThrust'] = '../apps/devid_cudasdk80/6_Advanced/segmentationTreeThrust'
app2cmd_dd['cudasdk_segmentationTreeThrust'] = './run.sh'

app2dir_dd['cudasdk_shflscan'] = '../apps/devid_cudasdk80/6_Advanced/shfl_scan'
app2cmd_dd['cudasdk_shflscan'] = './run.sh'

app2dir_dd['cudasdk_sortingNetworks'] = '../apps/devid_cudasdk80/6_Advanced/sortingNetworks'
app2cmd_dd['cudasdk_sortingNetworks'] = './run.sh'

app2dir_dd['cudasdk_threadFenceReduction'] = '../apps/devid_cudasdk80/6_Advanced/threadFenceReduction'
app2cmd_dd['cudasdk_threadFenceReduction'] = './run.sh'

app2dir_dd['cudasdk_transpose'] = '../apps/devid_cudasdk80/6_Advanced/transpose'
app2cmd_dd['cudasdk_transpose'] = './run.sh'

app2dir_dd['cudasdk_batchCUBLAS'] = '../apps/devid_cudasdk80/7_CUDALibraries/batchCUBLAS'
app2cmd_dd['cudasdk_batchCUBLAS'] = './run.sh'

app2dir_dd['cudasdk_boxFilterNPP'] = '../apps/devid_cudasdk80/7_CUDALibraries/boxFilterNPP'
app2cmd_dd['cudasdk_boxFilterNPP'] = './run.sh'

app2dir_dd['cudasdk_MCEstimatePiInlineP'] = '../apps/devid_cudasdk80/7_CUDALibraries/MC_EstimatePiInlineP'
app2cmd_dd['cudasdk_MCEstimatePiInlineP'] = './run.sh'

app2dir_dd['cudasdk_MCEstimatePiInlineQ'] = '../apps/devid_cudasdk80/7_CUDALibraries/MC_EstimatePiInlineQ'
app2cmd_dd['cudasdk_MCEstimatePiInlineQ'] = './run.sh'

app2dir_dd['cudasdk_MCEstimatePiP'] = '../apps/devid_cudasdk80/7_CUDALibraries/MC_EstimatePiP'
app2cmd_dd['cudasdk_MCEstimatePiP'] = './run.sh'

app2dir_dd['cudasdk_MCEstimatePiQ'] = '../apps/devid_cudasdk80/7_CUDALibraries/MC_EstimatePiQ'
app2cmd_dd['cudasdk_MCEstimatePiQ'] = './run.sh'

app2dir_dd['cudasdk_MCSingleAsianOptionP'] = '../apps/devid_cudasdk80/7_CUDALibraries/MC_SingleAsianOptionP'
app2cmd_dd['cudasdk_MCSingleAsianOptionP'] = './run.sh'

app2dir_dd['cudasdk_simpleCUBLAS'] = '../apps/devid_cudasdk80/7_CUDALibraries/simpleCUBLAS'
app2cmd_dd['cudasdk_simpleCUBLAS'] = './run.sh'

app2dir_dd['cudasdk_simpleCUFFTcallback'] = '../apps/devid_cudasdk80/7_CUDALibraries/simpleCUFFT_callback'
app2cmd_dd['cudasdk_simpleCUFFTcallback'] = './run.sh'


# ------------------------------------------------------------------------------
# nupar
# ------------------------------------------------------------------------------
# appList.append(GPUApp_pb2.GPUApp(
# name='parIIR',
# dir='../apps/rcuda_nupar/CUDA/IIR',
# cmd='./parIIR 10240'))

#------------------------------------------------------------------------------
# polybench
#------------------------------------------------------------------------------
app2dir_dd['poly_2dconv'] = '../apps/devid_poly/CUDA/2DCONV'
app2cmd_dd['poly_2dconv'] = './run.sh'

app2dir_dd['poly_3dconv'] = '../apps/devid_poly/CUDA/3DCONV'
app2cmd_dd['poly_3dconv'] = './run.sh'

app2dir_dd['poly_3mm'] = '../apps/devid_poly/CUDA/3MM'
app2cmd_dd['poly_3mm'] = './run.sh'

app2dir_dd['poly_atax'] = '../apps/devid_poly/CUDA/ATAX'
app2cmd_dd['poly_atax'] = './run.sh'

app2dir_dd['poly_bicg'] = '../apps/devid_poly/CUDA/BICG'
app2cmd_dd['poly_bicg'] = './run.sh'

app2dir_dd['poly_correlation'] = '../apps/devid_poly/CUDA/CORR'
app2cmd_dd['poly_correlation'] = './run.sh'

app2dir_dd['poly_covariance'] = '../apps/devid_poly/CUDA/COVAR'
app2cmd_dd['poly_covariance'] = './run.sh'

app2dir_dd['poly_fdtd2d'] = '../apps/devid_poly/CUDA/FDTD-2D'
app2cmd_dd['poly_fdtd2d'] = './run.sh'

app2dir_dd['poly_gemm'] = '../apps/devid_poly/CUDA/GEMM'
app2cmd_dd['poly_gemm'] = './run.sh'

app2dir_dd['poly_gesummv'] = '../apps/devid_poly/CUDA/GESUMMV'
app2cmd_dd['poly_gesummv'] = './run.sh'

app2dir_dd['poly_mvt'] = '../apps/devid_poly/CUDA/MVT'
app2cmd_dd['poly_mvt'] = './run.sh'

app2dir_dd['poly_syr2k'] = '../apps/devid_poly/CUDA/SYR2K'
app2cmd_dd['poly_syr2k'] = './run.sh'

app2dir_dd['poly_syrk'] = '../apps/devid_poly/CUDA/SYRK'
app2cmd_dd['poly_syrk'] = './run.sh'


#------------------------------------------------------------------------------
# lonestar
#------------------------------------------------------------------------------
app2dir_dd['lonestar_bh'] = '../apps/devid_lonestar/apps/bh'
app2cmd_dd['lonestar_bh'] = './run.sh'

app2dir_dd['lonestar_dmr'] = '../apps/devid_lonestar/apps/dmr'
app2cmd_dd['lonestar_dmr'] = './run.sh'

app2dir_dd['lonestar_mst'] = '../apps/devid_lonestar/apps/mst'
app2cmd_dd['lonestar_mst'] = './run.sh'

app2dir_dd['lonestar_sssp'] = '../apps/devid_lonestar/apps/sssp'
app2cmd_dd['lonestar_sssp'] = './run.sh'


#------------------------------------------------------------------------------
# parboil
#------------------------------------------------------------------------------
app2dir_dd['parboil_bfs'] = '../apps/devid_parboil/benchmarks/bfs'
app2cmd_dd['parboil_bfs'] = './run.sh'

app2dir_dd['parboil_cutcp'] = '../apps/devid_parboil/benchmarks/cutcp'
app2cmd_dd['parboil_cutcp'] = './run.sh'

app2dir_dd['parboil_lbm'] = '../apps/devid_parboil/benchmarks/lbm'
app2cmd_dd['parboil_lbm'] = './run.sh'

app2dir_dd['parboil_mriq'] = '../apps/devid_parboil/benchmarks/mri-q'
app2cmd_dd['parboil_mriq'] = './run.sh'

app2dir_dd['parboil_sgemm'] = '../apps/devid_parboil/benchmarks/sgemm'
app2cmd_dd['parboil_sgemm'] = './run.sh'

app2dir_dd['parboil_stencil'] = '../apps/devid_parboil/benchmarks/stencil'
app2cmd_dd['parboil_stencil'] = './run.sh'


#------------------------------------------------------------------------------
# rodinia
#------------------------------------------------------------------------------
app2dir_dd['rodinia_backprop'] = '../apps/devid_rodinia/backprop'
app2cmd_dd['rodinia_backprop'] = './run.sh'

app2dir_dd['rodinia_b+tree'] = '../apps/devid_rodinia/b+tree'
app2cmd_dd['rodinia_b+tree'] = './run.sh'

app2dir_dd['rodinia_dwt2d'] = '../apps/devid_rodinia/dwt2d'
app2cmd_dd['rodinia_dwt2d'] = './run.sh'

app2dir_dd['rodinia_gaussian'] = '../apps/devid_rodinia/gaussian'
app2cmd_dd['rodinia_gaussian'] = './run.sh'

app2dir_dd['rodinia_heartwall'] = '../apps/devid_rodinia/heartwall'
app2cmd_dd['rodinia_heartwall'] = './run.sh'

app2dir_dd['rodinia_hotspot'] = '../apps/devid_rodinia/hotspot'
app2cmd_dd['rodinia_hotspot'] = './run.sh'

app2dir_dd['rodinia_lud'] = '../apps/devid_rodinia/lud'
app2cmd_dd['rodinia_lud'] = './run.sh'

app2dir_dd['rodinia_lavaMD'] = '../apps/devid_rodinia/lavaMD'
app2cmd_dd['rodinia_lavaMD'] = './run.sh'

app2dir_dd['rodinia_needle'] = '../apps/devid_rodinia/nw'
app2cmd_dd['rodinia_needle'] = './run.sh'

app2dir_dd['rodinia_pathfinder'] = '../apps/devid_rodinia/pathfinder'
app2cmd_dd['rodinia_pathfinder'] = './run.sh'

#------------------------------------------------------------------------------
# shoc
#------------------------------------------------------------------------------
app2dir_dd['shoc_lev1BFS'] = '../apps/devid_shoc/src/cuda/level1/bfs'
app2cmd_dd['shoc_lev1BFS'] = './run.sh'

app2dir_dd['shoc_lev1sort'] = '../apps/devid_shoc/src/cuda/level1/sort'
app2cmd_dd['shoc_lev1sort'] = './run.sh'

app2dir_dd['shoc_lev1fft'] = '../apps/devid_shoc/src/cuda/level1/fft'
app2cmd_dd['shoc_lev1fft'] = './run.sh'

app2dir_dd['shoc_lev1GEMM'] = '../apps/devid_shoc/src/cuda/level1/gemm'
app2cmd_dd['shoc_lev1GEMM'] = './run.sh'

app2dir_dd['shoc_lev1md5hash'] = '../apps/devid_shoc/src/cuda/level1/md5hash'
app2cmd_dd['shoc_lev1md5hash'] = './run.sh'

app2dir_dd['shoc_lev1reduction'] = '../apps/devid_shoc/src/cuda/level1/reduction'
app2cmd_dd['shoc_lev1reduction'] = './run.sh'


'''
appList.append(GPUApp_pb2.GPUApp(
    name='shoc-md',
    dir='../apps/devid_shoc/src/cuda/level1/md',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc-neuralnet',
    dir='../apps/devid_shoc/src/cuda/level1/neuralnet',
    cmd='./run.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc-scan',
    dir='../apps/devid_shoc/src/cuda/level1/scan',
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
    '''


#------------------------------------------------------------------------------
# others
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# save
#------------------------------------------------------------------------------
np.save('app2dir_dd.npy', app2dir_dd)
np.save('app2cmd_dd.npy', app2cmd_dd)
