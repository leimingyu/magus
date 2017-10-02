#!/bin/bash
nvprof --metrics all --csv --log-file md_metrics.csv \
	./MD
