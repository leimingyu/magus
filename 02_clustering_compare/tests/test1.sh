#!/bin/bash

#
# [1] timing
# https://stackoverflow.com/questions/16959337/usr-bin-time-format-output-elapsed-time-in-milliseconds
# 
# [2] run N scripts in parallel using the background mode
# https://stackoverflow.com/questions/12907721/run-three-shell-script-simultaneously

if [ -f test1_timing_log ]
then
	rm test1_timing_log
	touch test1_timing_log
fi

ITER=10

#------------------------------------------------------------------------------
# 1) binomialOptions
#------------------------------------------------------------------------------
for (( n=1; n<=$ITER; n++ ))
do
	ts=$(date +%s%N) 

	./binomialOptions/binomialOptions

	runtime_ms=$((($(date +%s%N) - $ts)/1000000)) 

	echo "$runtime_ms"  >> test1_timing_log
done

awk '{ total += $1; count++ } END { print total/count }' test1_timing_log | tee binomialOptions_ms 



#------------------------------------------------------------------------------
# 2) conjugateGradientPrecond
#------------------------------------------------------------------------------
for (( n=1; n<=$ITER; n++ ))
do
	ts=$(date +%s%N) 

	./conjugateGradientPrecond/conjugateGradientPrecond

	runtime_ms=$((($(date +%s%N) - $ts)/1000000)) 

	echo "$runtime_ms"  >> test1_timing_log
done

awk '{ total += $1; count++ } END { print total/count }' test1_timing_log | tee  conjugateGradientPrecond_ms



#------------------------------------------------------------------------------
# 3) convolutionFFT2D 
#------------------------------------------------------------------------------
for (( n=1; n<=$ITER; n++ ))
do
	ts=$(date +%s%N) 

	./convolutionFFT2D/convolutionFFT2D

	runtime_ms=$((($(date +%s%N) - $ts)/1000000)) 

	echo "$runtime_ms"  >> test1_timing_log
done

awk '{ total += $1; count++ } END { print total/count }' test1_timing_log | tee convolutionFFT2D_ms


#------------------------------------------------------------------------------
# 4) interval 
#------------------------------------------------------------------------------
for (( n=1; n<=$ITER; n++ ))
do
	ts=$(date +%s%N) 

	./interval/interval

	runtime_ms=$((($(date +%s%N) - $ts)/1000000)) 

	echo "$runtime_ms"  >> test1_timing_log
done

awk '{ total += $1; count++ } END { print total/count }' test1_timing_log | tee interval_ms 


#------------------------------------------------------------------------------
# 5) matrixMul 
#------------------------------------------------------------------------------
for (( n=1; n<=$ITER; n++ ))
do
	ts=$(date +%s%N) 

	./matrixMul/matrixMul

	runtime_ms=$((($(date +%s%N) - $ts)/1000000)) 

	echo "$runtime_ms"  >> test1_timing_log
done

awk '{ total += $1; count++ } END { print total/count }' test1_timing_log | tee matrixMul_ms 


#------------------------------------------------------------------------------
# 6) MC_SingleAsianOptionP
#------------------------------------------------------------------------------
for (( n=1; n<=$ITER; n++ ))
do
	ts=$(date +%s%N) 

	./MC_SingleAsianOptionP/MC_SingleAsianOptionP

	runtime_ms=$((($(date +%s%N) - $ts)/1000000)) 

	echo "$runtime_ms"  >> test1_timing_log
done
awk '{ total += $1; count++ } END { print total/count }' test1_timing_log | tee MC_SingleAsianOptionP_ms 


#------------------------------------------------------------------------------
# 7) mergeSort
#------------------------------------------------------------------------------
for (( n=1; n<=$ITER; n++ ))
do
	ts=$(date +%s%N) 

	./mergeSort/mergeSort

	runtime_ms=$((($(date +%s%N) - $ts)/1000000)) 

	echo "$runtime_ms"  >> test1_timing_log
done
awk '{ total += $1; count++ } END { print total/count }' test1_timing_log | tee mergeSort_ms 


#------------------------------------------------------------------------------
# 8) quasirandomGenerator
#------------------------------------------------------------------------------
for (( n=1; n<=$ITER; n++ ))
do
	ts=$(date +%s%N) 

	./quasirandomGenerator/quasirandomGenerator	

	runtime_ms=$((($(date +%s%N) - $ts)/1000000)) 

	echo "$runtime_ms"  >> test1_timing_log
done
awk '{ total += $1; count++ } END { print total/count }' test1_timing_log | tee quasirandomGenerator_ms 


#------------------------------------------------------------------------------
# 9) radixSortThrust
#------------------------------------------------------------------------------
for (( n=1; n<=$ITER; n++ ))
do
	ts=$(date +%s%N) 

	./radixSortThrust/radixSortThrust

	runtime_ms=$((($(date +%s%N) - $ts)/1000000)) 

	echo "$runtime_ms"  >> test1_timing_log
done
awk '{ total += $1; count++ } END { print total/count }' test1_timing_log | tee radixSortThrust_ms 



#------------------------------------------------------------------------------
# 10) reduction 
#------------------------------------------------------------------------------
for (( n=1; n<=$ITER; n++ ))
do
	ts=$(date +%s%N) 

	./reduction/reduction

	runtime_ms=$((($(date +%s%N) - $ts)/1000000)) 

	echo "$runtime_ms"  >> test1_timing_log
done
awk '{ total += $1; count++ } END { print total/count }' test1_timing_log | tee reduction_ms 


#------------------------------------------------------------------------------
# 11) scan 
#------------------------------------------------------------------------------
for (( n=1; n<=$ITER; n++ ))
do
	ts=$(date +%s%N) 
	
	./scan/scan

	runtime_ms=$((($(date +%s%N) - $ts)/1000000)) 

	echo "$runtime_ms"  >> test1_timing_log
done
awk '{ total += $1; count++ } END { print total/count }' test1_timing_log | tee scan_ms 



#------------------------------------------------------------------------------
# 12) SobolQRNG 
#------------------------------------------------------------------------------
for (( n=1; n<=$ITER; n++ ))
do
	ts=$(date +%s%N) 
	
	./SobolQRNG/SobolQRNG

	runtime_ms=$((($(date +%s%N) - $ts)/1000000)) 

	echo "$runtime_ms"  >> test1_timing_log
done
awk '{ total += $1; count++ } END { print total/count }' test1_timing_log | tee SobolQRNG_ms 


#------------------------------------------------------------------------------
# 13) sortingNetworks 
#------------------------------------------------------------------------------
for (( n=1; n<=$ITER; n++ ))
do
	ts=$(date +%s%N) 
	
	./sortingNetworks/sortingNetworks

	runtime_ms=$((($(date +%s%N) - $ts)/1000000)) 

	echo "$runtime_ms"  >> test1_timing_log
done
awk '{ total += $1; count++ } END { print total/count }' test1_timing_log | tee sortingNetworks_ms 


#------------------------------------------------------------------------------
# 14) transpose
#------------------------------------------------------------------------------
for (( n=1; n<=$ITER; n++ ))
do
	ts=$(date +%s%N) 
	
	./transpose/transpose

	runtime_ms=$((($(date +%s%N) - $ts)/1000000)) 

	echo "$runtime_ms"  >> test1_timing_log
done
awk '{ total += $1; count++ } END { print total/count }' test1_timing_log | tee transpose_ms 

