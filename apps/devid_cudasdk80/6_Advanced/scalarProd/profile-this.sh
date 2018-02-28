#!/bin/bash

# metrics
nvprof --metrics all --csv     --log-file metrics_cudasdk_scalarProd.csv  ./scalarProd 0

# traces
nvprof --print-gpu-trace --csv --log-file  traces_cudasdk_scalarProd.csv  ./scalarProd 0

