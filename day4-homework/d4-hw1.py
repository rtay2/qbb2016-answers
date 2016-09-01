#!/usr/bin/env python

""""
Usage: ./01-timecourse.py <metadata.csv> <ctab_dir>
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

df_meta = pd.read_csv(sys.argv[1])
ctab_dir = sys.argv[2]   # Telling the path so we can open multiple ctab files using for loop
repfile = pd.read_csv(sys.argv[3])

fem_Sxl = []
male_Sxl = []
fem_reps = []
male_reps = []

df_roi = df_meta["sex"] == "female"
for sample in df_meta[df_roi]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table( filename ) 
    
    df_roi2 = df["t_name"] == "FBtr0331261"
    fem_Sxl.append(df[df_roi2]["FPKM"].values) 

males = df_meta["sex"] == "male"
for sample in df_meta[males]["sample"]: 
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table( filename ) 
    
    df_roi3 = df["t_name"] == "FBtr0331261"
    male_Sxl.append(df[df_roi3]["FPKM"].values)
    
df_roi4 = repfile["sex"] == "female"
for sample in repfile[df_roi4]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table( filename )

    df_roi5 = df["t_name"] == "FBtr0331261"
    fem_reps.append(df[df_roi5]["FPKM"].values)

df_roi6 = repfile["sex"] == "male"
for sample in repfile[df_roi6]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table( filename )

    df_roi7 = df["t_name"] == "FBtr0331261"
    male_reps.append(df[df_roi7]["FPKM"].values)


x = [0, 1,2,3,4,5,6,7]
xlabels = ["10","11", "12","13", "14A", "14B", "14C", "14D"]
plt.figure()
plt.plot(fem_Sxl, label = "Female", color = 'r', linewidth = 2.5)
plt.plot(male_Sxl, label = "Male", color = 'b', linewidth = 2.5)
plt.plot([4,5,6,7],fem_reps, 'ro')
plt.plot([4,5,6,7], male_reps, 'bo')
plt.legend(loc="upper left")
plt.xlabel("Developmental Stage")
plt.ylabel("mRNA Abundance (FPKM)")
plt.xticks(x, xlabels)
plt.xlim([0,8])
plt.title("Sxl")
plt.savefig("timecourse.png")
plt.close()
