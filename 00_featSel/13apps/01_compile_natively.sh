#!/bin/bash
cd binomialOptions && make clean && make 

cd ../convolutionFFT2D && make clean && make

cd ../interval && make clean && make

cd ../matrixMul && make clean && make

cd ../MC_SingleAsianOptionP && make clean && make

cd ../mergeSort && make clean && make

cd ../quasirandomGenerator && make clean && make 

cd ../radixSortThrust && make clean && make

cd ../reduction && make clean && make 

cd ../scan && make clean && make

cd ../SobolQRNG && make clean && make 

cd ../sortingNetworks && make clean && make

cd ../transpose && make clean && make
