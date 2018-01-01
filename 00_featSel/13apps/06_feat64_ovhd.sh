#!/bin/bash

#
# 64 metrics
#
metrics_list="branch_efficiency,warp_execution_efficiency,warp_nonpred_execution_efficiency,inst_replay_overhead,local_load_transactions_per_request,local_store_transactions_per_request,gld_transactions_per_request,gst_transactions_per_request,shared_load_transactions,local_load_transactions,global_hit_rate,local_hit_rate,gld_requested_throughput,gst_requested_throughput,gld_throughput,gst_throughput,local_memory_overhead,tex_cache_hit_rate,l2_tex_read_hit_rate,l2_tex_write_hit_rate,tex_cache_throughput,l2_tex_read_throughput,l2_tex_write_throughput,l2_read_throughput,l2_write_throughput,sysmem_write_throughput,shared_load_throughput,shared_store_throughput,gld_efficiency,gst_efficiency,sysmem_utilization,stall_inst_fetch,stall_exec_dependency,stall_memory_dependency,stall_texture,stall_sync,stall_other,stall_constant_memory_dependency,stall_pipe_busy',shared_efficiency,atomic_transactions_per_request,stall_memory_throttle,stall_not_selected,sysmem_write_utilization,sm_activity,achieved_occupancy,executed_ipc,issued_ipc,issue_slot_utilization,eligible_warps_per_cycle,l2_utilization,shared_utilization,ldst_fu_utilization,cf_fu_utilization,special_fu_utilization,tex_fu_utilization,single_precision_fu_utilization,double_precision_fu_utilization,flop_sp_efficiency,flop_dp_efficiency,dram_write_transactions,dram_read_throughput,dram_write_throughput,dram_utilization"

#echo $metrics_list

ITERS=1

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
	nvprof --metrics $metrics_list --csv --log-file "binomialOptions_metrics.csv"  ./binomialOptions
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
  nvprof --metrics $metrics_list --csv --log-file "convolutionFFT2D_metrics.csv"  ./convolutionFFT2D
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
  nvprof --metrics $metrics_list --csv --log-file "interval_metrics.csv"  ./interval
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
  nvprof --metrics $metrics_list --csv --log-file "matrixMul_metrics.csv" ./matrixMul 
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
  nvprof --metrics $metrics_list --csv --log-file "MC_SingleAsianOptionP_metrics.csv" ./MC_SingleAsianOptionP 
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
  nvprof --metrics $metrics_list --csv --log-file "mergeSort_metrics.csv" ./mergeSort 
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
  nvprof --metrics $metrics_list --csv --log-file "quasirandomGenerator_metrics.csv" ./quasirandomGenerator 
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
  nvprof --metrics $metrics_list --csv --log-file "radixSortThrust_metrics.csv" ./radixSortThrust
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
  nvprof --metrics $metrics_list --csv --log-file "reduction_metrics.csv" ./reduction
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
  nvprof --metrics $metrics_list --csv --log-file "scan_metrics.csv" ./scan
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
  nvprof --metrics $metrics_list --csv --log-file "SobolQRNG_metrics.csv" ./SobolQRNG
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
  nvprof --metrics $metrics_list --csv --log-file "sortingNetworks_metrics.csv" ./sortingNetworks
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
  nvprof --metrics $metrics_list --csv --log-file "transpose_metrics.csv" ./transpose
	runtime_ms=$((($(date +%s%N) - $ts)/1000000))
	echo -e "\ntranspose:$runtime_ms" >> ../prof_ovhd_featall
	wait
done
cd ../

