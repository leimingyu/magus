#/bin/bash
make 
make clean 
make EXTRA_NVCCFLAGS=--cudart=shared
