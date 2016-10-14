#!/usr/bin/env python

import sys 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.mlab import PCA

f = open(sys.argv[1], 'r')
data = np.loadtxt(f, delimiter = '\t', skiprows = 1, usecols = (2,3), unpack =True)


y = data[0, :]
x = data[1, :]


plt.figure()
plt.scatter(x,y, color = "orange")
plt.ylabel('PC2')
plt.xlabel('PC1')
plt.savefig("PCA_plot.png")
plt.close()