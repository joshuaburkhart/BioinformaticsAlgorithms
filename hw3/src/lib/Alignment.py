__author__ = 'burkhart'

ILLEGAL_CHARS = '-\n'

class MultipleAlignment:

    def __init__(self):
        self.sequence_matrix = []

    def add_sequence(self,sequence):
        for idx,char in enumerate(sequence):
            if idx < len(self.sequence_matrix):
                self.sequence_matrix[idx] += char
            else:
                self.sequence_matrix.append(char)

    def sum_aligned_char_scores(self,scoring_function,*sf_args):
        sum = 0.0
        for aligned_chars in self.sequence_matrix:
            if all(char not in ILLEGAL_CHARS for char in aligned_chars):
                sum += scoring_function(aligned_chars,sf_args)
        return sum

    def minimize_aligned_char_scores(self,scoring_function,*sf_args):
        score_list = []
        for aligned_chars in self.sequence_matrix:
            score_list.append(scoring_function(aligned_chars,sf_args))
        return min(score_list)