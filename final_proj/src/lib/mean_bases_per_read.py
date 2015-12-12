
import sys

#Usage: python3 mean_bases_per_read.py ~/input/reads.fasta

_author__ = 'burkhart'

def parse_fastq(fq):
    d = {}
    with open(fq) as FileObj:
        next(FileObj)
        for line in FileObj:
            Ns = line.count('N')
            if Ns in d:
                d[Ns] += 1
            else:
                d[Ns] = 1
                print('Read with {0} Ns detected: {1}'.format(Ns,line.rstrip()))
            next(FileObj)
            next(FileObj)
            next(FileObj)
    print(d)

parse_fastq(sys.argv[1])
