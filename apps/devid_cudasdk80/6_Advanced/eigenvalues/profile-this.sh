#!/bin/bash

# metrics
nvprof --metrics all --csv     --log-file metrics_cudasdk_eigenvalues.csv  ./eigenvalues 0

# traces
nvprof --print-gpu-trace --csv --log-file  traces_cudasdk_eigenvalues.csv  ./eigenvalues 0
