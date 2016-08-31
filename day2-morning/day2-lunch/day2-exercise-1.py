#!/usr/bin/env python
 
## SRR method will give you 'unaligned alignments' 
import sys
f = open(sys.argv[1])

count = 0
for line in f.readlines():
    line = line.rstrip("\r\n")
    if line.startswith("SRR"):
        count += 1
        continue
print count 