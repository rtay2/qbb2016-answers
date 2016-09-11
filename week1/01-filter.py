#!/usr/bin/env python

import sys
import string

nuc = open(sys.argv[1])

count = 0

abbrev = ["W", "K", "R", "Y", "S", "N"]

for line in nuc:
    fields = line.rstrip("\r\n").split("\t")
    q_start = fields[0]
    q_end = fields[1]
    seq = fields[2]
    if q_start != "1" or q_end != "10293":
        continue
    else:
        if "-" in line: 
            no_gaps = line.replace("-", "")
            # no_gaps = no_gaps.replace("R","A")
            # no_gaps = no_gaps.replace("Y","T")
            no_gaps_fields = no_gaps.rstrip("\r\n").split("\t")
            print ">" + str(count) + "\n" + no_gaps_fields[2]
            count += 1
        else:
            # no_gaps = line.replace("R","A")
            # no_gaps = no_gaps.replace("Y","T")
            # no_gaps_fields = no_gaps.rstrip("\r\n").split("\t")
            print ">" + str(count) + "\n" + seq
            count += 1
                
        # if "W" or "K" or "R" or "Y" or "S" or "N" in line:
        #     continue
            
            
        
            
            
    