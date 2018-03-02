#!/bin/bash
#./cutcp -i ../../datasets/cutcp/small/input/watbox.sl40.pqr  -o out_small  -d $1

# metrics
nvprof --metrics all --csv     --log-file metrics_parboil_cutcp.csv ./cutcp -i ../../datasets/cutcp/small/input/watbox.sl40.pqr  -o out_small  -d 0 
# traces
nvprof --print-gpu-trace --csv --log-file  traces_parboil_cutcp.csv  ./cutcp -i ../../datasets/cutcp/small/input/watbox.sl40.pqr  -o out_small  -d 0

mv metrics_*.csv ../../metrics/
mv traces_*.csv  ../../traces/

