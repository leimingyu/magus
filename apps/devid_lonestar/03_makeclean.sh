#!/bin/bash

##download inputs
#make inputs

cd apps/

for currDir in *
do
    if [ -d $currDir ]; then
			if [ "$currDir" != "scripts" ];then
				cd $currDir
				make clean
				cd ..
		fi
	fi
done



