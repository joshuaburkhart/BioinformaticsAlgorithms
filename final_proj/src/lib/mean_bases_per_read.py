
import sys

#Usage: python3 mean_bases_per_read.py ~/input/reads.fasta

_author__ = 'burkhart'

def parse_fastq(fq):
    d = {}
    with open(fq) as FileObj:
        next(FileObj)
        read_cnt = 0
        for line in FileObj:
            Ns = line.count('N')
            read_cnt += 1
            if Ns in d:
                d[Ns] += 1
            else:
                d[Ns] = 1
                print('Read with {0} Ns detected: {1}'.format(Ns,line.rstrip()))
            try:
                next(FileObj)
                next(FileObj)
                next(FileObj)
            except StopIteration:
                break
    print(d)
    print('read_cnt: {0}'.format(read_cnt))


parse_fastq(sys.argv[1])
