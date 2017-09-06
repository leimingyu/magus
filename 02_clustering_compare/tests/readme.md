### Tests
* test1
test 14 apps


### Notes
* lineOfSight failed with the following errors using rcuda.
```bash
lineOfSight.cu(215) : getLastCudaError() CUDA error : Kernel execution failed : (30) unknown error.
```

* MersenneTwisterGP11213
```bash
/usr/bin/ld: /usr/local/cuda-8.0/bin/../targets/x86_64-linux/lib/libculibos.a(cuos_common_posix.o): undefined reference to symbol 'dlclose@@GLIBC_2.2.5'
//lib/x86_64-linux-gnu/libdl.so.2: error adding symbols: DSO missing from command line
```

* conjugateGradient
same libculibos error
