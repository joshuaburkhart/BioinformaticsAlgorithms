__author__ = 'burkhart'

import math


def entropy(aligned_chars,param_tuple):
    """Entropy
    Compeau, P, Pevzner, P,c Active Learning Publishers,
    Bioinformatics Algorithms: An Active Learning Approach,
    2nd Ed., Vol. I, p. 76
    """
    e = 0.0
    for i in ''.join(set(aligned_chars)):
        p = float(aligned_chars.count(i)) / len(aligned_chars)
        if p > 0:
            e += p * math.log(p, 2)
    return -e + 0 #trick from http://goo.gl/8u8kQw


def sum_of_pairs(aligned_chars,param_tuple):
    """Sum-of-Pairs (SP-score)
    Compeau, P, Pevzner, P,c Active Learning Publishers,
    Bioinformatics Algorithms: An Active Learning Approach,
    2nd Ed., Vol. I, p. 290
    """
    matrix_wrapper = param_tuple[0]
    sp = 0.0
    for i in range(0,len(aligned_chars)):
        for j in range(i + 1,len(aligned_chars)):
            sp += matrix_wrapper(aligned_chars[i], aligned_chars[j])
    return sp + 0 #trick from http://goo.gl/8u8kQw
