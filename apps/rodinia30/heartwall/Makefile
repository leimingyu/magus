
ifdef OUTPUT
override OUTPUT = -DOUTPUT
endif

# link objects(binaries) together
CUDA_FLAG = $(EXTRA_NVCCFLAGS)

SMS ?= 30 35 50 52 60
ifeq ($(GENCODE_FLAGS),)
  $(foreach sm,$(SMS),$(eval GENCODE_FLAGS += -gencode arch=compute_$(sm),code=sm_$(sm)))
endif

CUDA_FLAG += $(GENCODE_FLAGS)

heartwall: main.o ./AVI/avilib.o ./AVI/avimod.o 
	nvcc $(CUDA_FLAG) main.o ./AVI/avilib.o ./AVI/avimod.o -I/usr/local/cuda/include -lm -o heartwall

# compile main function file into object (binary)
main.o: main.cu kernel.cu define.c
	nvcc $(CUDA_FLAG) $(OUTPUT) $(KERNEL_DIM) main.cu -I./AVI -c -O3

./AVI/avilib.o ./AVI/avimod.o:
	cd AVI; make;

# delete all object files
clean:
	rm -f *.o AVI/*.o heartwall *.linkinfo
