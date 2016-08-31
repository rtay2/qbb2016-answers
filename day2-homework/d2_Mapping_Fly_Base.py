#!/usr/bin/env python

f = open("fly.txt")
    
for line in f: 
    if "DROME" in line:
        fields = line.split()
        if len(fields) == 4:
            print fields[2], "\t", fields[3]
        
    

        