# coding=utf-8
import unittest

from hw3.src.lib.Alignment import MultipleAlignment
from hw3.src.lib.ScoringFunction import sum_of_pairs
from hw3.src.lib.ScoringFunction import entropy
from hw3.src.lib.ScoringMatrix import blosum_62

__author__ = 'burkhart'

SUM_ALIGN_EPSILON = 0.1


class TestAlignment(unittest.TestCase):
    def setUp(self):
        self._alignment = MultipleAlignment()

    def as_helper(self, seq):
        self._alignment.add_sequence(seq)

        self.assertEqual(len(self._alignment.sequence_matrix), len(seq))
        self.assertEqual(len(self._alignment.sequence_matrix[0]), 1)
        self.assertEqual(''.join(self._alignment.sequence_matrix), seq)

    def ss_entropy_helper(self, expect):
        actual = self._alignment.sum_aligned_char_scores(entropy)
        self.assertLess(abs(actual - expect), SUM_ALIGN_EPSILON,
                        "Incorrect sum of entropy scores: {0} "
                        "(expected {1} to be within {2})".format(
                            actual,
                            expect,
                            SUM_ALIGN_EPSILON))

    def ss_sp_helper(self, expect, matrix_wrapper):
        actual = self._alignment.sum_aligned_char_scores(sum_of_pairs, matrix_wrapper)
        self.assertLess(abs(actual - expect), SUM_ALIGN_EPSILON,
                        "Incorrect sum of SP scores: {0} "
                        "(expected {1} to be within {2})".format(
                            actual,
                            expect,
                            SUM_ALIGN_EPSILON))

    def test_add_sequence_1(self):
        self.as_helper('KMFPSTWY')

    def test_add_sequence_2(self):
        self.as_helper('K')

    def test_add_sequence_3(self):
        self.as_helper('KMFP----')

    def test_add_sequence_4(self):
        self.as_helper('---PSTWY')

    def test_add_sequence_5(self):
        self.as_helper('------')

    def test_add_sequence_6(self):
        self.as_helper('-')

    def test_add_sequences_1(self):
        seq_1 = 'BZXBZA'
        seq_2 = 'TTTT'
        seq_3 = 'XAXAXAXA'

        self._alignment.add_sequence(seq_1)
        self._alignment.add_sequence(seq_2)
        self._alignment.add_sequence(seq_3)

        self.assertEqual(len(self._alignment.sequence_matrix), len(seq_3))

        self.assertEqual(len(self._alignment.sequence_matrix[0]), 3)
        self.assertEqual(len(self._alignment.sequence_matrix[1]), 3)
        self.assertEqual(len(self._alignment.sequence_matrix[2]), 3)

        self.assertEqual(self._alignment.sequence_matrix[0], 'BTX')
        self.assertEqual(self._alignment.sequence_matrix[1], 'ZTA')
        self.assertEqual(self._alignment.sequence_matrix[2], 'XTX')

    def test_add_sequences_2(self):
        seq_1 = '-RRRRRRRRRRRRWWWWWWWWWWWWWWW-'
        seq_2 = '----------T---------'
        seq_3 = 'XZXZXZXZXZ------XZXZXZXZX'

        self._alignment.add_sequence(seq_1)
        self._alignment.add_sequence(seq_2)
        self._alignment.add_sequence(seq_3)

        self.assertEqual(len(self._alignment.sequence_matrix), len(seq_1))

        self.assertEqual(len(self._alignment.sequence_matrix[0]), 3)
        self.assertEqual(len(self._alignment.sequence_matrix[1]), 3)
        self.assertEqual(len(self._alignment.sequence_matrix[2]), 3)

        self.assertEqual(self._alignment.sequence_matrix[0], '--X')
        self.assertEqual(self._alignment.sequence_matrix[1], 'R-Z')
        self.assertEqual(self._alignment.sequence_matrix[2], 'R-X')

    def test_add_sequences_3(self):
        seq_1 = 'A'
        seq_2 = 'BB'
        seq_3 = 'CCC'
        seq_4 = 'DDDD'
        seq_5 = 'EEEEE'
        seq_6 = 'FFFFFF'

        self._alignment.add_sequence(seq_1)
        self._alignment.add_sequence(seq_2)
        self._alignment.add_sequence(seq_3)
        self._alignment.add_sequence(seq_4)
        self._alignment.add_sequence(seq_5)
        self._alignment.add_sequence(seq_6)

        self.assertEqual(len(self._alignment.sequence_matrix), len(seq_6))

        self.assertEqual(len(self._alignment.sequence_matrix[0]), 6)
        self.assertEqual(len(self._alignment.sequence_matrix[1]), 5)
        self.assertEqual(len(self._alignment.sequence_matrix[2]), 4)
        self.assertEqual(len(self._alignment.sequence_matrix[3]), 3)
        self.assertEqual(len(self._alignment.sequence_matrix[4]), 2)
        self.assertEqual(len(self._alignment.sequence_matrix[5]), 1)

        self.assertEqual(self._alignment.sequence_matrix[0], 'ABCDEF')
        self.assertEqual(self._alignment.sequence_matrix[1], 'BCDEF')
        self.assertEqual(self._alignment.sequence_matrix[2], 'CDEF')
        self.assertEqual(self._alignment.sequence_matrix[3], 'DEF')
        self.assertEqual(self._alignment.sequence_matrix[4], 'EF')
        self.assertEqual(self._alignment.sequence_matrix[5], 'F')

    def test_sum_aligned_char_scores_1(self):
        seq_1 = 'TWYV'
        seq_2 = 'AWYA'

        self._alignment.add_sequence(seq_1)
        self._alignment.add_sequence(seq_2)

        # -(-1 + 0 + 0 + -1)
        self.ss_entropy_helper(2.0)

        # 0 + 11 + 7 + 0
        self.ss_sp_helper(18.0, blosum_62)

    def test_sum_aligned_char_scores_2(self):
        seq_1 = 'TWYV'
        seq_2 = 'AW--'

        self._alignment.add_sequence(seq_1)
        self._alignment.add_sequence(seq_2)

        # -(-1 + 0 + 0 + 0)
        self.ss_entropy_helper(1.0)

        # 0 + 11 + 0 + 0
        self.ss_sp_helper(11.0, blosum_62)

    def test_sum_aligned_char_scores_3(self):
        seq_1 = 'ZWBB'
        seq_2 = 'ZWWB'
        seq_3 = 'ZWBW'

        self._alignment.add_sequence(seq_1)
        self._alignment.add_sequence(seq_2)
        self._alignment.add_sequence(seq_3)

        # -(0 + 0 + -(2/3 * log(2/3,2) + 1/3 * log(1/3,2)) + -(2/3 * log(2/3,2) + 1/3 * log(1/3,2))
        self.ss_entropy_helper(1.8)

        # 4 + 4 + 4 + 11 + 11 + 11 + -4 + 4 + -4 + 4 + -4 + -4
        self.ss_sp_helper(37.0, blosum_62)

    def test_sum_aligned_char_scores_4(self):
        seq_1 = 'ZWBB'
        seq_2 = 'ZW--'
        seq_3 = 'ZW--'

        self._alignment.add_sequence(seq_1)
        self._alignment.add_sequence(seq_2)
        self._alignment.add_sequence(seq_3)

        # -(0 + 0 + 0 + 0)
        self.ss_entropy_helper(0.0)

        # 4 + 4 + 4 + 11 + 11 + 11 + 0 + 0 + 0 + 0 + 0 + 0
        self.ss_sp_helper(45.0, blosum_62)

    def test_SOURCE_STABALIZER_sum_aligned_char_scores_1(self):
        seq_1 = 'ZWBB'
        seq_2 = 'ZWWB'
        seq_3 = 'ZWBW'
        seq_4 = 'ZWBB'
        seq_5 = 'ZWWB'
        seq_6 = 'ZWBW'

        self._alignment.add_sequence(seq_1)
        self._alignment.add_sequence(seq_2)
        self._alignment.add_sequence(seq_3)
        self._alignment.add_sequence(seq_4)
        self._alignment.add_sequence(seq_5)
        self._alignment.add_sequence(seq_6)

        self.ss_entropy_helper(1.8)
        self.ss_sp_helper(231.0, blosum_62)

    def test_SOURCE_STABALIZER_sum_aligned_char_scores_2(self):
        seq_1 = 'ZWBB'
        seq_2 = 'ZW--'
        seq_3 = 'ZW--'
        seq_4 = 'ZWBB'
        seq_5 = 'ZW--'
        seq_6 = 'ZW--'

        self._alignment.add_sequence(seq_1)
        self._alignment.add_sequence(seq_2)
        self._alignment.add_sequence(seq_3)
        self._alignment.add_sequence(seq_4)
        self._alignment.add_sequence(seq_5)
        self._alignment.add_sequence(seq_6)

        self.ss_entropy_helper(0.0)
        self.ss_sp_helper(225.0, blosum_62)


if __name__ == '__main__':
    unittest.main()
