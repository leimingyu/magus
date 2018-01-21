#!/bin/bash

cd batchCUBLAS && nvprof --metrics all --csv --log-file "batchCUBLAS_metrics.csv"  ./batchCUBLAS
cd ../

cd BlackScholes && nvprof --metrics all --csv --log-file "BlackScholes_metrics.csv"  ./BlackScholes
cd ../

cd boxFilterNPP && nvprof --metrics all --csv --log-file "boxFilterNPP_metrics.csv"  ./boxFilterNPP
cd ../

cd conjugateGradient && nvprof --metrics all --csv --log-file "conjugateGradient_metrics.csv"  ./conjugateGradient
cd ../

cd convolutionSeparable && nvprof --metrics all --csv --log-file "convolutionSeparable_metrics.csv"  ./convolutionSeparable
cd ../

cd dct8x8 && nvprof --metrics all --csv --log-file "dct8x8_metrics.csv"  ./dct8x8
cd ../

cd FDTD3d && nvprof --metrics all --csv --log-file "FDTD3d_metrics.csv"  ./FDTD3d
cd ../

cd histogram && nvprof --metrics all --csv --log-file "histogram_metrics.csv"  ./histogram
cd ../

cd nvgraph_Pagerank && nvprof --metrics all --csv --log-file "nvgraph_Pagerank_metrics.csv"  ./nvgraph_Pagerank
cd ../

cd simpleCUFFT_callback && nvprof --metrics all --csv --log-file "simpleCUFFT_callback_metrics.csv"  ./simpleCUFFT_callback
cd ../
