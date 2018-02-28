#!/bin/bash

# metrics
nvprof --metrics all --csv --log-file metrics_cudasdk_matrixMul.csv  ./matrixMul 0

# traces
nvprof --print-gpu-trace --csv --log-file trace_cudasdk_matrixMul.csv  ./matrixMul 0

