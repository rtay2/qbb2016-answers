#!/usr/bin/env bash

./00-d5-lunch.py ~/data/results/stringtie/SRR072893/t_data.ctab > promoter.bed
for i in *.bw
do
	bigWigAverageOverBed -bedOut=${i%bw}bed $i promoter.bed ${i%bw}tab
done
rm *.tab
./01-d5-lunch.py *3.bed > lin_reg_output.txt
