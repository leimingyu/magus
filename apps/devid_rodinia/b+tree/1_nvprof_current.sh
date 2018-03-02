#!/bin/bash
nvprof --metrics all --csv --log-file b+tree_metrics.csv ./b+tree.out file ../data/b+tree/mil.txt command ../data/b+tree/command.txt 
