import os
import unittest
from os import remove
from hw1.lib.FastaManipulation import clear_prot_seq_annots
from hw1.lib.FastaManipulation import read_sequences
from hw1.lib.FastaManipulation import write_annot_prot_seqs
from hw1.lib.FastaManipulation import add_prot_seq_annot
from hw1.lib.FastaManipulation import find_put_clev_sites
from hw1.lib.FastaManipulation import translate_to_prot
from hw1.lib.FastaManipulation import basic_prot

__author__ = 'burkhart'

_valid_fasta_data = """>gi|225543218|ref|NG_011641.1| Homo sapiens solute carrier family 16, member 2 (monocarboxylic acid transporter 8) (SLC16A2) on chromosome X
AGGTCCACAGTCAGACAAGTAAAATAATGTAAAGGGCTACAGGAGCCACACCTTACTTACTTGTTGTGAGCATAACCCAA
GCTGATTAATCTACACATGGTAGTAGTATTCTCTAAAGATCTGTTGTTGCTGATGATGTTTATTGATCAAGCATGATTTA
GAGATTTATAGAGGAAACTTCATGCATCTTAGGACACTAGCCCTATTTCTACAACTTTACTCTCAACCTTGTCTCATCTT
TTATATACTTCTATCTCAAAATGTCTTCACCCAATTTAGTAGAGTTACATTCAATAAATGGTAGTTATAATTATTAACAG
TTTCTACTACAATGTAAGCTCCATGAGGACAAGAACCATTGTATGTCCCCAGTGCCTAATATAGTGAATGGTACACATAG
TTGCTTGATAACTATTTGGGAAATGAATGGCTGAGTGGTATGAGAAAGGCAAGTGACATGCTTCCTCAGTTCAAGACTAA
>gi|291045455|ref|NG_016708.1| Homo sapiens Mdm2 p53 binding protein homolog (mouse) (MDM2) on chromosome 12
TTTACTTTTTTATTTTCCAGGACAGAGTCTTGCTCTGCCGCCCAGGCTCGAGTGCAGTGGCGCGATCTCGGCTCACTGCA
ACATCTGCCTCCCAGGTTCAAGAGATTCTGCTGCCTCAGCCTCCCGAGCAGCTGAGATTACAGGCTTGCACCACCATGCC
>gi|283945542|ref|NG_016372.1| Homo sapiens paraneoplastic antigen like 6A (PNMA6A), RefSeqGene on chromosome X
TCTAGAGCCTGTATCTTCTGCTTTCCCTTAGACCCTCCTTGCCCAGCCCCGGGGTCGGGGGGGCCTGGACTTGGGCTGCA
"""

_valid_fasta_infilename = 'test-valid.fasta'
_outfilename = 'test-output.fasta'

