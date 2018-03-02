#!/bin/bash
#./dwt2d rgb.bmp -d 1024x1024 -f -5 -l 3 -D $1

# metrics
nvprof --metrics all --csv     --log-file metrics_rodinia_dwt2d.csv  ./dwt2d rgb.bmp -d 1024x1024 -f -5 -l 3 -D 0 
# traces
nvprof --print-gpu-trace --csv --log-file  traces_rodinia_dwt2d.csv	 ./dwt2d rgb.bmp -d 1024x1024 -f -5 -l 3 -D 0

mv metrics_*.csv ../metrics/
mv traces_*.csv  ../traces/
