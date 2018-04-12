#!/bin/bash

#=============================================================================#
# Function: obtain the avg timing
#=============================================================================#

timeApp () {
appname=$1
runapp=$2
devid=$3

ts=$(date +%s%N)
#echo -e "\n$ts" >> /tmp/magic_time_log

### silcent the std output
$runapp $devid > /dev/null

runtime_ms=$((($(date +%s%N) - $ts)/1000000))

# runtime in ms
echo -e "\n$appname:$runtime_ms" >> /tmp/magic_time_log
}


#=============================================================================#
# Function: obtain the avg timing
#=============================================================================#

getAvg()
{
local keyWord=$1
local runtime=$(awk -v pat="$keyWord"  '$0~pat{print}' /tmp/magic_time_log  | awk -F ":" '{print $2}' | awk '{ total += $1 } END { print total/NR }')
echo $runtime
}

#=============================================================================#
# create log file
#=============================================================================#
if [ -f /tmp/magic_time_log ]
then
  rm /tmp/magic_time_log
fi
touch /tmp/magic_time_log

#=============================================================================#
# benchmark the perf 
#=============================================================================#
ITER=10

##=============================================================================#
#app1_keyword="convolutionSeparable"
#app1=$app1_keyword
#
#for (( i=1; i<=$ITER; i++ ))
#do
#  cd ../apps/devid_cudasdk80/3_Imaging/convolutionSeparable/
#  timeApp $app1_keyword ./run.sh 0 
#
#  # back to current folder
#  cd ../../../../09_case_study 
#done
#app1_runtime=$(getAvg $app1_keyword)
#echo -e $app1":\t"$app1_runtime"\n"
#
#
#
#
##=============================================================================#
#app1_keyword="fastWashTransform"
#app1=$app1_keyword
#
#for (( i=1; i<=$ITER; i++ ))
#do
#  cd ../apps/devid_cudasdk80/6_Advanced/fastWalshTransform/ 
#  timeApp $app1_keyword ./run.sh 0 
#
#  # back to current folder
#  cd ../../../../09_case_study 
#done
#app1_runtime=$(getAvg $app1_keyword)
#echo -e $app1":\t"$app1_runtime"\n"
#
#
#
##=============================================================================#
#app1_keyword="syrk"
#app1=$app1_keyword
#
#for (( i=1; i<=$ITER; i++ ))
#do
#  cd ../apps/devid_poly/CUDA/SYRK/
#  timeApp $app1_keyword ./run.sh 0 
#
#  # back to current folder
#  cd ../../../../09_case_study 
#done
#app1_runtime=$(getAvg $app1_keyword)
#echo -e $app1":\t"$app1_runtime"\n"

##=============================================================================#
#app1_keyword="3mm"
#app1=$app1_keyword
#
#for (( i=1; i<=$ITER; i++ ))
#do
#  cd ../apps/devid_poly/CUDA/3MM/
#  timeApp $app1_keyword ./run.sh 0 
#
#  # back to current folder
#  cd ../../../../09_case_study 
#done
#app1_runtime=$(getAvg $app1_keyword)
#echo -e $app1":\t"$app1_runtime"\n"
#
#
#
##=============================================================================#
#app1_keyword="CORR"   # modify here !!!
#app1=$app1_keyword
#
#for (( i=1; i<=$ITER; i++ ))
#do
#  # modify here !!!
#  cd ../apps/devid_poly/CUDA/CORR/
#  timeApp $app1_keyword ./run.sh 0 
#
#  # back to current folder
#  cd ../../../../09_case_study 
#done
#app1_runtime=$(getAvg $app1_keyword)
#echo -e $app1":\t"$app1_runtime"\n"
#
#
#
##=============================================================================#
#app1_keyword="COVAR"   # modify here !!!
#app1=$app1_keyword
#
#for (( i=1; i<=$ITER; i++ ))
#do
#  # modify here !!!
#  cd ../apps/devid_poly/CUDA/COVAR/
#  timeApp $app1_keyword ./run.sh 0 
#
#  # back to current folder
#  cd ../../../../09_case_study 
#done
#app1_runtime=$(getAvg $app1_keyword)
#echo -e $app1":\t"$app1_runtime"\n"
#
#
#
##=============================================================================#
#app1_keyword="FDTD-2D"   # modify here !!!
#app1=$app1_keyword
#
#for (( i=1; i<=$ITER; i++ ))
#do
#  # modify here !!!
#  cd ../apps/devid_poly/CUDA/FDTD-2D/
#  timeApp $app1_keyword ./run.sh 0 
#
#  # back to current folder
#  cd ../../../../09_case_study 
#done
#app1_runtime=$(getAvg $app1_keyword)
#echo -e $app1":\t"$app1_runtime"\n"



