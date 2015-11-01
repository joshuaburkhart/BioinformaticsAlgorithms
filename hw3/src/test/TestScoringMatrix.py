# coding=utf-8
import unittest

from hw3.src.lib.ScoringMatrix import blosum_62

__author__ = 'burkhart'


class TestScoringMatrix(unittest.TestCase):
    def tb_helper(self, char_i, char_j, expect):
        actual = blosum_62(char_i, char_j)
        self.assertEqual(actual, expect,
                         "Score for {0} was {1} but expected {2}".format(
                             [char_i, char_j],
                             actual,
                             expect
                         ))

    def test_blosum_62_AA(self):
        """http://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt
        AA = 4
        """
        self.tb_helper('A', 'A', 4)

    def test_blosum_62_AR(self):
        """http://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt
        AR = -1
        """
        self.tb_helper('A', 'R', -1)

    def test_blosum_62_AN(self):
        """http://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt
        AN = -2
        """
        self.tb_helper('A', 'N', -2)

    def test_blosum_62_AD(self):
        """http://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt
        AD = -2
        """
        self.tb_helper('A', 'D', -2)

    def test_blosum_62_AC(self):
        """http://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt
        AC = 0
        """
        self.tb_helper('A', 'C', 0)

    def test_blosum_62_AQ(self):
        """http://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt
        AQ = -1
        """
        self.tb_helper('A', 'Q', -1)

    def test_blosum_62_AE(self):
        """http://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt
        AE = -1
        """
        self.tb_helper('A', 'E', -1)

    def test_blosum_62_AG(self):
        """http://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt
        AG = -1
        """
        self.tb_helper('A', 'G', 0)

    def test_blosum_62_AX(self):
        """http://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt
        AX = 0
        """
        self.tb_helper('A', 'X', 0)

    def test_blosum_62_RR(self):
        """http://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt
        RR = 5
        """
        self.tb_helper('R', 'R', 5)

    def test_blosum_62_XX(self):
        """http://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt
        XX = -1
        """
        self.tb_helper('X', 'X', -1)

    def test_blosum_62_WW(self):
        """http://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt
        WW = 11
        """
        self.tb_helper('W', 'W', 11)

    def test_blosum_62_BD(self):
        """http://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt
        BD = 4
        """
        self.tb_helper('B', 'D', 4)

    def test_blosum_62_0x450x45(self):
        self.tb_helper('-', '-', 0)

    def test_blosum_62_Z0x45(self):
        self.tb_helper('Z', '-', 0)

    def test_blosum_62_0x45S(self):
        self.tb_helper('-', 'S', 0)


if __name__ == '__main__':
    unittest.main()
