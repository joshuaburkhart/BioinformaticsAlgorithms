import re

__author__ = 'burkhart'

MTRIX_HEAD_RGX = '^[ARNDCQEGHILKMFPSTWYVBZX *]+'
MTRIX_DATA_RGX = '^[ARNDCQEGHILKMFPSTWYVBZX*][0-9- ]+'
ALIGND_SEQ_RGX = '^[ARNDCQEGHILKMFPSTWYVBZX-]+'


def add_alignments_from_txt(filename,alignment):
    in_fptr = open(filename, 'r')
    while 1:
        line = in_fptr.readline()
        if not line:
            break
        if re.match(ALIGND_SEQ_RGX,line):
            alignment.add_sequence(line.rstrip())
    in_fptr.close()


def matrix_2_dictsource(filename):
    d = {}
    in_fptr = open(filename, 'r')
    while 1:
        line = in_fptr.readline()
        if not line:
            break
        if re.match(MTRIX_DATA_RGX,line):
            data = [x for x in line.split(' ') if x]
            for x in range(len(header)):
                d[frozenset([data[0],header[x]])] = float(data[x + 1])
        elif re.match(MTRIX_HEAD_RGX,line):
            header = [x for x in line.split(' ') if x]
    in_fptr.close()
    return d