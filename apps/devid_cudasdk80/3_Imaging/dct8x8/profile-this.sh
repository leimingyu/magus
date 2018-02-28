#!/bin/bash

# metrics
nvprof --metrics all --csv     --log-file metrics_cudasdk_dct8x8.csv  ./dct8x8 0

# traces
nvprof --print-gpu-trace --csv --log-file  traces_cudasdk_dct8x8.csv  ./dct8x8 0

