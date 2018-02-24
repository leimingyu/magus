#!/bin/bash
nvprof --metrics all --csv --log-file dwt2d_metrics.csv ./dwt2d rgb.bmp -d 1024x1024 -f -5 -l 3
