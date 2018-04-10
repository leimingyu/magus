#!/bin/bash
sleep 0
./run_client.py "cudasdk_convolutionFFT2D" &
sleep 1
./run_client.py "poly_syr2k" &
sleep 1
./run_client.py "lonestar_dmr" &
sleep 1
./run_client.py "cudasdk_sortingNetworks" &
sleep 1
./run_client.py "poly_syrk" &
sleep 1
./run_client.py "parboil_lbm" &
sleep 1
./run_client.py "cudasdk_convolutionSeparable" &
sleep 1
./run_client.py "cudasdk_binomialOptions" &
sleep 1
./run_client.py "poly_3mm" &
sleep 1
./run_client.py "cudasdk_radixSortThrust" &
sleep 1
./run_client.py "cudasdk_FDTD3d" &
sleep 1
./run_client.py "poly_correlation" &
sleep 1
./run_client.py "poly_covariance" &
sleep 1
./run_client.py "poly_fdtd2d" &
sleep 1
./run_client.py "cudasdk_interval" &
sleep 1
./run_client.py "cudasdk_scan" &
sleep 1
./run_client.py "cudasdk_stereoDisparity" &
sleep 1
./run_client.py "cudasdk_fastWalshTransform" &
