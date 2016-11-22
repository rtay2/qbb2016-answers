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

df = pd.read_csv(sys.argv[1], sep="\t")


cfu_list = []
mys_list = []
unk_list = []
poly_list = []

for index, row in df.iterrows():
    cfu = float(row['CFU'])
    mys = float(row['mys'])
    poly = float(row['poly'])
    unk = float(row['unk'])
    gene = row['gene']
    average = (cfu + mys)/2
    early_expressed.append(average)
    average2 = (unk+poly)/2
    late_expressed.append(average2)
    gene_names.append(gene)
    cfu_list.append(cfu)
    mys_list.append(mys)
    unk_list.append(unk)
    poly_list.append(poly)
    
w = pd.DataFrame()
w['gene_names'] = gene_names
w['cfu'] = cfu_list
w['mys'] = mys_list
w['unk'] = unk_list
w['poly'] = poly_list
w['earlyMean'] = early_expressed
w['lateMean'] = late_expressed

# print w

ratio = []

for index, row in w.iterrows():
    lateMean = float(row['lateMean'])
    earlyMean = float(row['earlyMean'])
    ratio_r1  = (lateMean/earlyMean)
    ratio.append(ratio_r1)
    
    
w['ratio'] = ratio

# print w

variable_genes = []

for item, row in w.iterrows():
    ratio1 = float(row['ratio'])
    pass1genes = (row['gene_names'])
    if 0.5 < ratio1 < 2:
        continue
        # print "Not different"
    else:
        variable_genes.append(str(pass1genes))
        # print "Yes"
print w

# print variable_genes

# y = pd.DataFrame()
# y['variable_genes'] = variable_genes
#
# # print y
#
# test = ['Mir682', 'Slc4a1', 'Tmem184a']
#
z = w[w.gene_names.isin(variable_genes)]
print z

# r1diff = w.gene_names.isin(y)
# r1results = w[r1diff]
#
# print r1results

# for item in variable_genes:
#     print item
#



# d = pd.DataFrame()
# d['variable_genes'] = variable_genes
# d['the_early'] = the_early
# d['the_late'] = the_late
#
# raw = pd.DataFrame([])
# raw['gene'] = gene_names
# raw['rCFU'] = cfu_list
# raw['rpoly'] = poly_list
# raw['rmys'] = mys_list
# raw['runk'] = unk_list

# print raw



# diff_r1 = raw.gene.isin(variable_genes)
# results_r1 = raw[diff_r1]

# print results_r1


###don't use 
# for index, row in raw.iterrows():
#     gene1 = str(row['gene'])
#     rCFU = float(row['rCFU'])
#     rpoly = float(row['rpoly'])
#     rmys = float(row['rmys'])
#     runk = float(row['runk'])
#     if gene1  not in variable_genes:
#         pass
#     else:
#         print gene1 + "\t" + str(rCFU) + "\t" + str(rpoly) + "\t" + str(rmys) + "\t" + str(runk)
#
#
# diff_r1 = raw.gene.isin(variable_genes)
# results_r1 = raw[diff_r1]
# print diff_genes
        


# stats.ttest_rel(d['the_early'], d['the_late'])



        
# early_dict = dict(zip(gene_names, early_expressed))
# late_dict = dict(zip(gene_names, late_expressed))
#
# print early_dict