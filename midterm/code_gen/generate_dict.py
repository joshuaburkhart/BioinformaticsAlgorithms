# coding=utf-8
import re
import sys

#Ex: $ python3 generate_dict.py BLOSUM62.txt | pbcopy


__author__ = 'burkhart'

_matrix_header = '^[ARNDCQEGHILKMFPSTWYVBZX *]+'
_matrix_data = '^[ARNDCQEGHILKMFPSTWYVBZX*][0-9- ]+'


def matrix_2_dictsource(filename):
    """
    ripped out of FileConverter.py
    :param filename:
    :return:
    """
    d = {}
    in_fptr = open(filename)
    while 1:
        line = in_fptr.readline()
        if not line:
            break
        if re.match(_matrix_data, line):
            data = [x for x in line.split(' ') if x]
            for x in range(len(header)):
                d[frozenset([data[0].strip(), header[x].strip()])] = float(data[x + 1])
        elif re.match(_matrix_header, line):
            header = [x for x in line.split(' ') if x]
    in_fptr.close()
    return d


print(matrix_2_dictsource(sys.argv[1]))
