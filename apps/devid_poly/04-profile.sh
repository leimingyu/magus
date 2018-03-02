#!/bin/bash

#make clean
#make

cd CUDA 
for currDir in *
do
    #echo $currDir
    if [ -d $currDir ]; then
		  # check whether it is the targeted folder
		  echo -e "\n\n"
      echo $currDir

		  cd $currDir

		  ./profile-this.sh
		  #mv *.csv ../../
		  cd ..
	fi
done

echo -e "\n\n"
echo "(Profiling Succeed!)"
