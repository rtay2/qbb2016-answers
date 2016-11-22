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

file = open(sys.argv[1])
gene_expr = np.loadtxt(file, skiprows = 1, usecols = range(1,7))
expr_matrix = linkage(gene_expr, 'average')
leaves = leaves_list(expr_matrix)

inverted = np.transpose(gene_expr)
inverted_leaves = linkage(inverted)
l_test = leaves_list(inverted_leaves)
# print l_test

# print np.shape(expr_matrix)
# print np.shape(inverted_leaves)

#Creating the heatmap
# plt.figure()
# plt.imshow(gene_expr, aspect = 'auto', interpolation = 'nearest')
# plt.grid(False)
# plt.colorbar()
# plt.show()

## Creating the dendrogram
# cell_types = ["CFU", "poly", "unk", "mys", "int", "mid"]
# plt.figure()
# cell_dn = dendrogram(inverted_leaves, leaf_rotation=0, leaf_font_size = 10, labels = cell_types)
# plt.savefig("dendrogram_by_type.png")
# plt.close()


# plt.figure()
# gene_dn = dendrogram(expr_matrix,orientation='right')
# plt.show()

# idx2 = cell_dn['leaves']
# idx1 = gene_dn['leaves']
# gene_expr = gene_expr[idx1,:]
# gene_expr = gene_expr[:,idx2]
# im = plt.matshow(gene_expr, aspect = 'auto', origin='lower')
# plt.colorbar(im)
# # plt.show()
# plt.savefig("heatmap.png")
# plt.close()

## Making the CFU-Poly scatter plot
cfu_poly = gene_expr[:,0:2]

centroids, labels = kmeans2(gene_expr ,7)

plt.figure()
cfu2 = cfu_poly[:,0]
poly2 = cfu_poly[:,1]
color = np.array(["red", "blue", "green", "yellow", "orange", "purple", "pink"])
plt.scatter(cfu2,poly2,c=color[labels])
plt.xlabel("CFU")
plt.ylabel("Poly")
plt.savefig("scatterPlot.png")
plt.close()

early_expressed = []
late_expressed = []
gene_names = []




    


