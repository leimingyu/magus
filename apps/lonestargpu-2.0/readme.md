### compile program
download inputs
```bash
make inputs
```

### compile for rcuda
```bash
make clean && make EXTRA_NVCCFLAGS=--cudart=shared
```
