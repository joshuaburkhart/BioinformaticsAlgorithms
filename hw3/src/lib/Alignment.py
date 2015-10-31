__author__ = 'burkhart'


class Alignment:

    def __init__(self):
        self.sequence_matrix = []

    def add_sequence(self,sequence):
        for idx,char in enumerate(sequence):
            if idx < len(self.sequence_matrix):
                self.sequence_matrix[idx] += char
            else:
                self.sequence_matrix.append(char)

    def sum_aligned_char_scores(self,scoring_function,*sf_args):
        sum = 0
        for aligned_chars in self.sequence_matrix:
            sum += scoring_function(aligned_chars,sf_args)
        return sum
