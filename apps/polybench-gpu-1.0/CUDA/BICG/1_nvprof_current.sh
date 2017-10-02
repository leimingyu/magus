#!/bin/bash
nvprof --metrics all --csv --log-file BICG_metrics.csv ./bicg.exe
