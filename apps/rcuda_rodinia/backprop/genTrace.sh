#!/bin/bash

nvprof --print-gpu-trace  --csv ./backprop 65536 2> gpu_trace.csv 
nvprof --print-api-trace  --csv ./backprop 65536 2> api_trace.csv 
nvprof --metrics all  --csv ./backprop 65536 2> metrics_trace.csv 
nvprof --events all  --csv ./backprop 65536 2> events_trace.csv 
