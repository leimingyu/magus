#!/bin/bash
nvprof --metrics all --csv --log-file backprop_metrics.csv   ./backprop 65536
