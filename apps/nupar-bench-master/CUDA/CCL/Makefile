CPP = g++
CUDA_VERSION = cuda-8.0
NVCC = nvcc

SOURCEDIR = .


CPP_SOURCES = $(SOURCEDIR)/accl_main.cpp
CU_SOURCES = $(SOURCEDIR)/accl.cu

CFLAGS =

NVCCFLAGS := $(EXTRA_NVCCFLAGS)
NVCCFLAGS += -pg

ARCH = -arch=sm_35 \
		     -gencode=arch=compute_50,code=sm_50 \
		     -gencode=arch=compute_52,code=sm_52 \
		     -gencode=arch=compute_61,code=compute_61

EXE = $(SOURCEDIR)/accl

DEVICE_OBJS = $(SOURCEDIR)/accl_cu.o

LINK_OBJS = $(SOURCEDIR)/accl_cu_dlink.o

all: accl

accl: accl_cu_dlink.o
	$(CPP) -o $(EXE) $(DEVICE_OBJS) $(LINK_OBJS) $(CPP_SOURCES) -L/usr/local/$(CUDA_VERSION)/lib64 -lcudart -lcuda -lcudadevrt -lpthread -fopenmp

accl_cu_dlink.o: accl_cu.o
	$(NVCC) $(NVCCFLAGS) $(ARCH) -Xcompiler '-fPIC' -dlink $(DEVICE_OBJS) -o $(LINK_OBJS) -lcudadevrt

accl_cu.o:
	$(NVCC) $(NVCCFLAGS) $(ARCH) -Xcompiler '-fPIC' -dc -m64 $(CU_SOURCES) -o $(DEVICE_OBJS)

clean:
	rm -f $(DEVICE_OBJS)
	rm -f $(LINK_OBJS)
	rm -f $(EXE)
