#!/bin/bash
devid=$1
RCUDA_DEVICE_0=mcx1.coe.neu.edu:$devid  ./bfs -i ../../datasets/bfs/NY/input/graph_input.dat  -o out.dat
