#!/usr/bin/env python

import sys
import fasta
import itertools

nuc_search = fasta.FASTAReader(open(sys.argv[1]))

codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', '---':'*'
    }

ref = []
dS_of_hits = []
dN_of_hits = []

for identifier, sequence in nuc_search:
    print identifier
    if identifier == "0_1":
        for codon in range(0,len(sequence),3):
            codon_temp = sequence[codon:codon+ 3]
            aa = codontable.get(codon_temp)
            ref.append(aa)
    else:
        dS = 0
        dN = 0
        hprot_seq = []
        for codon in range(0,len(sequence),3):
            hits_codon = sequence[codon:codon + 3]
            aa = codontable[hits_codon]
            hprot_seq.append(aa)
        for i in range(len(hprot_seq)):
            q_aa = ref[i]
            h_aa = hprot_seq[i]
            print q_aa, h_aa
            if q_aa == h_aa:
                dS += 1
            else:
                dN += 1
        print dS, dN
            # dS_of_hits.append(dS)
            # dN_of_hits.append(dN)


# print "".join(hprot_seq)
# print "".join(ref)


                


    