
import sys

__author__ = 'burkhart'

#Usage: python3 mean_bases_per_read.py ~/input/reads.fasta

def parse_fastq(fq):
    d = {}
    with open(fq) as FileObj:
        for line in FileObj[2:]:
            Ns = line.count('N')
            if Ns in d:
                d[Ns] += 1
            else:
                d[Ns] = 1
    print(d)

parse_fastq(sys.argv[1])
