include ../common/make.config

LOCAL_CC = gcc -g -O3 -Wall
CC := $(CUDA_DIR)/bin/nvcc

CUDA_FLAG = $(EXTRA_NVCCFLAGS)

SMS ?= 30 35 50 52 60
ifeq ($(GENCODE_FLAGS),)
  $(foreach sm,$(SMS),$(eval GENCODE_FLAGS += -gencode arch=compute_$(sm),code=sm_$(sm)))
endif

CUDA_FLAG += $(GENCODE_FLAGS)


all : nn hurricane_gen

clean :
	rm -rf *.o nn hurricane_gen

nn : nn_cuda.cu
	$(CC) $(CUDA_FLAG) -cuda nn_cuda.cu
	$(CC) $(CUDA_FLAG) -o nn nn_cuda.cu

hurricane_gen : hurricane_gen.c
	$(LOCAL_CC) -o $@ $< -lm

#data :
#	mkdir data
#	./gen_dataset.sh
