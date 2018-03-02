#!/bin/bash
#./b+tree.out file ../data/b+tree/mil.txt command ../data/b+tree/command.txt $1

# metrics
nvprof --metrics all --csv     --log-file metrics_rodinia_b+tree.csv ./b+tree.out file ../data/b+tree/mil.txt command ../data/b+tree/command.txt 0
# traces
nvprof --print-gpu-trace --csv --log-file  traces_rodinia_b+tree.csv ./b+tree.out file ../data/b+tree/mil.txt command ../data/b+tree/command.txt 0

mv metrics_*.csv ../metrics/
mv traces_*.csv  ../traces/
