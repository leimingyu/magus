#!/bin/bash

# metrics
nvprof --metrics all --csv     --log-file metrics_cudasdk_FDTD3d.csv  ./FDTD3d 0

# traces
nvprof --print-gpu-trace --csv --log-file  traces_cudasdk_FDTD3d.csv  ./FDTD3d 0


