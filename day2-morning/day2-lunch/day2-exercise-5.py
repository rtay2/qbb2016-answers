#!/usr/bin/env python

f = open("mappedreads.sam")

count = 0 
final_total = 0 

for line in f:
    if line.startswith("SRR"):
        count += 1
        if line.split("\t")[4]!= "255":
            running_total = int(line.split("\t")[4])
            final_total = final_total + running_total
            
print final_total/count 
            


    