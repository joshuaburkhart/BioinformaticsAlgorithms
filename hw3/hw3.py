import sys

from src.lib.FileConverter import txt_2_alignment
from src.lib.ScoringFunction import entropy
from src.lib.ScoringFunction import sum_of_pairs
from src.lib.ScoringMatrix import blosum_62

__author__ = 'burkhart'
_usage= 'Usage: python hw3.py infile\nExample: python hw3.py hw3.txt'

if len(sys.argv) != 2:
    print(_usage)
    exit()

_infile = sys.argv[1]
_alignment = txt_2_alignment(_infile)
_entropy = _alignment.sum_aligned_char_scores(entropy)
_sum_of_pairs = _alignment.sum_aligned_char_scores(sum_of_pairs,blosum_62)

print("Entropy: {0}".format(_entropy))
print("Sum of Pairs: {0}".format(_sum_of_pairs))
