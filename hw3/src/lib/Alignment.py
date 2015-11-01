# coding=utf-8
__author__ = 'burkhart'

ILLEGAL_CHARS = '-\n'


class MultipleAlignment:
    """
    represents a simple multiple alignment
    """

    def __init__(self):
        self.sequence_matrix = []

    def add_sequence(self, sequence):
        """
        adds sequence characters to matrix, appending
        to existing values such that aligned characters
        will end up occupying the same index
        ex:
        'ZWAB'
        'B-ZX'
        will end up as
        ['ZB','W-','AZ','BX']
        :param sequence:
        """
        for idx, char in enumerate(sequence):
            if idx < len(self.sequence_matrix):
                self.sequence_matrix[idx] += char
            else:
                self.sequence_matrix.append(char)

    def sum_aligned_char_scores(self, scoring_function, *sf_args):
        """
        addition commutes. aligned characters of matrix
        are summed, simulating the summation of whichever
        scoring function
        :param scoring_function:
        :param sf_args:
        :return:
        """
        score_sum = 0.0
        for aligned_chars in self.sequence_matrix:
            if all(char not in ILLEGAL_CHARS for char in aligned_chars):
                score_sum += scoring_function(aligned_chars, sf_args)
        return score_sum

    def minimize_aligned_char_scores(self, scoring_function, *sf_args):
        """
        returns the minimum value returned by the
        scoring function for aligned characters
        :param scoring_function:
        :param sf_args:
        :return:
        """
        score_list = []
        for aligned_chars in self.sequence_matrix:
            score_list.append(scoring_function(aligned_chars, sf_args))
        return min(score_list)
