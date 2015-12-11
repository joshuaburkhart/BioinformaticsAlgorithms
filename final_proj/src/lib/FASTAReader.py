
import sys
import re

_fasta_data = '[ATCGNatcgn]+'
_fasta_nt_list = ['\x00'] # prepend with null byte for 1-indexed coord system
_transcriptome_nt_multiset = []

def parse_fasta(fasta_filename):
    global _fasta_nt_list
    #build fasta_coord_data
    #coord: 'nt'
    in_fptr = open(fasta_filename)
    while 1:
        line = in_fptr.readline()
        if not line:
            break
        if re.match(_fasta_data, line):
            [_fasta_nt_list.append(char) for char in line]
    in_fptr.close()

#TODO: use list comprehensions
def build_transcriptome_multiset(transcript_dict):
    global _fasta_nt_list
    global _transcriptome_nt_multiset
    for tid,exons in transcript_dict.items():
        sorted_t = sort_t(exons)
        for coord in sorted_t:
            if coord in _fasta_nt_list:
                _transcriptome_nt_multiset.append(_fasta_nt_list[coord].upper())

def pct_char(char):
    if char.upper() in _transcriptome_nt_multiset:
        return \
            float(_transcriptome_nt_multiset.count(char.upper()))/ \
            float(len(_transcriptome_nt_multiset) - 1)# subtract 1 for null byte due to 1-based coord system
    else:
        return 0

#TODO: remove this duplicate code (from AltDensity)
def sort_t(transcript):
    print('T',end="")
    sys.stdout.flush()
    exon_idcs = []
    print('adding exons to exon_idcs...')
    for exon in transcript:
        try:
            exon_idcs += list(range(exon[0], exon[1] + 1))
        except IndexError:
            print('exon:{0}'.format(exon))
    print('sorting exon_idcs in case transcript was antisense')
    exon_idcs.sort()
    return exon_idcs