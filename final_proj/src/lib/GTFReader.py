# coding=utf-8

import re

__author__ = 'burkhart'

#TODO: make this regex faster.. maybe replace .+? with \w
_exon_locus_and_transcript = '.+?\t.+?\texon\t(?P<start>[0-9]+)\t(?P<end>[0-9]+)\t.+?\t.+?\t.+?\t.*?transcript_id\s\"(?P<tid>[A-Z0-9]+)\"'


def parse_transcripts(gtf_filename):
    d = {}
    in_fptr = open(gtf_filename)
    while 1:
        line = in_fptr.readline()
        if not line:
            break
        m = re.match(_exon_locus_and_transcript, line)
        if m:
            s = int(m.group('start'))
            e = int(m.group('end'))
            t = m.group('tid')
            if(t in d):
                d[t].append((s,e))
            else:
                d[t] = [(s,e)]
    in_fptr.close()
    return d