##=============================================================================#
#app1_keyword="SYR2K"   # modify here !!!
#app1=$app1_keyword
#
#for (( i=1; i<=$ITER; i++ ))
#do
#  # modify here !!!
#  cd ../apps/devid_poly/CUDA/SYR2K/
#  timeApp $app1_keyword ./run.sh 0 
#
#  # back to current folder
#  cd ../../../../09_case_study 
#done
#app1_runtime=$(getAvg $app1_keyword)
#echo -e $app1":\t"$app1_runtime"\n"
#
#
##=============================================================================#
#app1_keyword="dmr"   # modify here !!!
#app1=$app1_keyword
#
#for (( i=1; i<=$ITER; i++ ))
#do
#  # modify here !!!
#  cd ../apps/devid_lonestar/apps/dmr
#  timeApp $app1_keyword ./run.sh 0 
#
#  # back to current folder
#  cd ../../../../09_case_study 
#done
#app1_runtime=$(getAvg $app1_keyword)
#echo -e $app1":\t"$app1_runtime"\n"
#
#
#
##=============================================================================#
#app1_keyword="lbm"   # modify here !!!
#app1=$app1_keyword
#
#for (( i=1; i<=$ITER; i++ ))
#do
#  # modify here !!!
#  cd ../apps/devid_parboil/benchmarks/lbm
#
#  timeApp $app1_keyword ./run.sh 0 
#
#  # back to current folder
#  cd ../../../../09_case_study 
#done
#app1_runtime=$(getAvg $app1_keyword)
#echo -e $app1":\t"$app1_runtime"\n"


##=============================================================================#
#app1_keyword="convolutionFFT2D"   # modify here !!!
#app1=$app1_keyword
#
#for (( i=1; i<=$ITER; i++ ))
#do
#  # modify here !!!
#  cd ../apps/devid_cudasdk80/3_Imaging/convolutionFFT2D
#  timeApp $app1_keyword ./run.sh 0 
#
#  # back to current folder
#  cd ../../../../09_case_study 
#done
#app1_runtime=$(getAvg $app1_keyword)
#echo -e $app1":\t"$app1_runtime"\n"
#
#
##=============================================================================#
#app1_keyword="stereoDisparity"   # modify here !!!
#app1=$app1_keyword
#
#for (( i=1; i<=$ITER; i++ ))
#do
#  # modify here !!!
#  cd ../apps/devid_cudasdk80/3_Imaging/stereoDisparity
#  timeApp $app1_keyword ./run.sh 0 
#
#  # back to current folder
#  cd ../../../../09_case_study 
#done
#app1_runtime=$(getAvg $app1_keyword)
#echo -e $app1":\t"$app1_runtime"\n"
#
#
##=============================================================================#
#app1_keyword="binomialOptions"   # modify here !!!
#app1=$app1_keyword
#
#for (( i=1; i<=$ITER; i++ ))
#do
#  # modify here !!!
#  cd ../apps/devid_cudasdk80/4_Finance/binomialOptions
#  timeApp $app1_keyword ./run.sh 0 
#
#  # back to current folder
#  cd ../../../../09_case_study 
#done
#app1_runtime=$(getAvg $app1_keyword)
#echo -e $app1":\t"$app1_runtime"\n"
#
#
##=============================================================================#
#app1_keyword="FDTD3d"   # modify here !!!
#app1=$app1_keyword
#
#for (( i=1; i<=$ITER; i++ ))
#do
#  # modify here !!!
#  cd ../apps/devid_cudasdk80/6_Advanced/FDTD3d
#  timeApp $app1_keyword ./run.sh 0 
#
#  # back to current folder
#  cd ../../../../09_case_study 
#done
#app1_runtime=$(getAvg $app1_keyword)
#echo -e $app1":\t"$app1_runtime"\n"
#
#
#
##=============================================================================#
#app1_keyword="interval"   # modify here !!!
#app1=$app1_keyword
#
#for (( i=1; i<=$ITER; i++ ))
#do
#  # modify here !!!
#  cd ../apps/devid_cudasdk80/6_Advanced/interval
#  timeApp $app1_keyword ./run.sh 0 
#
#  # back to current folder
#  cd ../../../../09_case_study 
#done
#app1_runtime=$(getAvg $app1_keyword)
#echo -e $app1":\t"$app1_runtime"\n"
#
#
#
##=============================================================================#
#app1_keyword="radixSortThrust"   # modify here !!!
#app1=$app1_keyword
#
#for (( i=1; i<=$ITER; i++ ))
#do
#  # modify here !!!
#  cd ../apps/devid_cudasdk80/6_Advanced/radixSortThrust
#  timeApp $app1_keyword ./run.sh 0 
#
#  # back to current folder
#  cd ../../../../09_case_study 
#done
#app1_runtime=$(getAvg $app1_keyword)
#echo -e $app1":\t"$app1_runtime"\n"
#
#
#
##=============================================================================#
#app1_keyword="sortingNetworks"   # modify here !!!
#app1=$app1_keyword
#
#for (( i=1; i<=$ITER; i++ ))
#do
#  # modify here !!!
#  cd ../apps/devid_cudasdk80/6_Advanced/sortingNetworks
#  timeApp $app1_keyword ./run.sh 0 
#
#  # back to current folder
#  cd ../../../../09_case_study 
#done
#app1_runtime=$(getAvg $app1_keyword)
#echo -e $app1":\t"$app1_runtime"\n"
#
#
#
##=============================================================================#
#app1_keyword="scan"   # modify here !!!
#app1=$app1_keyword
#
#for (( i=1; i<=$ITER; i++ ))
#do
#  # modify here !!!
#  cd ../apps/devid_cudasdk80/6_Advanced/scan
#  timeApp $app1_keyword ./run.sh 0 
#
#  # back to current folder
#  cd ../../../../09_case_study 
#done
#app1_runtime=$(getAvg $app1_keyword)
#echo -e $app1":\t"$app1_runtime"\n"



