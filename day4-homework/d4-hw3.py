#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

df = pd.read_table(sys.argv[1])
df2 = pd.read_table(sys.argv[2])

expr_R = df["FPKM"]
expr_G = df2["FPKM"]

log_R = np.log2(expr_R + 1)
log_G = np.log2(expr_G + 1)

the_m = log_R - log_G
the_a = 0.5 * (log_R + log_G)

plt.figure()
plt.scatter(the_a, the_m, alpha = 0.1, color ='b')
plt.xlabel("A")
plt.ylabel("M")
plt.title("SRR072893 v SRR072915")
plt.tick_params(axis='x',top='off')
plt.tick_params(axis='y',right='off')
plt.savefig("MA_plot.png")
plt.close()