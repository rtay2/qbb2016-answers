#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

df = pd.read_table(sys.argv[1])

df2 = df["FPKM"] > 0
new = df[df2]["FPKM"]
logged_FPKM = np.log(new)


plt.figure()
subplot(111,axisbg='w')
plt.hist(logged_FPKM, bins = 80,color='0.78',edgecolor='w',linewidth=1)
plt.title("Expression Levels in SRR072893 ")
plt.ylabel("Count")
plt.xlabel("Log(FPKM)")
plt.tick_params(axis='x',top='off')
plt.tick_params(axis='y',right='off')
plt.savefig("histogram.png",edgecolor='none')
plt.close()