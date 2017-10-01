#!/bin/bash
nvprof --metrics all --csv --log-file nw_metrics.csv    ./needle 2048 10
