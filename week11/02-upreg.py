#!/usr/bin/env python

import matplotlib.pyplot as plt
plt.style.use('ggplot')
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
from scipy import stats
import numpy as np 
import sys
from scipy.cluster.vq import kmeans2
import pandas as pd

pd.set_option('display.max_rows',1000)
pd.set_option('display.width',1000)

sig_results = pd.read_csv(sys.argv[1])


diff_expr_genes = []

for index, row in sig_results.iterrows():
    gene = str(row['genename'])
    diff_expr_genes.append(gene)

# print diff_expr_genes
    
pass1 = pd.read_csv(sys.argv[2])

final_genes = pass1[pass1.gene_names.isin(diff_expr_genes)]

print final_genes

max = final_genes.loc[final_genes['ratio'].idxmax()]
# print max

