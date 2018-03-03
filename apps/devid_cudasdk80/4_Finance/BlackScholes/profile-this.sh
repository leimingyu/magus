#!/bin/bash

# metrics
nvprof --metrics all --csv     --log-file metrics_cudasdk_BlackScholes.csv  ./BlackScholes 0

# traces
nvprof --print-gpu-trace --csv --log-file  traces_cudasdk_BlackScholes.csv  ./BlackScholes 0

