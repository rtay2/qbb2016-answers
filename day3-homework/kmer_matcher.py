#!/usr/bin/env python

import sys, fasta

k = int(sys.argv[1])
query_file = open(sys.argv[2])
target_file = open(sys.argv[3])

for identifier, sequence in fasta.FASTAReader(query_file):
    sequence = sequence.upper()
    kmer_hash = {}
    for i in range(0,len(sequence) - k):
        start = i
        end = i + k
        kmer = sequence[i:i+k]
        if kmer not in kmer_hash:
            kmer_hash[kmer]= [start] 
        else:
            kmer_hash[kmer].append(start)
        
for seq_name, sequence in fasta.FASTAReader(target_file):
    sequence = sequence.upper()
    target_seq_kmer = {}
    for g, i in enumerate(range(0,len(sequence) - k)):
        start = i
        end = i + k
        kmer = sequence[i:i+k]
        if kmer in kmer_hash:
            print seq_name, start, kmer_hash[kmer], kmer
        if g > 1000:
            break


            
        
        
        

        
