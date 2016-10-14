#!/usr/bin/env python

import sys
import pandas as pd

file = open(sys.argv[1])
for line in file.readlines():
    fields = line.rstrip(" ").split("\t")
    print fields[0]+"\t"+fields[1]+"\t"+fields[2]+ "\t"+fields[3]+"\t"+fields[4]+"\t"+fields[5]