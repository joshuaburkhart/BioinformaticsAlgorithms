import sys

from src.lib.FileConverter import txt_2_alignment
from src.lib.ScoringFunction import entropy
from src.lib.ScoringFunction import sum_of_pairs
from src.lib.ScoringMatrix import blosum_62

__author__ = 'burkhart'
_usage = 'Usage: python hw3.py infile\nExample: python hw3.py hw3.txt'

if len(sys.argv) != 2:
    print(_usage)
    exit()


def print_entropy_and_sop(infile):
    alignment = txt_2_alignment(infile)

    print("Entropy: {0}".format(
        round(
            alignment.sum_aligned_char_scores(entropy),
            3)))

    print("Minimum Entropy: {0}".format(
        round(
            alignment.minimize_aligned_char_scores(entropy),
            3)))

    print("Sum of Pairs: {0}".format(
        round(
            alignment.sum_aligned_char_scores(sum_of_pairs, blosum_62),
            3)))

print_entropy_and_sop(sys.argv[1])
