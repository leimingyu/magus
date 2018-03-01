#!/bin/bash

cd src/cuda/level1/ 

for currDir in *
do
    if [ -d $currDir ];then
			echo $currDir
			echo -e "\n\n"

			cd $currDir
			./profile-this.sh

			cd ..
    fi
done


##### go to level2
##cd ../level2
##
##for currDir in *
##do
##	if [ -d $currDir ];then
##		echo $currDir
##		if [ "$currDir" != "qtclustering" ];then
##		  echo -e "\n\n"
##		  cd $currDir
##		  ./1_nvprof_current.sh
##		  mv *.csv ../../../../
##		  cd ..
##		fi
##	fi
##done





echo -e "\n\n"
echo "All done"
