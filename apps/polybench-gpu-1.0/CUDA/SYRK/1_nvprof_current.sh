#!/bin/bash
nvprof --metrics all --csv --log-file SYRK_metrics.csv ./syrk.exe
