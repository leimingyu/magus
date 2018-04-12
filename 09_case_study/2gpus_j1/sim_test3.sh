#!/bin/bash

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

#================#
# create log file
#================#
if [ -f /tmp/magic_time_log ]
then
  rm /tmp/magic_time_log
fi
touch /tmp/magic_time_log

#================#
# benchmark the perf 
#================#
ITER=10

app1_keyword="stereoDisparity"
app1=$app1_keyword

app2_keyword="3MM"
app2=$app2_keyword

app3_keyword="GEMM"
app3=$app3_keyword

app4_keyword="lavaMD"
app4=$app4_keyword

for (( i=1; i<=$ITER; i++ ))
do
  # gpu 0
  cd ../../apps/devid_cudasdk80/3_Imaging/stereoDisparity
  timeApp $app1_keyword ./run.sh 0 &

  # gpu 1
  cd ../../../devid_poly/CUDA/3MM/
  timeApp $app2_keyword ./run.sh 1 &

  # gpu 0
  cd ../../../devid_poly/CUDA/GEMM/
  timeApp $app3_keyword ./run.sh 0 &

  # gpu 1
  cd ../../../devid_rodinia/lavaMD/ 
  timeApp $app4_keyword ./run.sh 1 &

  wait

  # back to current folder
  cd ../../../09_case_study/2gpus_j1
done

currentFile=`basename "$0"`
echo -e "\nTest Done! ($currentFile)\nCheck /tmp/magic_time_log\n"

#================#
# obtain the timing 
#================#
getAvg()
{
local keyWord=$1
local runtime=$(awk -v pat="$keyWord"  '$0~pat{print}' /tmp/magic_time_log  | awk -F ":" '{print $2}' | awk '{ total += $1 } END { print total/NR }')
echo $runtime
}

app1_runtime=$(getAvg $app1_keyword)
app2_runtime=$(getAvg $app2_keyword)
app3_runtime=$(getAvg $app3_keyword)
app4_runtime=$(getAvg $app4_keyword)

echo -e $app1":\t"$app1_runtime"\n"$app2":\t"$app2_runtime"\n"$app3":\t"$app3_runtime"\n"$app4":\t"$app4_runtime"\n"
