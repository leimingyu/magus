#!/bin/bash
nvprof --metrics all --csv --log-file GEMM_metrics.csv ./gemm.exe
