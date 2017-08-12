BIN    		:= $(TOPLEVEL)/bin
INPUTS 		:= $(TOPLEVEL)/inputs

NVCC 		:= nvcc
GCC  		:= g++
CC := $(GCC)
#CUB_DIR := $(TOPLEVEL)/cub-1.1.1
CUB_DIR := $(TOPLEVEL)/cub-1.7.0


SMS ?= 30 35 50 52 60
ifeq ($(GENCODE_FLAGS),)
  $(foreach sm,$(SMS),$(eval GENCODE_FLAGS += -gencode arch=compute_$(sm),code=sm_$(sm)))
endif



ifdef debug
FLAGS := $(GENCODE_FLAGS) -g -DLSGDEBUG=1 -G
else
# including -lineinfo -G causes launches to fail because of lack of resources, pity.
FLAGS := -O3 $(GENCODE_FLAGS) -g -Xptxas -v  #-lineinfo -G
endif
INCLUDES := -I $(TOPLEVEL)/include -I $(CUB_DIR)
LINKS := 

EXTRA := $(FLAGS) $(INCLUDES) $(LINKS)

.PHONY: clean variants support optional-variants

ifdef APP
$(APP): $(SRC) $(INC)
	$(NVCC) $(EXTRA) -DVARIANT=0 -o $@ $<
	cp $@ $(BIN)

variants: $(VARIANTS)

optional-variants: $(OPTIONAL_VARIANTS)

support: $(SUPPORT)

clean: 
	rm -f $(APP) $(BIN)/$(APP)
ifdef VARIANTS
	rm -f $(VARIANTS)
endif
ifdef OPTIONAL_VARIANTS
	rm -f $(OPTIONAL_VARIANTS)
endif

endif
