#!/bin/bash

cd batchCUBLAS && nvprof --print-gpu-trace --csv --log-file "batchCUBLAS_trace.csv"  ./batchCUBLAS
cd ../

cd BlackScholes && nvprof --print-gpu-trace --csv --log-file "BlackScholes_trace.csv"  ./BlackScholes
cd ../

cd boxFilterNPP && nvprof --print-gpu-trace --csv --log-file "boxFilterNPP_trace.csv"  ./boxFilterNPP
cd ../

cd conjugateGradient && nvprof --print-gpu-trace --csv --log-file "conjugateGradient_trace.csv"  ./conjugateGradient
cd ../

cd convolutionSeparable && nvprof --print-gpu-trace --csv --log-file "convolutionSeparable_trace.csv"  ./convolutionSeparable
cd ../

cd dct8x8 && nvprof --print-gpu-trace --csv --log-file "dct8x8_trace.csv"  ./dct8x8
cd ../

cd FDTD3d && nvprof --print-gpu-trace --csv --log-file "FDTD3d_trace.csv"  ./FDTD3d
cd ../

cd histogram && nvprof --print-gpu-trace --csv --log-file "histogram_trace.csv"  ./histogram
cd ../

cd nvgraph_Pagerank && nvprof --print-gpu-trace --csv --log-file "nvgraph_Pagerank_trace.csv"  ./nvgraph_Pagerank
cd ../

cd simpleCUFFT_callback && nvprof --print-gpu-trace --csv --log-file "simpleCUFFT_callback_trace.csv"  ./simpleCUFFT_callback
cd ../
