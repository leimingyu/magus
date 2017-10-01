#!/bin/bash
make clean && make EXTRA_NVCCFLAGS=--cudart=shared
