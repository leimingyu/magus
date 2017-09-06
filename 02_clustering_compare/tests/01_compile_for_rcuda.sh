#!/bin/bash
cd binomialOptions  && \
	make clean && make EXTRA_NVCCFLAGS=--cudart=shared

cd ../conjugateGradientPrecond && \
	make clean && make EXTRA_NVCCFLAGS=--cudart=shared

cd ../convolutionFFT2D && \
	make clean && make EXTRA_NVCCFLAGS=--cudart=shared

cd ../interval && \
	make clean && make EXTRA_NVCCFLAGS=--cudart=shared

cd ../matrixMul && \
	make clean && make EXTRA_NVCCFLAGS=--cudart=shared

cd ../MC_SingleAsianOptionP && \
	make clean && make EXTRA_NVCCFLAGS=--cudart=shared

cd ../mergeSort && \
	make clean && make EXTRA_NVCCFLAGS=--cudart=shared

cd ../quasirandomGenerator && \
	make clean && make EXTRA_NVCCFLAGS=--cudart=shared

cd ../radixSortThrust && \
	make clean && make EXTRA_NVCCFLAGS=--cudart=shared

cd ../reduction && \
	make clean && make EXTRA_NVCCFLAGS=--cudart=shared

cd ../scan && \
	make clean && make EXTRA_NVCCFLAGS=--cudart=shared

cd ../SobolQRNG && \
	make clean && make EXTRA_NVCCFLAGS=--cudart=shared

cd ../sortingNetworks && \
	make clean && make EXTRA_NVCCFLAGS=--cudart=shared

cd ../transpose && \
	make clean && make EXTRA_NVCCFLAGS=--cudart=shared
