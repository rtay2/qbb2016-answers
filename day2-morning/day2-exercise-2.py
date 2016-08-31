#!/usr/bin/env python

import sys
f = open("mappedreads.sam")

count = 0
for line in f.readlines():
    if "NM:i:0" in line:
        count += 1 
print count 