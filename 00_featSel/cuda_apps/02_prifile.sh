#!/bin/bash

for currDir in *
do
  if [ -d $currDir ];then
    if [ "$currDir" != "common" ]; then
			cd $currDir
			echo $currDir
			logFile=$currDir"_metrics.csv"
			#appExe=$currDir
			echo $logFile
			echo $appExe
			/usr/local/cuda-8.0/bin/nvprof --metrics all --csv --log-file $logFile ./$appExe
			mv *.csv ../
			cd ..
		fi
  fi
  break
done

