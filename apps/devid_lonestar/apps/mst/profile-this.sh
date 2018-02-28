#!/bin/bash
LSGINPUTS=../../inputs
#./mst $LSGINPUTS/rmat12.sym.gr $1 

# metrics
nvprof --metrics all --csv     --log-file metrics_lonestar_mst.csv ./mst $LSGINPUTS/rmat12.sym.gr 0  
# traces
nvprof --print-gpu-trace --csv --log-file  traces_lonestar_mst.csv ./mst $LSGINPUTS/rmat12.sym.gr 0  

mv metrics_*.csv ../../metrics/
mv traces_*.csv  ../../traces/

