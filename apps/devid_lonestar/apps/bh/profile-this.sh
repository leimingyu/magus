#!/bin/bash

#./bh 30000 50 $1

# metrics
nvprof --metrics all --csv     --log-file metrics_lonestar_bh.csv ./bh 30000 50 0 

# traces
nvprof --print-gpu-trace --csv --log-file  traces_lonestar_bh.csv ./bh 30000 50 0 


mv metrics_*.csv ../../metrics/
mv traces_*.csv  ../../traces/