###=============================================================================#
##app1_keyword="segmentationTreeThrust"   # modify here !!!
##app1=$app1_keyword
##
##for (( i=1; i<=$ITER; i++ ))
##do
##  # modify here !!!
##  cd ../apps/devid_cudasdk80/6_Advanced/segmentationTreeThrust
##  timeApp $app1_keyword ./run.sh 0 
##
##  # back to current folder
##  cd ../../../../09_case_study 
##done
##app1_runtime=$(getAvg $app1_keyword)
##echo -e $app1":\t"$app1_runtime"\n"


##=============================================================================#
#app1_keyword="MC_EstimatePiInlineP"   # modify here !!!
#app1=$app1_keyword
#
## modify here !!!
#cd ../apps/devid_cudasdk80/7_CUDALibraries/MC_EstimatePiInlineP
#
#
#for (( i=1; i<=$ITER; i++ ))
#do
#  timeApp $app1_keyword ./run.sh 0 
#
#done
#app1_runtime=$(getAvg $app1_keyword)
#echo -e $app1":\t"$app1_runtime"\n"
#
## back to current folder
#cd ../../../../09_case_study 
#
#
#
##=============================================================================#
#app1_keyword="MC_EstimatePiInlineQ"   # modify here !!!
#app1=$app1_keyword
#
## modify here !!!
#cd ../apps/devid_cudasdk80/7_CUDALibraries/MC_EstimatePiInlineQ
#
#for (( i=1; i<=$ITER; i++ ))
#do
#  timeApp $app1_keyword ./run.sh 0 
#done
#app1_runtime=$(getAvg $app1_keyword)
#echo -e $app1":\t"$app1_runtime"\n"
#
## back to current folder
#cd ../../../../09_case_study 



#=============================================================================#
app1_keyword="GEMM"   # modify here !!!
app1=$app1_keyword

# modify here !!!
cd ../apps/devid_poly/CUDA/GEMM

for (( i=1; i<=$ITER; i++ ))
do
  timeApp $app1_keyword ./run.sh 0 
done
app1_runtime=$(getAvg $app1_keyword)
echo -e $app1":\t"$app1_runtime"\n"

# back to current folder
cd ../../../../09_case_study 


#=============================================================================#
app1="lavaMD"   # modify here !!!

# modify here !!!
cd ../apps/devid_rodinia/lavaMD

for (( i=1; i<=$ITER; i++ ))
do
  timeApp $app1 ./run.sh 0 
done
app1_runtime=$(getAvg $app1)
echo -e $app1":\t"$app1_runtime"\n"

# back to current folder
cd ../../../09_case_study 



#=============================================================================#
app1="concurrentKernels"   # modify here !!!

# modify here !!!
cd ../apps/devid_cudasdk80/6_Advanced/concurrentKernels

for (( i=1; i<=$ITER; i++ ))
do
  timeApp $app1 ./run.sh 0 
done
app1_runtime=$(getAvg $app1)
echo -e $app1":\t"$app1_runtime"\n"

# back to current folder
cd ../../../../09_case_study 





