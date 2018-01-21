#!/bin/bash
#mv *.csv  ../metrics

for currDir in *
do
  if [ -d $currDir ];then
    if [ "$currDir" != "common" ]; then
			cd $currDir
			mv *_metrics.csv ../../test_apps_metrics
			mv *_trace.csv ../../test_apps_trace
			cd ..
		fi
  fi
done

