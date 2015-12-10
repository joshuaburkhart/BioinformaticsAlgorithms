# coding=utf-8
__author__ = 'burkhart'

def max_in_window(transcript_dict, alt_set, window_size):
    max_alts = 0
    #TODO: Use a threadpool to execute this loop
    for transcript in transcript_dict:
        exon_idcs = []
        for exon in transcript:
            exon_idcs += list(range(exon[0], exon[1] + 1))
        for w_pos in range(0, len(exon_idcs) - window_size + 1):
            window = range(w_pos, w_pos + window_size)
            cur_alts = 0
            for pos in window:
                if pos in alt_set:
                    cur_alts += 1
            if cur_alts > max_alts:
                max_alts = cur_alts
    return max_alts
