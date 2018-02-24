#!/bin/bash
nvprof --metrics all --csv --log-file lud_metrics.csv  cuda/lud_cuda -s 256 -v
