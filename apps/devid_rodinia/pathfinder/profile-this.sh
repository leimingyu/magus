#!/bin/bash
#./pathfinder 100000 100 20 $1

# metrics
nvprof --metrics all --csv     --log-file metrics_rodinia_pathfinder.csv  ./pathfinder 100000 100 20 0
# traces
nvprof --print-gpu-trace --csv --log-file  traces_rodinia_pathfinder.csv  ./pathfinder 100000 100 20 0

mv metrics_*.csv ../metrics/
mv traces_*.csv  ../traces/
