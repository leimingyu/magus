#!/bin/bash
#./lbm 1 -i ../../datasets/lbm/short/input/120_120_150_ldc.of   -o out -d $1

# metrics
nvprof --metrics all --csv     --log-file metrics_parboil_lbm.csv  ./lbm 1 -i ../../datasets/lbm/short/input/120_120_150_ldc.of   -o out -d 0 
# traces
nvprof --print-gpu-trace --csv --log-file  traces_parboil_lbm.csv  ./lbm 1 -i ../../datasets/lbm/short/input/120_120_150_ldc.of   -o out -d 0

mv metrics_*.csv ../../metrics/
mv traces_*.csv  ../../traces/


