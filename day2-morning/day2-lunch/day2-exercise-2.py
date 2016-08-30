#!/usr/bin/env python

f = open("mappedreads.sam")

count = 0
for line in f.readlines():
    if "XM:i:0" in line:
        count += 1 
print count 