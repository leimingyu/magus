#!/bin/bash
nvprof --metrics all --csv --log-file hotspot_metrics.csv ./hotspot 512 2 2 ../data/hotspot/temp_512 ../data/hotspot/power_512 output.out
