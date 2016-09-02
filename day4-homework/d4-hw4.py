#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde


df = pd.read_table(sys.argv[1])

for_dens = df["FPKM"] + 1
w_log = np.log10(for_dens)

density = gaussian_kde(w_log)
data = np.linspace(-1,4, 200)

plt.figure()
plt.plot(data, density(data), linewidth = 1)
plt.ylabel("Density")
plt.xlabel("FPKM")
plt.title("Kernel Density for SRR072893")
plt.tick_params(axis='x',top='off')
plt.tick_params(axis='y',left='off')
plt.savefig("KDE_plot.png")
plt.close()


