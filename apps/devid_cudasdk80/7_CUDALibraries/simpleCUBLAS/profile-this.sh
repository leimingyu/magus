#!/bin/bash

# metrics
nvprof --metrics all --csv     --log-file metrics_cudasdk_simpleCUBLAS.csv  ./simpleCUBLAS 0

# traces
nvprof --print-gpu-trace --csv --log-file  traces_cudasdk_simpleCUBLAS.csv  ./simpleCUBLAS 0

