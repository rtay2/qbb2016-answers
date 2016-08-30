#!/usr/bin/env python
 
f = open("mappedreads.sam")

count = 0
for line in f.readlines():
    line = line.rstrip("\r\n")
    if line.startswith("SRR"):
        count += 1
        continue
print count 