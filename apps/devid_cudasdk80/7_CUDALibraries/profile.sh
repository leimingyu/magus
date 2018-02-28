#!/bin/bash

for currDir in *
do
    if [ -d $currDir ]; then
			if [ "$currDir" != "common" ];then
				cd $currDir
				#make clean 
				#make 
				./profile-this.sh
				mv metrics_*.csv ../../metrics/
				mv traces_*.csv ../../traces/
				cd ..
		fi
	fi
done
