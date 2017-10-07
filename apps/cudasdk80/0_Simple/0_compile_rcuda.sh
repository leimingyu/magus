#!/bin/bash

for currDir in *
do
    if [ -d $currDir ]; then
		if [ "$currDir" != "common" ];then
			cd $currDir
			make clean && make EXTRA_NVCCFLAGS=--cudart=shared
		fi
	fi
done
