#!/bin/bash
# $1 is the input file, $2 is the output file, $3 is the metrics file
# echo $3
seqc -d markDuplicates.seq $1 $2 $3
python3 writeBam.py $1 $2