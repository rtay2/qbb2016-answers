#!/usr/bin/env python

""""
Compares FPKM of Sxl for two samples where FPKM > 0. 
Usage: d4-exercise-1.py file1 file2
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_table(sys.argv[1])
df2 = pd.read_table(sys.argv[2])

def make_boxplots(file): 
    df_Sxl = file["gene_name"] == "Sxl"
    df_x = file[df_Sxl]
    df_db = df_x["FPKM"] > 0
    df_dbsub = df_x[df_db]
    logged_FPKM = np.log(df_dbsub["FPKM"])
    return logged_FPKM
    
value1=make_boxplots(df)
print value1

value2=make_boxplots(df2)
print value2


plt.figure()
plt.boxplot([value1, value2],labels = ["893","915"])
plt.ylabel("Log(FPKM)")
plt.savefig("Sxl.png")
plt.close()
