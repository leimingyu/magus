#!/bin/bash

# metrics
nvprof --metrics all --csv     --log-file metrics_cudasdk_dwtHaar1D.csv  ./dwtHaar1D 0

# traces
nvprof --print-gpu-trace --csv --log-file  traces_cudasdk_dwtHaar1D.csv  ./dwtHaar1D 0


