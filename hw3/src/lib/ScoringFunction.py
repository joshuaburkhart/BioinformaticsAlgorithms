__author__ = 'burkhart'

import math

def entropy(aligned_chars):
    """Entropy
    Compeau, P, Pevzner, P,c Active Learning Publishers,
    Bioinformatics Algorithms: An Active Learning Approach,
    2nd Ed., Vol. I, p. 76
    """
    e = 0
    for i in aligned_chars:
        p = float(aligned_chars.count(i))/len(aligned_chars)
        if p > 0:
            e += p * math.log(p,2)
    return -e

class Blosum62:

    def __init__(self):
        pass

    @staticmethod
    def sum_of_pairs(aligned_chars):
        """Sum-of-Pairs (SP-score)
        Compeau, P, Pevzner, P,c Active Learning Publishers,
        Bioinformatics Algorithms: An Active Learning Approach,
        2nd Ed., Vol. I, p. 290
        """
        sp = 0
        for i in range[0:len(aligned_chars)]:
            for j in range[i+1:len(aligned_chars)]:
                sp += Blosum62.s(aligned_chars[i],aligned_chars[j])
        return sp

    @staticmethod
    def s(char_i,char_j):
        pass