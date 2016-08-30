#!/usr/bin/env python

f = open("mappedreads.sam")

count = 0 
for line in f.readlines():
    if line.startswith("SRR"):
        print line.split("\t")[2]
        count += 1
        if count == 10:
            break 

    