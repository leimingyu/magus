#!/bin/bash

#usage: mummergpu [options] reference.fna query.fna

#bin/mummergpu -G $1 ../data/mummergpu/NC_003997.fna ../data/mummergpu/NC_003997.20k.fna  > NC_00399.out

# metrics
nvprof --metrics all --csv     --log-file metrics_rodinia_mummergpu.csv  bin/mummergpu -G 0 ../data/mummergpu/NC_003997.fna ../data/mummergpu/NC_003997.20k.fna  > NC_00399.out
# traces
nvprof --print-gpu-trace --csv --log-file  traces_rodinia_mummergpu.csv  bin/mummergpu -G 0 ../data/mummergpu/NC_003997.fna ../data/mummergpu/NC_003997.20k.fna  > NC_00399.out 

mv metrics_*.csv ../metrics/
mv traces_*.csv  ../traces/


