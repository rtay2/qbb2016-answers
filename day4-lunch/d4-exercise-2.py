#!/usr/bin/env python

""""
Usage: d4-exercise-2.py file1 file2 window_size

"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_table(sys.argv[1])
df2 = pd.read_table(sys.argv[2])
our_size = sys.argv[3]
our_files = [df, df2]

chrom = ["2L", "2R", "3L", "3R", "4", "X"]

def calc_roll(chromosome):
    roll_mean = []
    for file in our_files:
        df_roi = file["chr"] == chromosome
        df_chrom = file[df_roi]
        smoothed = df_chrom["FPKM"].rolling(int(our_size)).mean()
        roll_mean.append(smoothed)
    plt.figure()
    plt.plot(roll_mean[0])
    plt.plot(roll_mean[1])
    plt.title("Rolling mean (size = " + our_size + ") for " + chromosome)
    plt.savefig(chromosome + "_plot.png")
    plt.close()
    
for i in chrom:
    calc_roll(i)

