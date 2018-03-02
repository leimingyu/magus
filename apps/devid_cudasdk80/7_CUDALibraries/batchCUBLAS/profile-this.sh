#!/bin/bash

# metrics
nvprof --metrics all --csv     --log-file metrics_cudasdk_batchCUBLAS.csv  ./batchCUBLAS 0

# traces
nvprof --print-gpu-trace --csv --log-file  traces_cudasdk_batchCUBLAS.csv  ./batchCUBLAS 0

