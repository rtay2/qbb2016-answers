#!/usr/bin/env python

## Give file location data/day1/mappedreads

import sys
f = open(sys.argv[1])

count = 0 
for line in f.readlines():
    if line.startswith("SRR"):
        if line.split("\t")[2] != "*":
            print line.split("\t")[2]
            count += 1
            if count == 11:
                break 

    