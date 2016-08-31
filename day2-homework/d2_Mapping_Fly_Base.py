#!/usr/bin/env python

import sys
f = open(sys.argv[1])
    
for line in f: 
    if "DROME" in line:
        fields = line.rstrip("\r\n").split()
        if len(fields) == 4:
            print fields[2], "\t", fields[3]
        ## else:
        ##    print
        
