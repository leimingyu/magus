#!/bin/bash

# metrics
nvprof --metrics all --csv     --log-file metrics_cudasdk_convolutionFFT2D.csv  ./convolutionFFT2D 0

# traces
nvprof --print-gpu-trace --csv --log-file  traces_cudasdk_convolutionFFT2D.csv  ./convolutionFFT2D 0


