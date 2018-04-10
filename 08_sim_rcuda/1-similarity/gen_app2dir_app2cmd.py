#!/usr/bin/env python
"""Indexing app dir and cmd in data dict."""

import os
import sys
import pandas as pd
import numpy as np


app2dir_dd = {}
app2cmd_dd = {}

#------------------------------------------------------------------------------
# cuda sdk 8.0:  ``$./run_rcuda.sh devid``
#------------------------------------------------------------------------------

app2dir_dd['cudasdk_matrixMul'] = '../apps/rcuda_cusdk80/0_Simple/matrixMul'
app2cmd_dd['cudasdk_matrixMul'] = './run_rcuda.sh'

app2dir_dd['cudasdk_vectorAdd'] = '../apps/rcuda_cusdk80/0_Simple/vectorAdd'
app2cmd_dd['cudasdk_vectorAdd'] = './run_rcuda.sh'

app2dir_dd['cudasdk_convolutionFFT2D'] = '../apps/rcuda_cusdk80/3_Imaging/convolutionFFT2D'
app2cmd_dd['cudasdk_convolutionFFT2D'] = './run_rcuda.sh'

app2dir_dd['cudasdk_convolutionSeparable'] = '../apps/rcuda_cusdk80/3_Imaging/convolutionSeparable'
app2cmd_dd['cudasdk_convolutionSeparable'] = './run_rcuda.sh'

app2dir_dd['cudasdk_convolutionTexture'] = '../apps/rcuda_cusdk80/3_Imaging/convolutionTexture'
app2cmd_dd['cudasdk_convolutionTexture'] = './run_rcuda.sh'

app2dir_dd['cudasdk_dct8x8'] = '../apps/rcuda_cusdk80/3_Imaging/dct8x8'
app2cmd_dd['cudasdk_dct8x8'] = './run_rcuda.sh'

app2dir_dd['cudasdk_dwtHaar1D'] = '../apps/rcuda_cusdk80/3_Imaging/dwtHaar1D'
app2cmd_dd['cudasdk_dwtHaar1D'] = './run_rcuda.sh'

app2dir_dd['cudasdk_dxtc'] = '../apps/rcuda_cusdk80/3_Imaging/dxtc'
app2cmd_dd['cudasdk_dxtc'] = './run_rcuda.sh'

app2dir_dd['cudasdk_stereoDisparity'] = '../apps/rcuda_cusdk80/3_Imaging/stereoDisparity'
app2cmd_dd['cudasdk_stereoDisparity'] = './run_rcuda.sh'

app2dir_dd['cudasdk_binomialOptions'] = '../apps/rcuda_cusdk80/4_Finance/binomialOptions'
app2cmd_dd['cudasdk_binomialOptions'] = './run_rcuda.sh'

app2dir_dd['cudasdk_BlackScholes'] = '../apps/rcuda_cusdk80/4_Finance/BlackScholes'
app2cmd_dd['cudasdk_BlackScholes'] = './run_rcuda.sh'

app2dir_dd['cudasdk_quasirandomGenerator'] = '../apps/rcuda_cusdk80/4_Finance/quasirandomGenerator'
app2cmd_dd['cudasdk_quasirandomGenerator'] = './run_rcuda.sh'

app2dir_dd['cudasdk_SobolQRNG'] = '../apps/rcuda_cusdk80/4_Finance/SobolQRNG'
app2cmd_dd['cudasdk_SobolQRNG'] = './run_rcuda.sh'

app2dir_dd['cudasdk_c++11Cuda'] = '../apps/rcuda_cusdk80/6_Advanced/c++11_cuda'
app2cmd_dd['cudasdk_c++11Cuda'] = './run_rcuda.sh'

app2dir_dd['cudasdk_concurrentKernels'] = '../apps/rcuda_cusdk80/6_Advanced/concurrentKernels'
app2cmd_dd['cudasdk_concurrentKernels'] = './run_rcuda.sh'

app2dir_dd['cudasdk_eigenvalues'] = '../apps/rcuda_cusdk80/6_Advanced/eigenvalues'
app2cmd_dd['cudasdk_eigenvalues'] = './run_rcuda.sh'

app2dir_dd['cudasdk_fastWalshTransform'] = '../apps/rcuda_cusdk80/6_Advanced/fastWalshTransform'
app2cmd_dd['cudasdk_fastWalshTransform'] = './run_rcuda.sh'

app2dir_dd['cudasdk_FDTD3d'] = '../apps/rcuda_cusdk80/6_Advanced/FDTD3d'
app2cmd_dd['cudasdk_FDTD3d'] = './run_rcuda.sh'