class TestFastaManipulation(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        clear_prot_seq_annots()
        if os.path.isfile(_valid_fasta_infilename):
            remove(_valid_fasta_infilename)
        if os.path.isfile(_outfilename):
            remove(_outfilename)

    def write_valid_fasta(self):
        tst_data_fptr = open(_valid_fasta_infilename, 'w+')
        tst_data_fptr.write(_valid_fasta_data)
        tst_data_fptr.close()

    # TODO: add more tests for read_sequences()
    def test_read_sequences_valid(self):
        # create valid fasta file
        self.write_valid_fasta()

        sequences = read_sequences(_valid_fasta_infilename)

        # assure correct type
        self.assertEqual(dict,type(sequences), 'Incorrect type')

        # assure correct length
        self.assertEqual(len(sequences), 3, 'Incorrect length')

        # assure correct keys
        self.assertTrue('>gi|225543218|ref|NG_011641.1| Homo sapiens solute ' \
                        'carrier family 16, member 2 (monocarboxylic acid ' \
                        'transporter 8) (SLC16A2) on chromosome X' in sequences.keys())
        self.assertTrue('>gi|291045455|ref|NG_016708.1| Homo sapiens Mdm2 ' \
                        'p53 binding protein homolog (mouse) (MDM2) on chromosome ' \
                        '12' in sequences.keys())
        self.assertTrue('>gi|283945542|ref|NG_016372.1| Homo sapiens paraneoplastic ' \
                        'antigen like 6A (PNMA6A), RefSeqGene on chromosome ' \
                        'X' in sequences.keys())

        # assure correct values
        self.assertTrue('TTTACTTTTTTATTTTCCAGGACAGAGTCTTGCTCTGCCGCCCAGGCTCGAGTGCAGTGGCGCGATCTCGGCTCACTGCA' \
                        'ACATCTGCCTCCCAGGTTCAAGAGATTCTGCTGCCTCAGCCTCCCGAGCAGCTGAGATTACAGGCTTGCACCACCATGCC'
                        in sequences.values())
        self.assertTrue('TCTAGAGCCTGTATCTTCTGCTTTCCCTTAGACCCTCCTTGCCCAGCCCCGGGGTCGGGGGGGCCTGGACTTGGGCTGCA'
                        in sequences.values())
        self.assertTrue('AGGTCCACAGTCAGACAAGTAAAATAATGTAAAGGGCTACAGGAGCCACACCTTACTTACTTGTTGTGAGCATAACCCAA' \
                        'GCTGATTAATCTACACATGGTAGTAGTATTCTCTAAAGATCTGTTGTTGCTGATGATGTTTATTGATCAAGCATGATTTA' \
                        'GAGATTTATAGAGGAAACTTCATGCATCTTAGGACACTAGCCCTATTTCTACAACTTTACTCTCAACCTTGTCTCATCTT' \
                        'TTATATACTTCTATCTCAAAATGTCTTCACCCAATTTAGTAGAGTTACATTCAATAAATGGTAGTTATAATTATTAACAG' \
                        'TTTCTACTACAATGTAAGCTCCATGAGGACAAGAACCATTGTATGTCCCCAGTGCCTAATATAGTGAATGGTACACATAG' \
                        'TTGCTTGATAACTATTTGGGAAATGAATGGCTGAGTGGTATGAGAAAGGCAAGTGACATGCTTCCTCAGTTCAAGACTAA'
                        in sequences.values())

        # assure correct k,v pairs
        self.assertEqual('AGGTCCACAGTCAGACAAGTAAAATAATGTAAAGGGCTACAGGAGCCACACCTTACTTACTTGTTGTGAGCATAACCCAA' \
                        'GCTGATTAATCTACACATGGTAGTAGTATTCTCTAAAGATCTGTTGTTGCTGATGATGTTTATTGATCAAGCATGATTTA' \
                        'GAGATTTATAGAGGAAACTTCATGCATCTTAGGACACTAGCCCTATTTCTACAACTTTACTCTCAACCTTGTCTCATCTT' \
                        'TTATATACTTCTATCTCAAAATGTCTTCACCCAATTTAGTAGAGTTACATTCAATAAATGGTAGTTATAATTATTAACAG' \
                        'TTTCTACTACAATGTAAGCTCCATGAGGACAAGAACCATTGTATGTCCCCAGTGCCTAATATAGTGAATGGTACACATAG' \
                        'TTGCTTGATAACTATTTGGGAAATGAATGGCTGAGTGGTATGAGAAAGGCAAGTGACATGCTTCCTCAGTTCAAGACTAA',
                         sequences['>gi|225543218|ref|NG_011641.1| Homo sapiens solute ' \
                                   'carrier family 16, member 2 (monocarboxylic acid ' \
                                   'transporter 8) (SLC16A2) on chromosome X'],
                         'Incorrect kv pair')
        self.assertEqual('TTTACTTTTTTATTTTCCAGGACAGAGTCTTGCTCTGCCGCCCAGGCTCGAGTGCAGTGGCGCGATCTCGGCTCACTGCA' \
                         'ACATCTGCCTCCCAGGTTCAAGAGATTCTGCTGCCTCAGCCTCCCGAGCAGCTGAGATTACAGGCTTGCACCACCATGCC',
                         sequences['>gi|291045455|ref|NG_016708.1| Homo sapiens Mdm2 ' \
                                   'p53 binding protein homolog (mouse) (MDM2) on chromosome ' \
                                   '12'],
                         'Incorrect kv pair')
        self.assertEqual('TCTAGAGCCTGTATCTTCTGCTTTCCCTTAGACCCTCCTTGCCCAGCCCCGGGGTCGGGGGGGCCTGGACTTGGGCTGCA',
                         sequences['>gi|283945542|ref|NG_016372.1| Homo sapiens paraneoplastic ' \
                                   'antigen like 6A (PNMA6A), RefSeqGene on chromosome ' \
                                   'X'],
                         'Incorrect kv pair')

    # TODO: add more tests for translate_to_prot()
    def test_translate_to_prot_valid_dna0(self):
        valid_dna0 = 'ATGATATATATGGGGAGAG'
        valid_dna0_pro0 = 'MIYMGR'
        valid_dna0_pro1 = ''
        valid_dna0_pro2 = 'DIYGE'

        prot_seqs = translate_to_prot(valid_dna0)

        # assure correct type
        self.assertEqual(list,type(prot_seqs),'Incorrect type')

        # assure correct length
        self.assertEqual(3,len(prot_seqs),'Incorrect length')

        # assure protein sequences shorter than dna sequence
        self.assertTrue(len(prot_seqs[0]) <= len(valid_dna0), 'Too many prots')
        self.assertTrue(len(prot_seqs[1]) <= len(valid_dna0), 'Too many prots')
        self.assertTrue(len(prot_seqs[2]) <= len(valid_dna0), 'Too many prots')

        # assure protein translated correctly
        self.assertEqual(valid_dna0_pro0,prot_seqs[0],'Incorrect prot translation')
        self.assertEqual(valid_dna0_pro1,prot_seqs[1],'Incorrect prot translation')
        self.assertEqual(valid_dna0_pro2,prot_seqs[2],'Incorrect prot translation')

        print(valid_dna0)
        print("".join([(x + "  ") for x in prot_seqs[0]]))
        print("".join([(" " + x + " ") for x in prot_seqs[1]]))
        print("".join([("  " + x) for x in prot_seqs[2]]))

    def test_translate_to_prot_valid_dna1(self):
        valid_dna1 = 'TTATATATTTATATATTTT'
        valid_dna1_pro0 = 'LYIYIF'
        valid_dna1_pro1 = 'YIFIYF'
        valid_dna1_pro2 = 'IYLYI'

        prot_seqs = translate_to_prot(valid_dna1)

        # assure correct type
        self.assertEqual(list,type(prot_seqs),'Incorrect type')

        # assure correct length
        self.assertEqual(3,len(prot_seqs),'Incorrect length')

        # assure protein sequences shorter than dna sequence
        self.assertTrue(len(prot_seqs[0]) <= len(valid_dna1), 'Too many prots')
        self.assertTrue(len(prot_seqs[1]) <= len(valid_dna1), 'Too many prots')
        self.assertTrue(len(prot_seqs[2]) <= len(valid_dna1), 'Too many prots')

        # assure protein translated correctly
        self.assertEqual(valid_dna1_pro0,prot_seqs[0],'Incorrect prot translation')
        self.assertEqual(valid_dna1_pro1,prot_seqs[1],'Incorrect prot translation')
        self.assertEqual(valid_dna1_pro2,prot_seqs[2],'Incorrect prot translation')

        print(valid_dna1)
        print("".join([(x + "  ") for x in prot_seqs[0]]))
        print("".join([(" " + x + " ") for x in prot_seqs[1]]))
        print("".join([("  " + x) for x in prot_seqs[2]]))

    def test_translate_to_prot_valid_dna2(self):
        valid_dna2 = 'GAGAGAGAGAGAGAGAGAT'
        valid_dna2_pro0 = 'ERERER'
        valid_dna2_pro1 = 'RERERD'
        valid_dna2_pro2 = 'ERERE'

        prot_seqs = translate_to_prot(valid_dna2)

        # assure correct type
        self.assertEqual(list,type(prot_seqs),'Incorrect type')

        # assure correct length
        self.assertEqual(3,len(prot_seqs),'Incorrect length')

        # assure protein sequences shorter than dna sequence
        self.assertTrue(len(prot_seqs[0]) <= len(valid_dna2), 'Too many prots')
        self.assertTrue(len(prot_seqs[1]) <= len(valid_dna2), 'Too many prots')
        self.assertTrue(len(prot_seqs[2]) <= len(valid_dna2), 'Too many prots')

        # assure protein translated correctly
        self.assertEqual(valid_dna2_pro0,prot_seqs[0],'Incorrect prot translation')
        self.assertEqual(valid_dna2_pro1,prot_seqs[1],'Incorrect prot translation')
        self.assertEqual(valid_dna2_pro2,prot_seqs[2],'Incorrect prot translation')

        print(valid_dna2)
        print("".join([(x + "  ") for x in prot_seqs[0]]))
        print("".join([(" " + x + " ") for x in prot_seqs[1]]))
        print("".join([("  " + x) for x in prot_seqs[2]]))

    # TODO: add more tests for find_put_clev_sites()
    def test_find_put_clev_sites_valid_prot_seq0(self):
        valid_prot_seq0 = 'KRH'
        valid_prot_seq0_clev0 = 0
        valid_prot_seq0_clev1 = 1

        put_clevs = find_put_clev_sites(valid_prot_seq0)

        # assure correct type
        self.assertEqual(list,type(put_clevs),'Incorrect type')

        # assure correct length
        self.assertEqual(2,len(put_clevs),'Incorrect length')

        # assure correct putative cleavage sites
        self.assertEqual(valid_prot_seq0_clev0,put_clevs[0],'Incorrect clev sites')
        self.assertEqual(valid_prot_seq0_clev1,put_clevs[1],'Incorrect clev sites')

        print(valid_prot_seq0)
        indicator = list(' ' * len(valid_prot_seq0))
        for put_clev in put_clevs:
            indicator[put_clev] = '^'
            print("".join(indicator))
            print(valid_prot_seq0)
            print(put_clevs)

    def test_find_put_clev_sites_valid_prot_seq1(self):
        valid_prot_seq1 = 'KRHLLLLLLLLLLLKK'
        valid_prot_seq1_clev0 = 0
        valid_prot_seq1_clev1 = 1
        valid_prot_seq1_clev2 = 14

        put_clevs = find_put_clev_sites(valid_prot_seq1)

        # assure correct type
        self.assertEqual(list,type(put_clevs),'Incorrect type')

        # assure correct length
        self.assertEqual(3,len(put_clevs),'Incorrect length')

        # assure correct putative cleavage sites
        self.assertEqual(valid_prot_seq1_clev0,put_clevs[0],'Incorrect clev sites')
        self.assertEqual(valid_prot_seq1_clev1,put_clevs[1],'Incorrect clev sites')
        self.assertEqual(valid_prot_seq1_clev2,put_clevs[2],'Incorrect clev sites')

        print(valid_prot_seq1)
        indicator = list(' ' * len(valid_prot_seq1))
        for put_clev in put_clevs:
            indicator[put_clev] = '^'
            print("".join(indicator))
            print(valid_prot_seq1)
            print(put_clevs)

    # TODO: add more tests for write_prot_seqs()
    def test_add_prot_seq_annot(self):
        seq_name = '>name0'
        put_clevs = [0, 1, 2, 3]
        prot_seq = 'KRKRKRKRKLLLLLLL'
        expected_name = '>name0, putative cleavage sites: [0, 1, 2, 3]'

        kv_pair = add_prot_seq_annot(seq_name, put_clevs, prot_seq)

        # assure correct type
        self.assertEqual(list,type(kv_pair),'Incorrect type')

        # assure correct length
        self.assertEqual(2,len(kv_pair),'Incorrect length')

        # assure correct key
        self.assertEqual(expected_name,kv_pair[0],'Incorrect key')

        # assure correct value
        self.assertEqual(prot_seq,kv_pair[1],'Incorrect value')

    def test_add_prot_seq_annot_no_prot_seq(self):
        seq_name = '>name0'
        put_clevs = []
        prot_seq = ''
        expected_name = '>name0, putative cleavage sites: <NONE>'

        kv_pair = add_prot_seq_annot(seq_name, put_clevs, prot_seq)

        # assure correct type
        self.assertEqual(list,type(kv_pair),'Incorrect type')

        # assure correct length
        self.assertEqual(2,len(kv_pair),'Incorrect length')

        # assure correct key
        self.assertEqual(expected_name,kv_pair[0],'Incorrect key')

        # assure correct value
        self.assertEqual(prot_seq,kv_pair[1],'Incorrect value')

    def test_add_prot_seq_annot_no_cleavage_sites(self):
        seq_name = '>name0'
        put_clevs = []
        prot_seq = 'KRKRKRKRKLLLLLLL'
        expected_name = '>name0, putative cleavage sites: <NONE>'

        kv_pair = add_prot_seq_annot(seq_name, put_clevs, prot_seq)

        # assure correct type
        self.assertEqual(list,type(kv_pair),'Incorrect type')

        # assure correct length
        self.assertEqual(2,len(kv_pair),'Incorrect length')

        # assure correct key
        self.assertEqual(expected_name,kv_pair[0],'Incorrect key')

        # assure correct value
        self.assertEqual(prot_seq,kv_pair[1],'Incorrect value')

    def test_write_annot_prot_seqs_1row(self):
        # build dictionary
        add_prot_seq_annot('>name1', [3, 13, 34], 'AGEKHAGGQ')

        expected_output = '>name1, putative cleavage sites: [3, 13, 34]\nAGEKHAGGQ'

        # write dictionary
        write_annot_prot_seqs(_outfilename)

        # check file was created
        self.assertTrue(os.path.exists(_outfilename))

        # read test output
        tst_fptr = open(_outfilename, 'r+')
        tst_output0 = tst_fptr.read()
        tst_fptr.close()

        print
        print('Actual output')
        print('!'+tst_output0+'!')

        print
        print('Expected output')
        print('!'+expected_output+'!')

        self.assertEqual(expected_output,tst_output0,'Incorrect data')

    def test_write_annot_prot_seqs_2rows(self):
        # build dictionary
        add_prot_seq_annot('>name1', [3, 13, 34], 'AGEKHAGGQ')
        add_prot_seq_annot('>name2', [4, 14, 35], 'GGLKAALGT')

        expected_output = '>name1, putative cleavage sites: [3, 13, 34]\nAGEKHAGGQ\n>name2, putative cleavage sites: [4, 14, 35]\nGGLKAALGT'

        # write dictionary
        write_annot_prot_seqs(_outfilename)

        # check file was created
        self.assertTrue(os.path.exists(_outfilename))

        # read test output
        tst_fptr = open(_outfilename, 'r+')
        tst_output0 = tst_fptr.read()
        tst_fptr.close()

        print
        print('Actual output')
        print('!'+tst_output0+'!')

        print
        print('Expected output')
        print('!'+expected_output+'!')

        self.assertEqual(expected_output,tst_output0,'Incorrect data')

    def test_write_annot_prot_seqs_1key_2prots(self):
        # build dictionary
        add_prot_seq_annot('>name1', [], 'AGEKHAGGQ')
        add_prot_seq_annot('>name1', [], 'GGLKAALGT')

        expected_output = '>name1, putative cleavage sites: <NONE>\nAGEKHAGGQ\nGGLKAALGT'

        # write dictionary
        write_annot_prot_seqs(_outfilename)

        # check file was created
        self.assertTrue(os.path.exists(_outfilename))

        # read test output
        tst_fptr = open(_outfilename, 'r+')
        tst_output0 = tst_fptr.read()
        tst_fptr.close()

        print
        print('Actual output')
        print('!'+tst_output0+'!')

        print
        print('Expected output')
        print('!'+expected_output+'!')

        self.assertEqual(expected_output,tst_output0,'Incorrect data')

    def test_basic_prot(self):
        # basic
        self.assertTrue(basic_prot('K'),'Should be basic')
        self.assertTrue(basic_prot('R'),'Should be basic')
        self.assertTrue(basic_prot('H'),'Should be basic')

        # not
        self.assertFalse(basic_prot('G'),'Should not be basic')
        self.assertFalse(basic_prot('F'),'Should not be basic')
        self.assertFalse(basic_prot('L'),'Should not be basic')
        self.assertFalse(basic_prot('S'),'Should not be basic')
        self.assertFalse(basic_prot('Y'),'Should not be basic')
        self.assertFalse(basic_prot('C'),'Should not be basic')
        self.assertFalse(basic_prot('W'),'Should not be basic')
        self.assertFalse(basic_prot('P'),'Should not be basic')
        self.assertFalse(basic_prot('Q'),'Should not be basic')
        self.assertFalse(basic_prot('I'),'Should not be basic')
        self.assertFalse(basic_prot('M'),'Should not be basic')
        self.assertFalse(basic_prot('T'),'Should not be basic')
        self.assertFalse(basic_prot('N'),'Should not be basic')
        self.assertFalse(basic_prot('V'),'Should not be basic')
        self.assertFalse(basic_prot('A'),'Should not be basic')
        self.assertFalse(basic_prot('D'),'Should not be basic')
        self.assertFalse(basic_prot('E'),'Should not be basic')


if __name__ == '__main__':
    unittest.main()
