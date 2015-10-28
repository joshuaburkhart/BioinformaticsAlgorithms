__author__ = 'burkhart'


class Alignment(object):

    def __init__(self,alphabet):
        self.alphabet = alphabet
        self.sequence_matrix = []

    def add_sequence(self,sequence):
        if all(self.alphabet.contains(char) for char in sequence):
            for idx,char in enumerate(sequence):
                if idx < len(self.sequence_matrix):
                    self.sequence_matrix[idx] += char
                else:
                    self.sequence_matrix.append(char)
        else:
            raise ValueError("Not all characters in sequence found in alphabet")

    def sum_aligned_char_scores(self,scoring_function):
        sum = 0
        for aligned_chars in self.sequence_matrix:
            sum += scoring_function(aligned_chars)
        return sum