app2dir_dd['cudasdk_interval'] = '../apps/rcuda_cusdk80/6_Advanced/interval'
app2cmd_dd['cudasdk_interval'] = './run_rcuda.sh'

app2dir_dd['cudasdk_lineOfSight'] = '../apps/rcuda_cusdk80/6_Advanced/lineOfSight'
app2cmd_dd['cudasdk_lineOfSight'] = './run_rcuda.sh'

app2dir_dd['cudasdk_mergeSort'] = '../apps/rcuda_cusdk80/6_Advanced/mergeSort'
app2cmd_dd['cudasdk_mergeSort'] = './run_rcuda.sh'

app2dir_dd['cudasdk_radixSortThrust'] = '../apps/rcuda_cusdk80/6_Advanced/radixSortThrust'
app2cmd_dd['cudasdk_radixSortThrust'] = './run_rcuda.sh'

app2dir_dd['cudasdk_reduction'] = '../apps/rcuda_cusdk80/6_Advanced/reduction'
app2cmd_dd['cudasdk_reduction'] = './run_rcuda.sh'

app2dir_dd['cudasdk_scalarProd'] = '../apps/rcuda_cusdk80/6_Advanced/scalarProd'
app2cmd_dd['cudasdk_scalarProd'] = './run_rcuda.sh'

app2dir_dd['cudasdk_scan'] = '../apps/rcuda_cusdk80/6_Advanced/scan'
app2cmd_dd['cudasdk_scan'] = './run_rcuda.sh'

app2dir_dd['cudasdk_segmentationTreeThrust'] = '../apps/rcuda_cusdk80/6_Advanced/segmentationTreeThrust'
app2cmd_dd['cudasdk_segmentationTreeThrust'] = './run_rcuda.sh'

app2dir_dd['cudasdk_shflscan'] = '../apps/rcuda_cusdk80/6_Advanced/shfl_scan'
app2cmd_dd['cudasdk_shflscan'] = './run_rcuda.sh'

app2dir_dd['cudasdk_sortingNetworks'] = '../apps/rcuda_cusdk80/6_Advanced/sortingNetworks'
app2cmd_dd['cudasdk_sortingNetworks'] = './run_rcuda.sh'

app2dir_dd['cudasdk_threadFenceReduction'] = '../apps/rcuda_cusdk80/6_Advanced/threadFenceReduction'
app2cmd_dd['cudasdk_threadFenceReduction'] = './run_rcuda.sh'

app2dir_dd['cudasdk_transpose'] = '../apps/rcuda_cusdk80/6_Advanced/transpose'
app2cmd_dd['cudasdk_transpose'] = './run_rcuda.sh'

app2dir_dd['cudasdk_batchCUBLAS'] = '../apps/rcuda_cusdk80/7_CUDALibraries/batchCUBLAS'
app2cmd_dd['cudasdk_batchCUBLAS'] = './run_rcuda.sh'

app2dir_dd['cudasdk_boxFilterNPP'] = '../apps/rcuda_cusdk80/7_CUDALibraries/boxFilterNPP'
app2cmd_dd['cudasdk_boxFilterNPP'] = './run_rcuda.sh'

app2dir_dd['cudasdk_MCEstimatePiInlineP'] = '../apps/rcuda_cusdk80/7_CUDALibraries/MC_EstimatePiInlineP'
app2cmd_dd['cudasdk_MCEstimatePiInlineP'] = './run_rcuda.sh'

app2dir_dd['cudasdk_MCEstimatePiInlineQ'] = '../apps/rcuda_cusdk80/7_CUDALibraries/MC_EstimatePiInlineQ'
app2cmd_dd['cudasdk_MCEstimatePiInlineQ'] = './run_rcuda.sh'

app2dir_dd['cudasdk_MCEstimatePiP'] = '../apps/rcuda_cusdk80/7_CUDALibraries/MC_EstimatePiP'
app2cmd_dd['cudasdk_MCEstimatePiP'] = './run_rcuda.sh'

app2dir_dd['cudasdk_MCEstimatePiQ'] = '../apps/rcuda_cusdk80/7_CUDALibraries/MC_EstimatePiQ'
app2cmd_dd['cudasdk_MCEstimatePiQ'] = './run_rcuda.sh'

app2dir_dd['cudasdk_MCSingleAsianOptionP'] = '../apps/rcuda_cusdk80/7_CUDALibraries/MC_SingleAsianOptionP'
app2cmd_dd['cudasdk_MCSingleAsianOptionP'] = './run_rcuda.sh'

app2dir_dd['cudasdk_simpleCUBLAS'] = '../apps/rcuda_cusdk80/7_CUDALibraries/simpleCUBLAS'
app2cmd_dd['cudasdk_simpleCUBLAS'] = './run_rcuda.sh'

