#!/bin/bash

ITERS=10

if [ -f prof_ovhd_featall ]
then
  rm prof_ovhd_featall
fi
touch prof_ovhd_featall


##--------
## binOpt
##--------
cd binomialOptions 
for (( i=0; i<$ITERS; i++ ))
do
  ts=$(date +%s%N)
	nvprof --metrics all --csv --log-file "binomialOptions_metrics.csv"  ./binomialOptions
	runtime_ms=$((($(date +%s%N) - $ts)/1000000))

	echo -e "\nbinOpt:$runtime_ms" >> ../prof_ovhd_featall

	wait
done
cd ../



#--------
# convFFT2D 
#--------
cd convolutionFFT2D 
for (( i=0; i<ITERS; i++ ))
do
  ts=$(date +%s%N)
  nvprof --metrics all --csv --log-file "convolutionFFT2D_metrics.csv"  ./convolutionFFT2D
	runtime_ms=$((($(date +%s%N) - $ts)/1000000))
	echo -e "\nconvFFT2D:$runtime_ms" >> ../prof_ovhd_featall
	wait
done
cd ../




#--------
# interval 
#--------
cd interval 
for (( i=0; i<ITERS; i++ ))
do
  ts=$(date +%s%N)
  nvprof --metrics all --csv --log-file "interval_metrics.csv"  ./interval
	runtime_ms=$((($(date +%s%N) - $ts)/1000000))
	echo -e "\ninterval:$runtime_ms" >> ../prof_ovhd_featall
	wait
done
cd ../


#--------
# matrixMul 
#--------
cd matrixMul 
for (( i=0; i<ITERS; i++ ))
do
  ts=$(date +%s%N)
  nvprof --metrics all --csv --log-file "matrixMul_metrics.csv" ./matrixMul 
	runtime_ms=$((($(date +%s%N) - $ts)/1000000))
	echo -e "\nmatrixMul:$runtime_ms" >> ../prof_ovhd_featall
	wait
done
cd ../



#--------
# MC_OptP
#--------
cd MC_SingleAsianOptionP 
for (( i=0; i<ITERS; i++ ))
do
  ts=$(date +%s%N)
  nvprof --metrics all --csv --log-file "MC_SingleAsianOptionP_metrics.csv" ./MC_SingleAsianOptionP 
	runtime_ms=$((($(date +%s%N) - $ts)/1000000))
	echo -e "\nMC_OptP:$runtime_ms" >> ../prof_ovhd_featall
	wait
done
cd ../


#--------
# mergeSort 
#--------
cd mergeSort 
for (( i=0; i<ITERS; i++ ))
do
  ts=$(date +%s%N)
  nvprof --metrics all --csv --log-file "mergeSort_metrics.csv" ./mergeSort 
	runtime_ms=$((($(date +%s%N) - $ts)/1000000))
	echo -e "\nmergeSort:$runtime_ms" >> ../prof_ovhd_featall
	wait
done
cd ../


#--------
# quasiGen 
#--------
cd quasirandomGenerator 
for (( i=0; i<ITERS; i++ ))
do
  ts=$(date +%s%N)
  nvprof --metrics all --csv --log-file "quasirandomGenerator_metrics.csv" ./quasirandomGenerator 
	runtime_ms=$((($(date +%s%N) - $ts)/1000000))
	echo -e "\nquasiGen:$runtime_ms" >> ../prof_ovhd_featall
	wait
done
cd ../


#--------
# rdxSortTust 
#--------
cd radixSortThrust 
for (( i=0; i<ITERS; i++ ))
do
  ts=$(date +%s%N)
  nvprof --metrics all --csv --log-file "radixSortThrust_metrics.csv" ./radixSortThrust
	runtime_ms=$((($(date +%s%N) - $ts)/1000000))
	echo -e "\nrdxSortTust:$runtime_ms" >> ../prof_ovhd_featall
	wait
done
cd ../


#--------
# reduction 
#--------
cd reduction 
for (( i=0; i<ITERS; i++ ))
do
  ts=$(date +%s%N)
  nvprof --metrics all --csv --log-file "reduction_metrics.csv" ./reduction
	runtime_ms=$((($(date +%s%N) - $ts)/1000000))
	echo -e "\nreduction:$runtime_ms" >> ../prof_ovhd_featall
	wait
done
cd ../

#--------
# scan 
#--------
cd scan 
for (( i=0; i<ITERS; i++ ))
do
  ts=$(date +%s%N)
  nvprof --metrics all --csv --log-file "scan_metrics.csv" ./scan
	runtime_ms=$((($(date +%s%N) - $ts)/1000000))
	echo -e "\nscan:$runtime_ms" >> ../prof_ovhd_featall
	wait
done
cd ../


#--------
# SobolQRNG 
#--------
cd SobolQRNG 
for (( i=0; i<ITERS; i++ ))
do
  ts=$(date +%s%N)
  nvprof --metrics all --csv --log-file "SobolQRNG_metrics.csv" ./SobolQRNG
	runtime_ms=$((($(date +%s%N) - $ts)/1000000))
	echo -e "\nSobolQRNG:$runtime_ms" >> ../prof_ovhd_featall
	wait
done
cd ../


#--------
# sortNets 
#--------
cd sortingNetworks 
for (( i=0; i<ITERS; i++ ))
do
  ts=$(date +%s%N)
  nvprof --metrics all --csv --log-file "sortingNetworks_metrics.csv" ./sortingNetworks
	runtime_ms=$((($(date +%s%N) - $ts)/1000000))
	echo -e "\nsortNets:$runtime_ms" >> ../prof_ovhd_featall
	wait
done
cd ../


#--------
# transpose 
#--------
cd transpose 
for (( i=0; i<ITERS; i++ ))
do
  ts=$(date +%s%N)
  nvprof --metrics all --csv --log-file "transpose_metrics.csv" ./transpose
	runtime_ms=$((($(date +%s%N) - $ts)/1000000))
	echo -e "\ntranspose:$runtime_ms" >> ../prof_ovhd_featall
	wait
done
cd ../

