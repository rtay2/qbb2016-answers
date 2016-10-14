#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


file = open(sys.argv[1])
maf = df[[4]]
to_plot = maf.values


plt.figure()
plt.style.use('ggplot')
plt.hist(to_plot,bins=50, facecolor='green')
plt.title("Allele Frequency Spectrum")
plt.xlabel("Minor Allele Frequency")
plt.ylabel("Count")
plt.show()











    
