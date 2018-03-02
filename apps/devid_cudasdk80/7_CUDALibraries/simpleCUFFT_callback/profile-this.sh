#!/bin/bash

# metrics
nvprof --metrics all --csv     --log-file metrics_cudasdk_simpleCUFFTcallback.csv  ./simpleCUFFT_callback 0

# traces
nvprof --print-gpu-trace --csv --log-file  traces_cudasdk_simpleCUFFTcallback.csv  ./simpleCUFFT_callback 0


