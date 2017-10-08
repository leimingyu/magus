#/bin/bash
for currDir in *
do
    if [ -d $currDir ]; then
		# check whether it is the targeted folder
		if [ "$currDir" != "bfs" ] && \
			[ "$currDir" != "cfd" ] && \
			[ "$currDir" != "hybridsort" ] && \
			[ "$currDir" != "mummergpu" ] && \
			[ "$currDir" != "nn" ] && \
			[ "$currDir" != "particlefilter" ] && \
			[ "$currDir" != "srad" ] && \
			[ "$currDir" != "streamcluster" ]; then

			cd $currDir
			make clean && make EXTRA_NVCCFLAGS=--cudart=shared
			cd ..
		fi
	fi
done
