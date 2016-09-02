#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
import statsmodels.api as sm

files = sys.argv[1:]
for i in files:
    df = pd.read_table(i, header=None)
    expr = df[4]
    chip_mean = df[5]
    model = sm.OLS(chip_mean,expr)
    results = model.fit()
    print i.replace(".bed","")
    print results.summary()
    