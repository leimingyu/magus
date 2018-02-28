#!/bin/bash

# metrics
nvprof --metrics all --csv     --log-file metrics_cudasdk_MCEstimatePiInlineP.csv  ./MC_EstimatePiInlineP0

# traces
nvprof --print-gpu-trace --csv --log-file  traces_cudasdk_MCEstimatePiInlineP.csv  ./MC_EstimatePiInlineP 0

