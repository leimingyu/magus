#!/bin/bash
#./bfs -i ../../datasets/bfs/NY/input/graph_input.dat  -o out.dat -d $1


# metrics
nvprof --metrics all --csv     --log-file metrics_parboil_bfs.csv ./bfs -i ../../datasets/bfs/NY/input/graph_input.dat  -o out.dat -d 0 

# traces
nvprof --print-gpu-trace --csv --log-file  traces_parboil_bfs.csv ./bfs -i ../../datasets/bfs/NY/input/graph_input.dat  -o out.dat -d 0 

mv metrics_*.csv ../../metrics/
mv traces_*.csv  ../../traces/

