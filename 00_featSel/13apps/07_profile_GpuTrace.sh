#!/bin/bash
cd binomialOptions && nvprof --print-gpu-trace --csv --log-file "binomialOptions_trace.csv"  ./binomialOptions
mv *.csv ../13app_trace/
cd ../

cd convolutionFFT2D && nvprof --print-gpu-trace --csv --log-file "convolutionFFT2D_trace.csv"  ./convolutionFFT2D
mv *.csv ../13app_trace/
cd ../

cd interval && nvprof --print-gpu-trace --csv --log-file "interval_trace.csv"  ./interval
mv *.csv ../13app_trace/
cd ../

cd matrixMul && nvprof --print-gpu-trace --csv --log-file "matrixMul_trace.csv" ./matrixMul 
mv *.csv ../13app_trace/
cd ../

cd MC_SingleAsianOptionP && nvprof --print-gpu-trace --csv --log-file "MC_SingleAsianOptionP_trace.csv" ./MC_SingleAsianOptionP 
mv *.csv ../13app_trace/
cd ../

cd mergeSort && nvprof --print-gpu-trace --csv --log-file "mergeSort_trace.csv" ./mergeSort 
mv *.csv ../13app_trace/
cd ../

cd quasirandomGenerator && nvprof --print-gpu-trace --csv --log-file "quasirandomGenerator_trace.csv" ./quasirandomGenerator 
mv *.csv ../13app_trace/
cd ../

cd radixSortThrust && nvprof --print-gpu-trace --csv --log-file "radixSortThrust_trace.csv" ./radixSortThrust
mv *.csv ../13app_trace/
cd ../

cd reduction && nvprof --print-gpu-trace --csv --log-file "reduction_trace.csv" ./reduction
mv *.csv ../13app_trace/
cd ../

cd scan && nvprof --print-gpu-trace --csv --log-file "scan_trace.csv" ./scan
mv *.csv ../13app_trace/
cd ../

cd SobolQRNG && nvprof --print-gpu-trace --csv --log-file "SobolQRNG_trace.csv" ./SobolQRNG
mv *.csv ../13app_trace/
cd ../

cd sortingNetworks && nvprof --print-gpu-trace --csv --log-file "sortingNetworks_trace.csv" ./sortingNetworks
mv *.csv ../13app_trace/
cd ../

cd transpose && nvprof --print-gpu-trace --csv --log-file "transpose_trace.csv" ./transpose
mv *.csv ../13app_trace/
cd ../

