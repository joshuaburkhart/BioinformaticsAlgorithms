# coding=utf-8

import sys
from multiprocessing import Pool

__author__ = 'burkhart'

def max_in_window(transcript_dict, alt_set, window_size):
    max_alt_ps = set()
    #TODO: Use a threadpool to execute this loop
    for transcript in transcript_dict.values():
        sorted_t = sort_t(transcript)
        mt = max_in_sorted_t(sorted_t,alt_set,window_size)
        max_alt_ps = mt if len(mt) > len(max_alt_ps) else max_alt_ps
    return max_alt_ps

def sort_t(transcript):
    print('T',end="")
    sys.stdout.flush()
    exon_idcs = []
    print('adding exons to exon_idcs...')
    for exon in transcript:
        try:
            exon_idcs += list(range(exon[0], exon[1] + 1))
        except IndexError:
            print('exon:{0}'.format(exon))
    print('sorting exon_idcs in case transcript was antisense')
    exon_idcs.sort()
    return exon_idcs

def max_in_sorted_t(exon_idcs,alt_set,window_size):
    max_alt_ps = set()
    print('sliding window over exon_idcs of size {0}...'.format(len(exon_idcs)))
    w_pos = 0
    while(w_pos < len(exon_idcs) - window_size + 1):
        window = range(exon_idcs[w_pos], exon_idcs[w_pos] + window_size)
        print('.',end="")
        sys.stdout.flush()
        print('window:{0}'.format(window))
        first_alt_pos = 0
        p_cntr = w_pos
        cur_alt_ps = set()
        for exon_pos in window:
            p_cntr += 1
            if exon_pos in alt_set:
                cur_alt_ps.add(exon_pos)
                if first_alt_pos == 0:
                    first_alt_pos = p_cntr # just in case we need it later

        if len(cur_alt_ps) == 0:
            if w_pos + window_size < len(exon_idcs) - window_size + 1:
                w_pos += window_size
                print('incrementing by window size..')
            else:
                w_pos = len(exon_idcs) - window_size + 1
                print('overlapping last window..')
        elif len(cur_alt_ps) > len(max_alt_ps):
            print('max_alt_ps:{0}'.format(cur_alt_ps))
            sys.stdout.flush()
            max_alt_ps = cur_alt_ps
            w_pos = first_alt_pos
        else:
            w_pos += first_alt_pos
            print('sliding to first_alt_pos, {0}'.format(first_alt_pos))
    return max_alt_ps