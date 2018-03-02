#!/bin/bash
nvprof --metrics all --csv --log-file heartwall_metrics.csv ./heartwall ../data/heartwall/test.avi 20
