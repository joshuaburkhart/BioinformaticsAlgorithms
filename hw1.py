# usage: python hw1.py infile [outfile]
import os
import sys
from hw1.lib.FastaManipulation import read_sequences
from hw1.lib.FastaManipulation import translate_to_prot
from hw1.lib.FastaManipulation import find_put_clev_sites
from hw1.lib.FastaManipulation import add_prot_seq_annot
from hw1.lib.FastaManipulation import write_annot_prot_seqs

__author__ = 'burkhart'

_outfilename = 'output.fasta'

if len(sys.argv) < 2:
    print("filename plz")
    exit()
elif not os.path.isfile(sys.argv[1]) or len(sys.argv) > 3:
    print("check usage plz")
    exit()
elif len(sys.argv) == 3:
    _outfilename = sys.argv[2]

dna_sequences = read_sequences(sys.argv[1])

for identifier in dna_sequences:
    possible_protein_sequences = translate_to_prot(dna_sequences[identifier])

    for protein_sequence in possible_protein_sequences:
        add_prot_seq_annot(
            identifier,
            find_put_clev_sites(protein_sequence),
            protein_sequence)

write_annot_prot_seqs(_outfilename)
