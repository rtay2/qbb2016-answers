#!/usr/bin/env python

import sys
import pandas as pd

file = open(sys.argv[1], 'r')
for line in file.readlines():
    if line.startswith("A"):
        line = line.replace('_', '\t')
        print line
    else:
        print line

# plink2 --assoc --vcf <file> --pheno <file> --allow-no-sex