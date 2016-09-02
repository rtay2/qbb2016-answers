#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde


df = pd.read_table(sys.argv[1])

for_dens = df["FPKM"]
density = gaussian_kde(for_dens)
data = np.linspace(-50,50,300)

plt.figure()
plt.plot(data, density(data), linewidth = 2)
plt.ylabel("Density")
plt.title("Kernel Density for SRR072893")
plt.tick_params(axis='x',top='off',bottom='off')
plt.tick_params(axis='y',left='off',right='off')
plt.savefig("KDE_plot.png")
plt.close()

