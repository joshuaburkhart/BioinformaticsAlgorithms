# coding=utf-8

import sys
from multiprocessing import Pool

__author__ = 'burkhart'

def max_in_window(transcript_dict, alt_set, window_size):
    max_alts = 0
    #TODO: Use a threadpool to execute this loop
    for transcript in transcript_dict.values():
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
        print('sliding window over exon_idcs of size {0}...'.format(len(exon_idcs)))
        w_pos = 0
        while(w_pos < len(exon_idcs) - window_size + 1):
            window = range(exon_idcs[w_pos], exon_idcs[w_pos] + window_size)
            print('.',end="")
            sys.stdout.flush()
            print('window:{0}'.format(window))
            first_alt_pos = w_pos
            cur_alts = 0
            for exon_pos in window:
                if exon_pos in alt_set:
                    cur_alts += 1
                first_alt_pos += 1 # just in case we need it later
            if cur_alts == 0:
                if w_pos + window_size < len(exon_idcs) - window_size + 1:
                    w_pos += window_size
                else:
                    w_pos = len(exon_idcs) - window_size + 1
            elif cur_alts > max_alts:
                print('max_alts set to {0}'.format(max_alts))
                sys.stdout.flush()
                max_alts = cur_alts
                w_pos = first_alt_pos
    return max_alts
