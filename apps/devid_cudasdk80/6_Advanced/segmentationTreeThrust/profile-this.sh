#!/bin/bash

# metrics
nvprof --metrics all --csv     --log-file metrics_cudasdk_segmentationTreeThrust.csv  ./segmentationTreeThrust 0

# traces
nvprof --print-gpu-trace --csv --log-file  traces_cudasdk_segmentationTreeThrust.csv  ./segmentationTreeThrust 0

