# coding=utf-8

import re

__author__ = 'burkhart'

_alt_data = '[0-9]+?\s+(?P<locus>[0-9]+)'

def parse_alternates(vcf_filename):
    s = set()
    in_fptr = open(vcf_filename)
    while 1:
        line = in_fptr.readline()
        if not line:
            break
        m = re.match(_alt_data, line)
        if m:
            s.add(int(m.group('locus')))
    in_fptr.close()
    return s
