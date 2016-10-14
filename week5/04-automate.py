#!/usr/bin/env python

import sys 


the_heads = []
file = open(sys.argv[1])
first = file.readline()
column_headers = first.rstrip().split('\t')
for i in column_headers:
    the_heads.append(i)
print the_heads

