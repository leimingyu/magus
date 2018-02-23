#!/bin/bash
sleep 0
./run_client.py "../apps/rcuda_cusdk80/0_Simple/matrixMul;./matrixMul" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/0_Simple/vectorAdd;./vectorAdd" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/3_Imaging/convolutionFFT2D;./convolutionFFT2D" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/3_Imaging/convolutionSeparable;./convolutionSeparable" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/3_Imaging/convolutionTexture;./convolutionTexture" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/3_Imaging/dct8x8;./dct8x8" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/3_Imaging/dct8x8;./dct8x8" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/3_Imaging/dwtHaar1D;./dwtHaar1D" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/3_Imaging/dxtc;./dxtc" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/3_Imaging/HSOpticalFlow;./HSOpticalFlow" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/3_Imaging/stereoDisparity;./stereoDisparity" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/4_Finance/binomialOptions;./binomialOptions" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/4_Finance/BlackScholes;./BlackScholes" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/4_Finance/quasirandomGenerator;./quasirandomGenerator" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/4_Finance/SobolQRNG;./SobolQRNG" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/6_Advanced/c++11_cuda;./c++11_cuda" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/6_Advanced/concurrentKernels;./concurrentKernels" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/6_Advanced/eigenvalues;./eigenvalues" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/6_Advanced/fastWalshTransform;./fastWalshTransform" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/6_Advanced/FDTD3d;./FDTD3d" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/6_Advanced/interval;./interval" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/6_Advanced/mergeSort;./mergeSort" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/6_Advanced/radixSortThrust;./radixSortThrust" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/6_Advanced/reduction;./reduction" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/6_Advanced/scalarProd;./scalarProd" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/6_Advanced/scan;./scan" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/6_Advanced/shfl_scan;./shfl_scan" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/6_Advanced/sortingNetworks;./sortingNetworks" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/6_Advanced/threadFenceReduction;./threadFenceReduction" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/6_Advanced/transpose;./transpose" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/7_CUDALibraries/batchCUBLAS;./batchCUBLAS" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/7_CUDALibraries/MC_EstimatePiInlineP;./MC_EstimatePiInlineP" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/7_CUDALibraries/MC_EstimatePiInlineQ;./MC_EstimatePiInlineQ" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/7_CUDALibraries/MC_EstimatePiP;./MC_EstimatePiP" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/7_CUDALibraries/MC_EstimatePiQ;./MC_EstimatePiQ" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/7_CUDALibraries/MC_SingleAsianOptionP;./MC_SingleAsianOptionP" &
sleep 1
./run_client.py "../apps/rcuda_cusdk80/7_CUDALibraries/simpleCUBLAS;./simpleCUBLAS" &
sleep 1
./run_client.py "../apps/rcuda_nupar/CUDA/IIR;./parIIR 10240" &
sleep 1
./run_client.py "../apps/rcuda_poly/CUDA/2DCONV;./2DConvolution.exe" &
sleep 1
./run_client.py "../apps/rcuda_poly/CUDA/3DCONV;./3DConvolution.exe" &
sleep 1
./run_client.py "../apps/rcuda_poly/CUDA/3MM;./3mm.exe" &
sleep 1
./run_client.py "../apps/rcuda_poly/CUDA/ATAX;./atax.exe" &
sleep 1
./run_client.py "../apps/rcuda_poly/CUDA/BICG;./bicg.exe" &
sleep 1
./run_client.py "../apps/rcuda_poly/CUDA/CORR;./correlation.exe" &
sleep 1
./run_client.py "../apps/rcuda_poly/CUDA/COVAR;./covariance.exe" &
sleep 1
./run_client.py "../apps/rcuda_poly/CUDA/FDTD-2D;./fdtd2d.exe" &
sleep 1
./run_client.py "../apps/rcuda_poly/CUDA/GEMM;./gemm.exe" &
sleep 1
./run_client.py "../apps/rcuda_poly/CUDA/GESUMMV;./gesummv.exe" &
sleep 1
./run_client.py "../apps/rcuda_poly/CUDA/MVT;./mvt.exe" &
sleep 1
./run_client.py "../apps/rcuda_poly/CUDA/SYR2K;./syr2k.exe" &
sleep 1
./run_client.py "../apps/rcuda_poly/CUDA/SYRK;./syrk.exe" &
sleep 1
./run_client.py "../apps/rcuda_lonestar/apps/bh;./bh 30000 50 0" &
sleep 1
./run_client.py "../apps/rcuda_lonestar/apps/dmr;./dmr  ../../inputs/250k.2 20" &
sleep 1
./run_client.py "../apps/rcuda_lonestar/apps/mst;./mst ../../inputs/LSGINPUTS/rmat12.sym.gr" &
sleep 1
./run_client.py "../apps/rcuda_lonestar/apps/sssp;./sssp ../../inputs/USA-road-d.FLA.gr" &
sleep 1
./run_client.py "../apps/rcuda_parboil/benchmarks/bfs;./bfs -i ../../datasets/bfs/NY/input/graph_input.dat  -o out.dat" &
sleep 1
./run_client.py "../apps/rcuda_parboil/benchmarks/cutcp;./cutcp -i ../../datasets/cutcp/small/input/watbox.sl40.pqr  -o out_small" &
sleep 1
./run_client.py "../apps/rcuda_parboil/benchmarks/lbm;./lbm 1 -i ../../datasets/lbm/short/input/120_120_150_ldc.of  -o out" &
sleep 1
./run_client.py "../apps/rcuda_parboil/benchmarks/mri-q;./mri-q -i ../../datasets/mri-q/small/input/32_32_32_dataset.bin" &
sleep 1
./run_client.py "../apps/rcuda_parboil/benchmarks/sgemm;./sgemm  -i ../../datasets/sgemm/small/input/matrix1.txt,../../datasets/sgemm/small/input/matrix2.txt,../../datasets/sgemm/small/input/matrix2t.txt" &
sleep 1
./run_client.py "../apps/rcuda_parboil/benchmarks/stencil;./stencil -i ../../datasets/stencil/small/input/128x128x32.bin 128 128 32 1001" &
sleep 1
./run_client.py "../apps/rcuda_rodinia/backprop;./backprop 65536" &
sleep 1
./run_client.py "../apps/rcuda_rodinia/b+tree;./b+tree.out file ../data/b+tree/mil.txt command ../data/b+tree/command.txt" &
sleep 1
./run_client.py "../apps/rcuda_rodinia/dwt2d;./dwt2d rgb.bmp -d 1024x1024 -f -5 -l 3" &
sleep 1
./run_client.py "../apps/rcuda_rodinia/gaussian;./gaussian -s 16" &
sleep 1
./run_client.py "../apps/rcuda_rodinia/heartwall;./heartwall ../data/heartwall/test.avi 20" &
sleep 1
./run_client.py "../apps/rcuda_rodinia/hotspot;./hotspot 512 2 2 ../data/hotspot/temp_512 ../data/hotspot/power_512 output.out" &
sleep 1
./run_client.py "../apps/rcuda_rodinia/lavaMD;./lavaMD -boxes1d 10" &
sleep 1
./run_client.py "../apps/rcuda_rodinia/lud;cuda/lud_cuda -s 256 -v" &
sleep 1
./run_client.py "../apps/rcuda_rodinia/nw;./needle 2048 10" &
sleep 1
./run_client.py "../apps/rcuda_rodinia/pathfinder;./pathfinder 100000 100 20" &
