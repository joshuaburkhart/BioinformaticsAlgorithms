import re
import math

_fastq_data = '[ATCGNatcgn]+'
_char_cnts = {}
_len = 0

def parse_fastq(fastq_filename):
    global _char_cnts
    global _len
    in_fptr = open(fastq_filename)
    while 1:
        line = in_fptr.readline()
        if not line:
            break
        if re.match(_fastq_data, line):
            for char in line:
                if char in 'ATCGatcg':
                    if char.upper() in _char_cnts:
                        _char_cnts[char.upper()] += 1
                    else:
                        _char_cnts[char.upper()] = 1
            _len += 1
    in_fptr.close()

def pct_read_chr_cnt(char):
    if char.upper() in _char_cnts:
        return float(_char_cnts[char.upper()]) / float(_len)
    else:
        return 0

def read_char_entropy():
    e = 0
    for char_cnt in _char_cnts.values():
        prob = float(char_cnt)/float(_len)
        e += -(prob * math.log2(prob)) * char_cnt