include ../common/make.config
CC := $(CUDA_DIR)/bin/nvcc

SMS ?= 30 35 50 52 60

ifeq ($(CC_FLAGS),)
  $(foreach sm,$(SMS),$(eval CC_FLAGS += -gencode arch=compute_$(sm),code=sm_$(sm)))
endif


ifdef VERIFY
override VERIFY = -DVERIFY
endif

ifdef OUTPUT
override OUTPUT = -DOUTPUT
endif

ifdef TIMER
override TIMER = -DTIMER
endif

hybridsort: main.cu  bucketsort.cu bucketsort.cuh bucketsort_kernel.cu histogram1024_kernel.cu  mergesort.cu mergesort.cuh mergesort_kernel.cu
	$(CC) $(CC_FLAGS) -I$(CUDA_DIR)/samples/common/inc/ $(VERIFY) $(OUTPUT) $(TIMER) $(HISTO_WG_SIZE_0) $(BUCKET_WG_SIZE_0) $(BUCKET_WG_SIZE_1) $(MERGE_WG_SIZE_0) $(MERGE_WG_SIZE_1) bucketsort.cu mergesort.cu main.cu -o hybridsort

clean:
	rm	*.o hybridsort
