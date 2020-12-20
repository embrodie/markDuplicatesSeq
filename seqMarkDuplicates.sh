#!/bin/bash
# bash seqMarkDuplicates.sh input_file.bam output_file.bam metrics_file.txt
# $1 is the input file, $2 is the output file, $3 is the metrics file
seqc -d markDuplicates.seq $1 $2 $3
python3 writeBam.py $1 $2
