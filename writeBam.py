import pysam
import sys
import os

in_file = str(sys.argv[1])
outfile_name = str(sys.argv[2]) if sys.argv[2] else "marked_dups.bam"

list_dups = open("list_dups_"+in_file+".txt", "r")
dup_reads = list_dups.read().split("\n")
list_dups.close()

orig_bamfile = pysam.AlignmentFile(in_file, "rb")
outfile = pysam.AlignmentFile(outfile_name, "wb", template=orig_bamfile)

for read in orig_bamfile.fetch():
	if read.query_name in dup_reads:
		read.flag = read.flag + 1024
	outfile.write(read)

orig_bamfile.close()
outfile.close()

os.remove("list_dups_"+in_file+".txt")

print("writing file done")