app2dir_dd['cudasdk_simpleCUFFTcallback'] = '../apps/rcuda_cusdk80/7_CUDALibraries/simpleCUFFT_callback'
app2cmd_dd['cudasdk_simpleCUFFTcallback'] = './run_rcuda.sh'


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
app2dir_dd['poly_2dconv'] = '../apps/rcuda_poly/CUDA/2DCONV'
app2cmd_dd['poly_2dconv'] = './run_rcuda.sh'

app2dir_dd['poly_3dconv'] = '../apps/rcuda_poly/CUDA/3DCONV'
app2cmd_dd['poly_3dconv'] = './run_rcuda.sh'

app2dir_dd['poly_3mm'] = '../apps/rcuda_poly/CUDA/3MM'
app2cmd_dd['poly_3mm'] = './run_rcuda.sh'

app2dir_dd['poly_atax'] = '../apps/rcuda_poly/CUDA/ATAX'
app2cmd_dd['poly_atax'] = './run_rcuda.sh'

app2dir_dd['poly_bicg'] = '../apps/rcuda_poly/CUDA/BICG'
app2cmd_dd['poly_bicg'] = './run_rcuda.sh'

app2dir_dd['poly_correlation'] = '../apps/rcuda_poly/CUDA/CORR'
app2cmd_dd['poly_correlation'] = './run_rcuda.sh'

app2dir_dd['poly_covariance'] = '../apps/rcuda_poly/CUDA/COVAR'
app2cmd_dd['poly_covariance'] = './run_rcuda.sh'

app2dir_dd['poly_fdtd2d'] = '../apps/rcuda_poly/CUDA/FDTD-2D'
app2cmd_dd['poly_fdtd2d'] = './run_rcuda.sh'

app2dir_dd['poly_gemm'] = '../apps/rcuda_poly/CUDA/GEMM'
app2cmd_dd['poly_gemm'] = './run_rcuda.sh'

app2dir_dd['poly_gesummv'] = '../apps/rcuda_poly/CUDA/GESUMMV'
app2cmd_dd['poly_gesummv'] = './run_rcuda.sh'

app2dir_dd['poly_mvt'] = '../apps/rcuda_poly/CUDA/MVT'
app2cmd_dd['poly_mvt'] = './run_rcuda.sh'

app2dir_dd['poly_syr2k'] = '../apps/rcuda_poly/CUDA/SYR2K'
app2cmd_dd['poly_syr2k'] = './run_rcuda.sh'

app2dir_dd['poly_syrk'] = '../apps/rcuda_poly/CUDA/SYRK'
app2cmd_dd['poly_syrk'] = './run_rcuda.sh'


#------------------------------------------------------------------------------
# lonestar
#------------------------------------------------------------------------------
app2dir_dd['lonestar_bh'] = '../apps/rcuda_lonestar/apps/bh'
app2cmd_dd['lonestar_bh'] = './run_rcuda.sh'

app2dir_dd['lonestar_dmr'] = '../apps/rcuda_lonestar/apps/dmr'
app2cmd_dd['lonestar_dmr'] = './run_rcuda.sh'

app2dir_dd['lonestar_mst'] = '../apps/rcuda_lonestar/apps/mst'
app2cmd_dd['lonestar_mst'] = './run_rcuda.sh'

app2dir_dd['lonestar_sssp'] = '../apps/rcuda_lonestar/apps/sssp'
app2cmd_dd['lonestar_sssp'] = './run_rcuda.sh'


#------------------------------------------------------------------------------
# parboil
#------------------------------------------------------------------------------
app2dir_dd['parboil_bfs'] = '../apps/rcuda_parboil/benchmarks/bfs'
app2cmd_dd['parboil_bfs'] = './run_rcuda.sh'

app2dir_dd['parboil_cutcp'] = '../apps/rcuda_parboil/benchmarks/cutcp'
app2cmd_dd['parboil_cutcp'] = './run_rcuda.sh'

app2dir_dd['parboil_lbm'] = '../apps/rcuda_parboil/benchmarks/lbm'
app2cmd_dd['parboil_lbm'] = './run_rcuda.sh'

app2dir_dd['parboil_mriq'] = '../apps/rcuda_parboil/benchmarks/mri-q'
app2cmd_dd['parboil_mriq'] = './run_rcuda.sh'

app2dir_dd['parboil_sgemm'] = '../apps/rcuda_parboil/benchmarks/sgemm'
app2cmd_dd['parboil_sgemm'] = './run_rcuda.sh'

app2dir_dd['parboil_stencil'] = '../apps/rcuda_parboil/benchmarks/stencil'
app2cmd_dd['parboil_stencil'] = './run_rcuda.sh'


