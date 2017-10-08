#Compile For RCUDA

### cudasdk80 
```bash
cd cudasdk80 && ./01-compile-rcuda.sh
```


### lonestargpu 
download inputs
```bash
make inputs
```
```bash
make clean && make EXTRA_NVCCFLAGS=--cudart=shared
```

### rodinia30
```bash
cd rodinia30 && ./01-compile-rcuda.sh
```

### polybench-gpu 
```bash
cd polybench-gpu-1.0 && ./01-compile-rcuda.sh
```

### parboil 
```bash
cd parboil && ./01-compile-rcuda.sh
```

