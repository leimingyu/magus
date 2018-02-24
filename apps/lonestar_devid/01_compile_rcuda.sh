#!/bin/bash

##download inputs
#make inputs

make clean && make EXTRA_NVCCFLAGS=--cudart=shared
