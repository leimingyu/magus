#!/bin/bash

#make clean
#make

cd apps
for currDir in *
do
    #echo $currDir
    if [ -d $currDir ]; then
		# check whether it is the targeted folder
		if [ "$currDir" != "bfs" ] && \
			[ "$currDir" != "pta" ] && \
			[ "$currDir" != "sp" ] && \
			[ "$currDir" != "scripts" ]; then

    	echo $currDir
		cd $currDir
		./1_nvprof_current.sh
		mv *.csv ../../
		cd ..
		fi
	fi
done

echo -e "\n\n"
echo "(Profiling Succeed!)"
