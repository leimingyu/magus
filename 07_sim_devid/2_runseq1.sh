#!/bin/bash
sleep 0
./run_client.py "cudasdk_matrixMul" &
sleep 1
./run_client.py "cudasdk_vectorAdd" &
sleep 1
./run_client.py "cudasdk_convolutionFFT2D" &
sleep 1
./run_client.py "cudasdk_convolutionSeparable" &
sleep 1
./run_client.py "cudasdk_convolutionTexture" &
sleep 1
./run_client.py "cudasdk_dct8x8" &
sleep 1
./run_client.py "cudasdk_dwtHaar1D" &
sleep 1
./run_client.py "cudasdk_dxtc" &
sleep 1
./run_client.py "cudasdk_stereoDisparity" &
sleep 1
./run_client.py "cudasdk_binomialOptions" &
sleep 1
./run_client.py "cudasdk_BlackScholes" &
sleep 1
./run_client.py "cudasdk_quasirandomGenerator" &
sleep 1
./run_client.py "cudasdk_SobolQRNG" &
sleep 1
./run_client.py "cudasdk_c++11Cuda" &
sleep 1
./run_client.py "cudasdk_concurrentKernels" &
sleep 1
./run_client.py "cudasdk_eigenvalues" &
sleep 1
./run_client.py "cudasdk_fastWalshTransform" &
sleep 1
./run_client.py "cudasdk_FDTD3d" &
sleep 1
./run_client.py "cudasdk_interval" &
sleep 1
./run_client.py "cudasdk_lineOfSight" &
sleep 1
./run_client.py "cudasdk_mergeSort" &
sleep 1
./run_client.py "cudasdk_radixSortThrust" &
sleep 1
./run_client.py "cudasdk_reduction" &
sleep 1
./run_client.py "cudasdk_scalarProd" &
sleep 1
./run_client.py "cudasdk_scan" &
sleep 1
./run_client.py "cudasdk_segmentationTreeThrust" &
sleep 1
./run_client.py "cudasdk_shflscan" &
sleep 1
./run_client.py "cudasdk_sortingNetworks" &
sleep 1
./run_client.py "cudasdk_threadFenceReduction" &
sleep 1
./run_client.py "cudasdk_transpose" &
sleep 1
./run_client.py "cudasdk_batchCUBLAS" &
sleep 1
./run_client.py "cudasdk_boxFilterNPP" &
sleep 1
./run_client.py "cudasdk_MCEstimatePiInlineP" &
sleep 1
./run_client.py "cudasdk_MCEstimatePiInlineQ" &
sleep 1
./run_client.py "cudasdk_MCEstimatePiP" &
sleep 1
./run_client.py "cudasdk_MCEstimatePiQ" &
sleep 1
./run_client.py "cudasdk_MCSingleAsianOptionP" &
sleep 1
./run_client.py "cudasdk_simpleCUBLAS" &
sleep 1
./run_client.py "cudasdk_simpleCUFFTcallback" &
sleep 1
./run_client.py "poly_2dconv" &
sleep 1
./run_client.py "poly_3dconv" &
sleep 1
./run_client.py "poly_3mm" &
sleep 1
./run_client.py "poly_atax" &
sleep 1
./run_client.py "poly_bicg" &
sleep 1
./run_client.py "poly_correlation" &
sleep 1
./run_client.py "poly_covariance" &
sleep 1
./run_client.py "poly_fdtd2d" &
sleep 1
./run_client.py "poly_gemm" &
sleep 1
./run_client.py "poly_gesummv" &
sleep 1
./run_client.py "poly_mvt" &
sleep 1
./run_client.py "poly_syr2k" &
sleep 1
./run_client.py "poly_syrk" &
sleep 1
./run_client.py "lonestar_bh" &
sleep 1
./run_client.py "lonestar_dmr" &
sleep 1
./run_client.py "lonestar_mst" &
sleep 1
./run_client.py "lonestar_sssp" &
sleep 1
./run_client.py "parboil_bfs" &
sleep 1
./run_client.py "parboil_cutcp" &
sleep 1
./run_client.py "parboil_lbm" &
sleep 1
./run_client.py "parboil_mriq" &
sleep 1
./run_client.py "parboil_sgemm" &
sleep 1
./run_client.py "parboil_stencil" &
sleep 1
./run_client.py "rodinia_backprop" &
sleep 1
./run_client.py "rodinia_b+tree" &
sleep 1
./run_client.py "rodinia_dwt2d" &
sleep 1
./run_client.py "rodinia_gaussian" &
sleep 1
./run_client.py "rodinia_heartwall" &
sleep 1
./run_client.py "rodinia_hybridsort" &
sleep 1
./run_client.py "rodinia_hotspot" &
sleep 1
./run_client.py "rodinia_lud" &
sleep 1
./run_client.py "rodinia_lavaMD" &
sleep 1
./run_client.py "rodinia_needle" &
sleep 1
./run_client.py "rodinia_pathfinder" &
sleep 1
./run_client.py "shoc_lev1BFS" &
sleep 1
./run_client.py "shoc_lev1sort" &
sleep 1
./run_client.py "shoc_lev1fft" &
sleep 1
./run_client.py "shoc_lev1GEMM" &
sleep 1
./run_client.py "shoc_lev1md5hash" &
sleep 1
./run_client.py "shoc_lev1reduction" &
