#!/bin/bash
LSGINPUTS=../../inputs  
#./dmr $LSGINPUTS/250k.2 20 $1 


# metrics
nvprof --metrics all --csv     --log-file metrics_lonestar_dmr.csv  ./dmr $LSGINPUTS/250k.2 20 0 

# traces
nvprof --print-gpu-trace --csv --log-file  traces_lonestar_dmr.csv  ./dmr $LSGINPUTS/250k.2 20 0 


mv metrics_*.csv ../../metrics/
mv traces_*.csv  ../../traces/
