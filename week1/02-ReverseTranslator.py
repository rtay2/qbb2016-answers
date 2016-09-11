#!/usr/bin/env python
    
import sys
import fasta
import itertools

prot_file = fasta.FASTAReader(open(sys.argv[1]))
nuc_file = fasta.FASTAReader(open(sys.argv[2]))

proteins = []
nts = []

for h in prot_file:
    proteins.append(h)
    
for i in nuc_file:
    nts.append(i)

    
for item in itertools.izip(proteins, nts):
    updated_nseq = []
    n = 0
    prot_seq = item [0][1]
    nuc_seq = item [1][1]
    for amino_acid in prot_seq:
        if amino_acid == "-":
            updated_nseq.append("---")
        else:
            codon = nuc_seq[ n: n+3 ]
            n += 3
            updated_nseq.append(codon)
    print ">" + str(item[0][0])
    print "".join(updated_nseq)

            
            
    

    

    

        
    
    
    
    