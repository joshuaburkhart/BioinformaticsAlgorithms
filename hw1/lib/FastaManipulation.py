import sys
from os import path
import re

__author__ = 'burkhart'

_dna2prot = {
    "TTT": "F",
    "TTC": "F",
    "TTA": "L",
    "TTG": "L",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "ATT": "I",
    "ATC": "I",
    "ATA": "I",
    "ATG": "M",
    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",
    "TCT": "S",
    "TCC": "S",
    "TCA": "S",
    "TCG": "S",
    "CCT": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "ACT": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "TAT": "Y",
    "TAC": "Y",
    "TAA": False,  # stop
    "TAG": False,  # stop
    "CAT": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "AAT": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "GAT": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "TGT": "C",
    "TGC": "C",
    "TGA": False,  # stop
    "TGG": "W",
    "CGT": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "AGT": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G"
}

_annot_prot_seqs = {}

def basic_prot(prot):
    if prot in "RKH":
        return True
    return False


"""Reads in a FASTA file of nucleotide
 (DNA) sequences (20 pts)"""
def read_sequences(filename):
    fasta_sequences = {}
    name = ""
    in_fptr = open(filename, "r")
    while 1:
        line = in_fptr.readline()
        if not line:
            break
        if re.match('^>.*', line):
            name = str(line.replace('\n',''))
            fasta_sequences[name] = ''
        elif re.match('^[ATCG]*', line):
            fasta_sequences[name] += str(line.replace('\n',''))
    in_fptr.close()
    return fasta_sequences


"""Carry out the translation to a protein
sequence in all possible frames (30 pts)"""
def translate_to_prot(bp_seq):
    prot_seq_lst = []
    for start in range(0, 3):  # three positions w/o rev complement?
        prot_seq_str = ""
        for i in range(start, len(bp_seq), 3):
            if i < len(bp_seq) - 2:  # don't IOB
                codon = bp_seq[i] + bp_seq[i + 1] + bp_seq[i + 2]
                if _dna2prot[codon]:
                    prot_seq_str += _dna2prot[codon]
                else:  # stop codon
                    break
        prot_seq_lst.append(prot_seq_str)
    return prot_seq_lst


"""Finds  putative cleavage sites which
are "double basic" (e.g., KK, KR, RK, RR)
in the protein sequence (20 pts)"""
def find_put_clev_sites(in_prot_seq_str):
    loc = []
    for i, e in enumerate(in_prot_seq_str):
        if i < len(in_prot_seq_str) - 1:  # IOB
            if basic_prot(e) and basic_prot(in_prot_seq_str[i + 1]):
                loc.append(i)
        else:
            break  # obvi done
    return loc

"""Outputs the resulting protein sequences
 and the possible locations in a FASTA file
  that carries the description field from the
   nucleotide entry. The locations of the
   cleavage sites should be described in the
   description field (25 pts)"""
def add_prot_seq_annot(seq_name,put_clevs,prot_seq):
    key = seq_name + ', putative cleavage sites: ' + \
              (str(put_clevs) if len(put_clevs) > 0 else '<NONE>')
    if len(prot_seq) > 0:
        if key in _annot_prot_seqs.keys():
            _annot_prot_seqs[key] += '\n'+prot_seq
        else:
            _annot_prot_seqs[key] = prot_seq
    return [key,prot_seq]

def clear_prot_seq_annots():
    global _annot_prot_seqs
    _annot_prot_seqs = {}

def write_annot_prot_seqs(out_filename):
    out_fptr = open(out_filename, 'w+')
    out_fptr.write('\n'.join(k + '\n' + v for k, v in _annot_prot_seqs.items()))
    out_fptr.close()