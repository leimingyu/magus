#!/bin/bash
nvprof --metrics all --csv --log-file gaussian_metrics.csv  ./gaussian -s 16
