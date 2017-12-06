#!/bin/bash
nvprof --metrics all --csv --log-file pathfinder_metrics.csv \
./pathfinder 100000 100 20 > result.txt
