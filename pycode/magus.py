#!/usr/bin/env python
"""Scripts to preprocess the cuda applications."""
#import os
import subprocess
import pandas as pd

METRICS_COLS = ['Device', 'Kernel', 'Invocations', 'Metric Name', 'Metric Description',
                'Min', 'Max', 'Avg']


def cuprof(appcmd, target_metrics=None, ofile=""):
    """Profile input cuda application."""
    # if target_metrics are specified, do partial profiling
    # else do full metrics profiling
    metrics_opt = "--metrics "
    if not target_metrics:
        metrics_opt += "all"
    else:
        for index, metric in enumerate(target_metrics):
            if index == len(target_metrics) - 1:
                metrics_opt += str(metric)
            else:
                metrics_opt += str(metric) + ","

    if not ofile:
        raise Exception('Output file is not specified!')

    log_opt = "--csv --log-file " + str(ofile)

    # if len(str(logFileName)):
    ##    raise Exception('Output metrics file is not specified!')

    run_nvprof = "nvprof" + " " + metrics_opt + " " + log_opt + " " + appcmd
    # print runNvprof

    pipe = subprocess.Popen(run_nvprof, shell=True)


def read_trace(logfile_csv):
    """Read profiling metrics in csv to dataframe in pandas."""
    df_trace = pd.read_csv(logfile_csv, names=METRICS_COLS, engine='python')

    # find out the number of rows to skip
    rows2skip = 0
    for index, row in df_trace.iterrows():
        if "Metric result" in str(row['Device']):
            rows2skip = index + 1  # index starting from 0
            break
    # print rows2skip

    df_trace = pd.read_csv(logfile_csv, names=METRICS_COLS, skiprows=rows2skip + 1)

    return df_trace