#------------------------------------------------------------------------------
# rodinia
#------------------------------------------------------------------------------
app2dir_dd['rodinia_backprop'] = '../apps/rcuda_rodinia/backprop'
app2cmd_dd['rodinia_backprop'] = './run_rcuda.sh'

app2dir_dd['rodinia_b+tree'] = '../apps/rcuda_rodinia/b+tree'
app2cmd_dd['rodinia_b+tree'] = './run_rcuda.sh'

app2dir_dd['rodinia_dwt2d'] = '../apps/rcuda_rodinia/dwt2d'
app2cmd_dd['rodinia_dwt2d'] = './run_rcuda.sh'

app2dir_dd['rodinia_gaussian'] = '../apps/rcuda_rodinia/gaussian'
app2cmd_dd['rodinia_gaussian'] = './run_rcuda.sh'

app2dir_dd['rodinia_heartwall'] = '../apps/rcuda_rodinia/heartwall'
app2cmd_dd['rodinia_heartwall'] = './run_rcuda.sh'

app2dir_dd['rodinia_hybridsort'] = '../apps/rcuda_rodinia/hybridsort'
app2cmd_dd['rodinia_hybridsort'] = './run_rcuda.sh'

app2dir_dd['rodinia_hotspot'] = '../apps/rcuda_rodinia/hotspot'
app2cmd_dd['rodinia_hotspot'] = './run_rcuda.sh'

app2dir_dd['rodinia_lud'] = '../apps/rcuda_rodinia/lud'
app2cmd_dd['rodinia_lud'] = './run_rcuda.sh'

app2dir_dd['rodinia_lavaMD'] = '../apps/rcuda_rodinia/lavaMD'
app2cmd_dd['rodinia_lavaMD'] = './run_rcuda.sh'

app2dir_dd['rodinia_needle'] = '../apps/rcuda_rodinia/nw'
app2cmd_dd['rodinia_needle'] = './run_rcuda.sh'

app2dir_dd['rodinia_pathfinder'] = '../apps/rcuda_rodinia/pathfinder'
app2cmd_dd['rodinia_pathfinder'] = './run_rcuda.sh'

#------------------------------------------------------------------------------
# shoc
#------------------------------------------------------------------------------
app2dir_dd['shoc_lev1BFS'] = '../apps/rcuda_shoc/src/cuda/level1/bfs'
app2cmd_dd['shoc_lev1BFS'] = './run_rcuda.sh'

app2dir_dd['shoc_lev1sort'] = '../apps/rcuda_shoc/src/cuda/level1/sort'
app2cmd_dd['shoc_lev1sort'] = './run_rcuda.sh'

app2dir_dd['shoc_lev1fft'] = '../apps/rcuda_shoc/src/cuda/level1/fft'
app2cmd_dd['shoc_lev1fft'] = './run_rcuda.sh'

app2dir_dd['shoc_lev1GEMM'] = '../apps/rcuda_shoc/src/cuda/level1/gemm'
app2cmd_dd['shoc_lev1GEMM'] = './run_rcuda.sh'

app2dir_dd['shoc_lev1md5hash'] = '../apps/rcuda_shoc/src/cuda/level1/md5hash'
app2cmd_dd['shoc_lev1md5hash'] = './run_rcuda.sh'

app2dir_dd['shoc_lev1reduction'] = '../apps/rcuda_shoc/src/cuda/level1/reduction'
app2cmd_dd['shoc_lev1reduction'] = './run_rcuda.sh'


'''
appList.append(GPUApp_pb2.GPUApp(
    name='shoc-md',
    dir='../apps/rcuda_shoc/src/cuda/level1/md',
    cmd='./run_rcuda.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc-neuralnet',
    dir='../apps/rcuda_shoc/src/cuda/level1/neuralnet',
    cmd='./run_rcuda.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc-scan',
    dir='../apps/rcuda_shoc/src/cuda/level1/scan',
    cmd='./run_rcuda.sh'))


appList.append(GPUApp_pb2.GPUApp(
    name='shoc-spmv',
    dir='../apps/rcuda_shoc/src/cuda/level1/spmv',
    cmd='./run_rcuda.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc-stencil2d',
    dir='../apps/rcuda_shoc/src/cuda/level1/stencil2d',
    cmd='./run_rcuda.sh'))

appList.append(GPUApp_pb2.GPUApp(
    name='shoc-triad',
    dir='../apps/rcuda_shoc/src/cuda/level1/triad',
    cmd='./run_rcuda.sh'))
    '''


#------------------------------------------------------------------------------
# others
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# save
#------------------------------------------------------------------------------
np.save('app2dir_dd.npy', app2dir_dd)
np.save('app2cmd_dd.npy', app2cmd_dd)
