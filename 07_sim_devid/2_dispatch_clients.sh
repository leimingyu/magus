#!/bin/bash
sleep 0
./run_client.py "../apps/devid_cudasdk80/0_Simple/matrixMul;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/0_Simple/vectorAdd;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/3_Imaging/convolutionFFT2D;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/3_Imaging/convolutionSeparable;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/3_Imaging/convolutionTexture;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/3_Imaging/dct8x8;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/3_Imaging/dwtHaar1D;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/3_Imaging/dxtc;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/3_Imaging/histogram;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/3_Imaging/HSOpticalFlow;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/3_Imaging/stereoDisparity;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/4_Finance/binomialOptions;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/4_Finance/BlackScholes;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/4_Finance/quasirandomGenerator;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/4_Finance/SobolQRNG;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/6_Advanced/c++11_cuda;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/6_Advanced/concurrentKernels;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/6_Advanced/eigenvalues;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/6_Advanced/fastWalshTransform;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/6_Advanced/FDTD3d;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/6_Advanced/interval;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/6_Advanced/lineOfSight;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/6_Advanced/mergeSort;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/6_Advanced/radixSortThrust;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/6_Advanced/reduction;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/6_Advanced/scalarProd;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/6_Advanced/scan;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/6_Advanced/segmentationTreeThrust;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/6_Advanced/shfl_scan;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/6_Advanced/sortingNetworks;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/6_Advanced/threadFenceReduction;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/6_Advanced/transpose;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/7_CUDALibraries/batchCUBLAS;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/7_CUDALibraries/boxFilterNPP;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/7_CUDALibraries/MC_EstimatePiInlineP;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/7_CUDALibraries/MC_EstimatePiInlineQ;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/7_CUDALibraries/MC_EstimatePiP;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/7_CUDALibraries/MC_EstimatePiQ;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/7_CUDALibraries/MC_SingleAsianOptionP;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/7_CUDALibraries/simpleCUBLAS;./run.sh" &
sleep 1
./run_client.py "../apps/devid_cudasdk80/7_CUDALibraries/simpleCUFFT_callback;./run.sh" &
sleep 1
./run_client.py "../apps/devid_poly/CUDA/2DCONV;./run.sh" &
sleep 1
./run_client.py "../apps/devid_poly/CUDA/3DCONV;./run.sh" &
sleep 1
./run_client.py "../apps/devid_poly/CUDA/3MM;./run.sh" &
sleep 1
./run_client.py "../apps/devid_poly/CUDA/ATAX;./run.sh" &
sleep 1
./run_client.py "../apps/devid_poly/CUDA/BICG;./run.sh" &
sleep 1
./run_client.py "../apps/devid_poly/CUDA/CORR;./run.sh" &
sleep 1
./run_client.py "../apps/devid_poly/CUDA/COVAR;./run.sh" &
sleep 1
./run_client.py "../apps/devid_poly/CUDA/FDTD-2D;./run.sh" &
sleep 1
./run_client.py "../apps/devid_poly/CUDA/GEMM;./run.sh" &
sleep 1
./run_client.py "../apps/devid_poly/CUDA/GESUMMV;./run.sh" &
sleep 1
./run_client.py "../apps/devid_poly/CUDA/MVT;./run.sh" &
sleep 1
./run_client.py "../apps/devid_poly/CUDA/SYR2K;./run.sh" &
sleep 1
./run_client.py "../apps/devid_poly/CUDA/SYRK;./run.sh" &
sleep 1
./run_client.py "../apps/devid_lonestar/apps/bh;./run.sh" &
sleep 1
./run_client.py "../apps/devid_lonestar/apps/dmr;./run.sh" &
sleep 1
./run_client.py "../apps/devid_lonestar/apps/mst;./run.sh" &
sleep 1
./run_client.py "../apps/devid_lonestar/apps/sssp;./run.sh" &
sleep 1
./run_client.py "../apps/devid_parboil/benchmarks/bfs;./run.sh" &
sleep 1
./run_client.py "../apps/devid_parboil/benchmarks/cutcp;./run.sh" &
sleep 1
./run_client.py "../apps/devid_parboil/benchmarks/lbm;./run.sh" &
sleep 1
./run_client.py "../apps/devid_parboil/benchmarks/mri-q;./run.sh" &
sleep 1
./run_client.py "../apps/devid_parboil/benchmarks/sgemm;./run.sh" &
sleep 1
./run_client.py "../apps/devid_parboil/benchmarks/stencil;./run.sh" &
sleep 1
./run_client.py "../apps/devid_rodinia/backprop;./run.sh" &
sleep 1
./run_client.py "../apps/devid_rodinia/dwt2d;./run.sh" &
sleep 1
./run_client.py "../apps/devid_rodinia/gaussian;./run.sh" &
sleep 1
./run_client.py "../apps/devid_rodinia/lavaMD;./run.sh" &
sleep 1
./run_client.py "../apps/devid_rodinia/lud;./run.sh" &
sleep 1
./run_client.py "../apps/devid_rodinia/nw;./run.sh" &
sleep 1
./run_client.py "../apps/devid_rodinia/pathfinder;./run.sh" &
sleep 1
./run_client.py "../apps/devid_shoc/src/cuda/level1/bfs;./run.sh" &
sleep 1
./run_client.py "../apps/devid_shoc/src/cuda/level1/fft;./run.sh" &
sleep 1
./run_client.py "../apps/devid_shoc/src/cuda/level1/gemm;./run.sh" &
sleep 1
./run_client.py "../apps/devid_shoc/src/cuda/level1/md;./run.sh" &
sleep 1
./run_client.py "../apps/devid_shoc/src/cuda/level1/md5hash;./run.sh" &
sleep 1
./run_client.py "../apps/devid_shoc/src/cuda/level1/neuralnet;./run.sh" &
sleep 1
./run_client.py "../apps/devid_shoc/src/cuda/level1/reduction;./run.sh" &
sleep 1
./run_client.py "../apps/devid_shoc/src/cuda/level1/scan;./run.sh" &
sleep 1
./run_client.py "../apps/devid_shoc/src/cuda/level1/sort;./run.sh" &
sleep 1
./run_client.py "../apps/devid_shoc/src/cuda/level1/spmv;./run.sh" &
sleep 1
./run_client.py "../apps/devid_shoc/src/cuda/level1/stencil2d;./run.sh" &
sleep 1
./run_client.py "../apps/devid_shoc/src/cuda/level1/triad;./run.sh" &
sleep 1
./run_client.py "../apps/devid_shoc/src/cuda/level2/qtclustering;./run.sh" &
sleep 1
./run_client.py "../apps/devid_shoc/src/cuda/level2/s3d;./run.sh" &
