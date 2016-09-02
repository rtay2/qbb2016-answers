#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np


df = pd.read_table(sys.argv[1])

for item in df.itertuples():
    chrom = item[2]
    chrom_list = ["2L", "2R", "3L", "3R", "4", "X"]
    t_name = item[6]
    fpkm = item[12]
    if item[3] == "+":
        p_st = item[4] - 500
        p_end = item[4] + 500
    else: 
        p_st = item[5] - 500
        p_end = item[5] + 500
    if chrom not in chrom_list:
        continue
    else:
        print "%s\t%d\t%d\t%s\t%d" %(chrom, p_st, p_end, t_name, fpkm)



