### Warnings
For some applications, profiling metrics will miss a few fields. Even though
the nvprof runs, you will see the warnings as below in your log csv file.

```
Warning: One or more events or metrics can't be profiled. Rerun with "--print-gpu-trace" for detail.
```

Here is a list of applications that fails.

* histogram
