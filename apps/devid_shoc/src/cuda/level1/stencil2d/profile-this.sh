#!/bin/bash

#./Stencil2D -d $1

# metrics
nvprof --metrics all --csv     --log-file metrics_shoc_lev1stencil2d.csv ./Stencil2D -d 0

# traces
nvprof --print-gpu-trace --csv --log-file  traces_shoc_lev1stencil2d.csv ./Stencil2D -d 0

mv metrics_*.csv ../../../../metrics/
mv traces_*.csv  ../../../../traces/
