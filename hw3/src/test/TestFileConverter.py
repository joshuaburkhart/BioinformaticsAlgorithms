import unittest
import os

from hw3.src.lib.FileConverter import add_alignments_from_txt,matrix_2_dictsource
from hw3.src.lib.Alignment import MultipleAlignment

__author__ = 'burkhart'

VALID_ALIGN_1_FN = 'test-valid_align_1.txt'
VALID_ALIGN_1 = """
ATTDEWKKQRKDSHKEVERRRRENINTAINVLSDLLPVRESSKAAILACAAEYIQKLKETDEANIEKWTLQKLLSEQNASQLASANEKLQEELGNAYKEIEYMKRVLRK----------
HGSEEWHRQRRENHKEVERKRRESINTGIRELARLIPTTDTNKAQILQRAVEYIKRLKENENNNIEKWTLEKLLTEQAVSELSASNEKLKHELESAYREIEQLKRGKK-----------
TGSTAWKQQRKESHKEVERRRRQNINTAIEKLSDLLPVKETSKAAILSRAAEYIQKMKETETANIEKWTLQKLLGEQQVSSLTSANDKLEQELSKAYKNLQELKKKLKEAGIEDPTEEE
"""
VALID_ALIGN_2_FN = 'test-valid_align_2.txt'
VALID_ALIGN_2 = """
ATTDEWKKQRKDSHKEVERRRRENINTAINVLSDLLPVRESSKAAILACAAEYIQKLKETDEANIEKWTLQKLLSEQNASQLASANEKLQEELGNAYKEIEYMKRVLRK----------
HGSEEWHRQRRENHKEVERKRRESINTGIRELARLIPTTDTNKAQILQRAVEYIKRLKENENNNIEKWTLEKLLTEQAVSELSASNEKLKHELESAYREIEQLKRGKK-----------
TGSTAWKQQRKESHKEVERRRRQNINTAIEKLSDLLPVKETSKAAILSRAAEYIQKMKETETANIEKWTLQKLLGEQQVSSLTSANDKLEQELSKAYKNLQELKKKLKEAGIEDPTEEE

"""
VALID_ALIGN_3_FN = 'test-valid_align_3.txt'
VALID_ALIGN_3 = """
junk\n\n
\0x23 \0x65
ATTDEWKKQRKDSHKEVERRRRENINTAINVLSDLLPVRESSKAAILACAAEYIQKLKETDEANIEKWTLQKLLSEQNASQLASANEKLQEELGNAYKEIEYMKRVLRK----------
HGSEEWHRQRRENHKEVERKRRESINTGIRELARLIPTTDTNKAQILQRAVEYIKRLKENENNNIEKWTLEKLLTEQAVSELSASNEKLKHELESAYREIEQLKRGKK-----------
#comment

\n\n
"""
VALID_ALIGN_4_FN = 'test-valid_align_4.txt'
VALID_ALIGN_4 = """
ATT
DEW
HG-
--A
AAA
BBB
CCC
DDD
EEE
FFF
GGG
"""
VALID_ALIGN_5_FN = 'test-valid_align_5.txt'
VALID_ALIGN_5 = """
INV

KAQ

ATT

---

YYY

EEE
"""
VALID_MTRIX_1 = """
  A T C G
A 1 0 0 0
T 0 1 0 0
C 0 0 1 0
G 0 0 0 1
"""
VALID_MTRIX_2 = """
#ignored
#ignored
   A  T  C  G
A  5 -2 -6  0
T -2  5  4 -9
C -6  4  5 -3
G  0 -9 -3  5
# ignored
# ignored
"""

class TestFileConverter(unittest.TestCase):

    def setUp(self):
        self.alignment = MultipleAlignment()

    def tearDown(self):
        self.remove_file(VALID_ALIGN_1_FN)
        self.remove_file(VALID_ALIGN_2_FN)
        self.remove_file(VALID_ALIGN_3_FN)
        self.remove_file(VALID_ALIGN_4_FN)
        self.remove_file(VALID_ALIGN_5_FN)

    def create_file(self,filename,data):
        tst_data_fptr = open(filename, 'w+')
        tst_data_fptr.write(data)
        tst_data_fptr.close()

    def remove_file(self,filename):
        if os.path.isfile(filename):
            os.remove(filename)

    def test_txt_2_alignment_1(self):
        self.create_file(VALID_ALIGN_1_FN,VALID_ALIGN_1)

        add_alignments_from_txt(VALID_ALIGN_1_FN,self.alignment)
        self.assertIsNotNone(self.alignment,"alignment was not created")
        self.assertEqual(len(self.alignment.sequence_matrix),119)

        self.remove_file(VALID_ALIGN_1_FN)

    def test_txt_2_alignment_2(self):
        self.create_file(VALID_ALIGN_2_FN,VALID_ALIGN_2)

        add_alignments_from_txt(VALID_ALIGN_2_FN,self.alignment)
        self.assertIsNotNone(self.alignment,"alignment was not created")
        self.assertEqual(len(self.alignment.sequence_matrix),119)

        self.remove_file(VALID_ALIGN_2_FN)

    def test_txt_2_alignment_3(self):
        self.create_file(VALID_ALIGN_3_FN,VALID_ALIGN_3)

        add_alignments_from_txt(VALID_ALIGN_3_FN,self.alignment)
        self.assertIsNotNone(self.alignment,"alignment was not created")
        self.assertEqual(len(self.alignment.sequence_matrix),119)

        self.remove_file(VALID_ALIGN_3_FN)

    def test_txt_2_alignment_4(self):
        self.create_file(VALID_ALIGN_4_FN,VALID_ALIGN_4)

        add_alignments_from_txt(VALID_ALIGN_4_FN,self.alignment)
        self.assertIsNotNone(self.alignment,"alignment was not created")
        self.assertEqual(len(self.alignment.sequence_matrix),3)

        self.remove_file(VALID_ALIGN_4_FN)

    def test_txt_2_alignment_5(self):
        self.create_file(VALID_ALIGN_5_FN,VALID_ALIGN_5)

        add_alignments_from_txt(VALID_ALIGN_5_FN,self.alignment)
        self.assertIsNotNone(self.alignment,"alignment was not created")
        self.assertEqual(len(self.alignment.sequence_matrix),3)

        self.remove_file(VALID_ALIGN_5_FN)

    # TODO: Write negative unit tests for txt_2_alignment
    def test_txt_2_alignment(self):
        pass

    # TODO: Write unit tests for matrix_2_dictsource
    def test_matrix_2_dictsource(self):
        pass

if __name__ == '__main__':
    unittest.main()