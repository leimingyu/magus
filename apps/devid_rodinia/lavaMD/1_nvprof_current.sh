#!/bin/bash
nvprof --metrics all --csv --log-file lavaMD_metrics.csv  ./lavaMD -boxes1d 10
