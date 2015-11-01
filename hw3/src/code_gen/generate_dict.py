import re
import sys

__author__ = 'burkhart'

_matrix_header = '^[ARNDCQEGHILKMFPSTWYVBZX *]+'
_matrix_data = '^[ARNDCQEGHILKMFPSTWYVBZX*][0-9- ]+'

def matrix_2_dictsource(filename):
    d = {}
    in_fptr = open(filename, 'r')
    while 1:
        line = in_fptr.readline()
        if not line:
            print('0')
            break
        if re.match(_matrix_data,line):
            print('1')
            data = [x for x in line.split(' ') if x]
            for x in range(len(header)):
                d[frozenset([data[0],header[x]])] = float(data[x + 1])
        elif re.match(_matrix_header,line):
            print('2')
            header = [x for x in line.split(' ') if x]
    in_fptr.close()
    return d

print(matrix_2_dictsource(sys.argv[1]))