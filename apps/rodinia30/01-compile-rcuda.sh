#/bin/bash
for currDir in *
do
    if [ -d $currDir ]; then
		# check whether it is the targeted folder
		if [ "$currDir" != "bfs" ] && \
			[ "$currDir" != "cfd" ] && \
			[ "$currDir" != "hybridsort" ] && \
			[ "$currDir" != "mummergpu" ] && \
			[ "$currDir" != "kmeans" ] && \
			[ "$currDir" != "nn" ] && \
			[ "$currDir" != "_nn" ] && \
			[ "$currDir" != "leukocyte" ] && \
			[ "$currDir" != "myocyte" ] && \
			[ "$currDir" != "common" ] && \
			[ "$currDir" != "data" ] && \
			[ "$currDir" != "particlefilter" ] && \
			[ "$currDir" != "srad" ] && \
			[ "$currDir" != "streamcluster" ]; then

			#echo "$currDir"
			cd $currDir
			make clean && make EXTRA_NVCCFLAGS=--cudart=shared
			cd ..
		fi
	fi
done
