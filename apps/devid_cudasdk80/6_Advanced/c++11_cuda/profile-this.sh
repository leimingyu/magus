#!/bin/bash

# metrics
nvprof --metrics all --csv     --log-file metrics_cudasdk_c++11Cuda.csv  ./c++11_cuda  0

# traces
nvprof --print-gpu-trace --csv --log-file  traces_cudasdk_c++11Cuda.csv  ./c++11_cuda  0

