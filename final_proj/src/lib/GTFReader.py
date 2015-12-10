# coding=utf-8

import re

__author__ = 'burkhart'

_exon_locus_and_transcript = '.+?\b.+?\bexon\b.*?(?P<start>[0-9]+)\b.*?(?P<end>[0-9]+)\b.*?transcript_id\s\"(?P<tid>[A-Z0-9]+)\"'

def parse_transcripts(gtf_filename):
    d = {}
    in_fptr = open(gtf_filename)
    while 1:
        line = in_fptr.readline()
        if not line:
            break
        m = re.match(_exon_locus_and_transcript, line)
        if m:
            s = m.group('start')
            e = m.group('end')
            t = m.group('tid')
            print('s:{0}, e:{1}, t:{2}'.format(s,e,t))
            if(t in d):
                d[t].append((s,e))
            else:
                d[t] = [(s,e)]
    in_fptr.close()
    return d