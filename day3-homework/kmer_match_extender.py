#!/usr/bin/env python

import sys, fasta

k = int(sys.argv[1])
query_file = open(sys.argv[2])
target_file = open(sys.argv[3])

kmer_hash = {}

for identifier, sequence1 in fasta.FASTAReader(query_file):
    sequence1 = sequence1.upper()
    for i in range(0,len(sequence1) - k):
        start = i
        end = i + k
        kmer = sequence1[i:i+k]
        if kmer not in kmer_hash:
            kmer_hash[kmer]= [start] 
        else:
            kmer_hash[kmer].append(start)

box_of_matches = []

for seq_name, sequence2 in fasta.FASTAReader(target_file):
    sequence2 = sequence2.upper()
    target_seq_kmer = {}
    file_one_output =[]
    for g, i in enumerate(range(0,len(sequence2) - k)):
        i = i
        j = i + k
        kmer = sequence2[i:i+k]
        if kmer in kmer_hash:
           for start in kmer_hash[kmer]:
               end = start + k
               n = 1
               w = 1
               while True:
                   if sequence2[i-n] == sequence1[start-n]:
                       n += 1
                   elif i-n == -1 or start-n == -1:
                       break
                   else:
                       break
               n -= 1
               while True:
                   if j+w == len(sequence2) or end+w == len(sequence1):
                       break
                   if sequence2[j+w] == sequence1[end+w]:
                       w += 1
                   else:
                       break
                       
               match = sequence2[i-n+1:j+w]
               box_of_matches.append(match)
               
box_of_matches.sort( reverse=True, key=len )
            
for match in box_of_matches[:1000]:
    print match

            
        
        
        

        
