#!/bin/bash

# metrics
nvprof --metrics all --csv     --log-file metrics_cudasdk_boxFilterNPP.csv  ./boxFilterNPP 0

# traces
nvprof --print-gpu-trace --csv --log-file  traces_cudasdk_boxFilterNPP.csv  ./boxFilterNPP 0

