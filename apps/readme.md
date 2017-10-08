#Compile For RCUDA

### cudasdk80 
```bash
cd cudasdk80 && ./compile-rcuda.sh
```


### lonestargpu 
download inputs
```bash
make inputs
```
```bash
make clean && make EXTRA_NVCCFLAGS=--cudart=shared
```
