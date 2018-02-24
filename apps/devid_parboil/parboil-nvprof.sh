#!/bin/bash

cd benchmarks

for currDir in *
do
    if [ -d $currDir ];then
		#echo $currDir 
		if [ "$currDir" != "others_" ]; then
			echo $currDir
			echo -e "\n\n"

			cd $currDir
			make clean
			make
			./1_nvprof_current.sh
			mv *.csv ../../
			cd ..
		fi
    fi
done

echo -e "\n\n"
echo "All done"
