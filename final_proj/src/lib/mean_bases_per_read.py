
import sys

#Usage: python3 mean_bases_per_read.py ~/input/reads.fasta

_author__ = 'burkhart'

def parse_fastq(fq):
    d = {}
    with open(fq) as FileObj:
        for line in FileObj:
            next(FileObj)
            Ns = line.count('N')
            if Ns in d:
                d[Ns] += 1
            else:
                d[Ns] = 1
            next(FileObj)
            next(FileObj)
    print(d)

parse_fastq(sys.argv[1])
