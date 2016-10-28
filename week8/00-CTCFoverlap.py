#!/usr/bin/env python

import h5py
import numpy as np
import sys

file = h5py.File("out.heat")
# print file.keys()
counts = file['0.counts'][...]
expected_counts = file['0.expected'][...]
positions = file['0.positions'][...]
regions = file['regions'][...]

start = regions[0][4]
end = regions[0][5]

peak_list = []

for line in open(sys.argv[1]):
    line = line.rstrip("\r\n").split("\t")
    if line[0] == "chrX" and int(line[1]) > start and int(line[1]) < end: 
        peak_list.append(int(line[1]))

where = np.where(counts > 0 )
enrichment = np.empty([1039,1039])
enrichment[where] = np.log(counts[where]/expected_counts[where])


for i in peak_list:
    highest_enriched = 0
    for num, m in enumerate(positions):
        if i > m[0] and i < m[1]:
            for column in range(0,len(positions)):
                if enrichment[num][column] > highest_enriched: 
                    highest_enriched = enrichment[num][column]
                    interactor_pos = positions[column]
            print i, m, interactor_pos, highest_enriched
                    

















