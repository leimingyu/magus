#!/bin/bash
nvprof --metrics all --csv --log-file fft_metrics.csv \
	./FFT
