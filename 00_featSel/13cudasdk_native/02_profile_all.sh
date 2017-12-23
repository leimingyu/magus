#!/bin/bash
cd binomialOptions && nvprof --metrics all --csv --log-file "binomialOptions_metrics.csv"  ./binomialOptions
cd ../

cd convolutionFFT2D && nvprof --metrics all --csv --log-file "convolutionFFT2D_metrics.csv"  ./convolutionFFT2D
cd ../

cd interval && nvprof --metrics all --csv --log-file "interval_metrics.csv"  ./interval
cd ../

cd matrixMul && nvprof --metrics all --csv --log-file "matrixMul_metrics.csv" ./matrixMul 
cd ../

cd MC_SingleAsianOptionP && nvprof --metrics all --csv --log-file "MC_SingleAsianOptionP_metrics.csv" ./MC_SingleAsianOptionP 
cd ../

cd mergeSort && nvprof --metrics all --csv --log-file "mergeSort_metrics.csv" ./mergeSort 
cd ../

cd quasirandomGenerator && nvprof --metrics all --csv --log-file "quasirandomGenerator_metrics.csv" ./quasirandomGenerator 
cd ../

cd radixSortThrust && nvprof --metrics all --csv --log-file "radixSortThrust_metrics.csv" ./radixSortThrust
cd ../

cd reduction && nvprof --metrics all --csv --log-file "reduction_metrics.csv" ./reduction
cd ../

cd scan && nvprof --metrics all --csv --log-file "scan_metrics.csv" ./scan
cd ../

cd SobolQRNG && nvprof --metrics all --csv --log-file "SobolQRNG_metrics.csv" ./SobolQRNG
cd ../

cd sortingNetworks && nvprof --metrics all --csv --log-file "sortingNetworks_metrics.csv" ./sortingNetworks
cd ../

cd transpose && nvprof --metrics all --csv --log-file "transpose_metrics.csv" ./transpose
cd ../

