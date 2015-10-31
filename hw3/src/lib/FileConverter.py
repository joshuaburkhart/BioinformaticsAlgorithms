import re
from src.lib.Alignment import Alignment

__author__ = 'burkhart'

_matrix_header = '^[ARNDCQEGHILKMFPSTWYVBZX *]+'
_matrix_data = '^[ARNDCQEGHILKMFPSTWYVBZX*][0-9- ]+'
_aligned_seq = '^[ARNDCQEGHILKMFPSTWYVBZX-]+'


def txt_2_alignment(filename):
    a = Alignment()
    in_fptr = open(filename, 'r')
    while 1:
        line = in_fptr.readline()
        if not line:
            break
        if re.match(_aligned_seq,line):
            a.add_sequence(line)
    in_fptr.close()
    return a


def matrix_2_dictsource(filename):
    d = {}
    in_fptr = open(filename, 'r')
    while 1:
        line = in_fptr.readline()
        if not line:
            break
        if re.match(_matrix_data,line):
            data = [x for x in line.split(' ') if x]
            for x in range(len(header)):
                d[frozenset([data[0],header[x]])] = float(data[x + 1])
        elif re.match(_matrix_header,line):
            header = [x for x in line.split(' ') if x]
    in_fptr.close()
    return d