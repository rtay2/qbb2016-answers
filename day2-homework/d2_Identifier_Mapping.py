#!/usr/bin/env python

'''Takes three arguments(full output file from mapping file, ctab file in other directory to be matched against the dictionary, option as either "Ignore" or "Default" on whether ctab lines with no fly id match should be ignored or the line read with a * in place of the uni id). 
'''

import sys

mapping_file = open("full_output.txt")

dict1={}
for line in mapping_file.readlines():
    fields = line.rstrip("\r\n").split("\t")
    fly_id = fields[1]
    uni_id = fields[0]
    dict1[fly_id]=uni_id

our_data_ctab = open(sys.argv[1])

option = sys.argv[2]

for line in our_data_ctab.readlines():
    line=line.strip()
    cols = line.split("\t")
    ctab_FBg = cols[8]
    if ctab_FBg in dict1:
        print line+'\t'+dict1[ctab_FBg]
    else:
        if option == "Ignore":
            continue
        elif option == "Default":
            print line+"\t"+"*"
            
    
            
            
        
