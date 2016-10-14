#!/usr/bin/env python

import sys
import fnmatch
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

n = 1

for file in sys.argv[1:]:
    f = open(file)
    
    the_ps = []
    
    for i, line in enumerate(f):
        if i == 0:
            continue
        else:
            fields = line.rstrip("\n\r").split()
            snp = fields[8]
            logp = -1 * np.log10(float(fields[8]))
            the_ps.append(logp)
            
    SNPs_along_chrom = np.array(range(len(the_ps)))
    PVALs = np.array(the_ps)

    greater_than_thresh = PVALs[PVALs > 5]
    less_than_thresh = PVALs[PVALs <= 5]
    greater_SNPs = SNPs_along_chrom[PVALs > 5 ]
    lesser_SNPs = SNPs_along_chrom[PVALs <= 5]

    plt.figure()
    plt.scatter(greater_SNPs,greater_than_thresh, edgecolor ='none', facecolor = 'red')
    plt.scatter(lesser_SNPs,less_than_thresh, edgecolor ='none', facecolor = 'blue')
    plt.title("Manhattan Plot")
    plt.xlabel ("SNP")
    plt.ylabel("-log10(P)")
    plt.axhline(color = 'r',ls = 'dotted')
    plt.savefig("Manhattan_Plot_of" + "_" + str(n))
    n += 1

        

# file = open("plink.P01.qassoc")
# for line in file.readlines():
#     print type(line)
# for file in os.listdir('/Users/cmdb/qbb2016-answers/week5/associations/'):
#     f = open(file)
#     for i, line in enumerate(f):
#         if i == 0:
#             continue
#         else:
#             fields = line.rstrip("\n\r").split()
#             print fields[1]
    # g = np.genfromtxt(f, unpack=True)
    # print g
    # f2 = f.readlines()
 #    print f2
    # for line in f2:
    #     fields = line.rstrip("\\n','").split("\t")
    #     print fields[0]
    # print type(f2)
    # myarray = np.asarray(f2)
    # print myarray[1]
    # for line in f.readlines():q
    #     print fields[0]
#         print fields[2]
#         # print type(fields)
#         # fields = line.rstrip().split("\t")
#         # print fields[1]
    # df = pd.read_table(f,delim_whitespace = True)
    # print df
    # pval = df[[8]]
    # snp = df[[1]]
    # print pval
 #    logp = -1 * np.log10(pval)
 #    new_df = pd.concat([snp,logp], axis=1)
 #    greater_than_thresh = new_df["P"] > 5
 #    less_than_thresh = new_df["P"] < 5
 #    above_thresh = new_df[greater_than_thresh]
 #    below_thresh = new_df[less_than_thresh]
 #    print "Good to go"


