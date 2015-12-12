import sys
import math

from src.lib.FASTQReader import parse_fastq,pct_read_chr_cnt,read_char_entropy
from src.lib.AltDensity import max_in_window
from src.lib.GTFReader import parse_transcripts
from src.lib.VCFReader import parse_alternates
from src.lib.FASTAReader import parse_fasta,build_transcriptome_multiset,pct_char,t_len

USAGE = 'Usage: python3 final_proj.py \
        <read length> <gtf file> <vcf file> <reference fasta> <reads fastq>\n' \
        'Example: python3 final_proj.py 100 ./data/input/example.gtf \
        ./data/input/example.vcf ./data/input/reference.fasta \'' \
        './data/input/reads.fastq'

if len(sys.argv) != 6:
    print(USAGE)
    exit()

_read_len = int(sys.argv[1])
_gtf = sys.argv[2]
_vcf = sys.argv[3]
_fasta = sys.argv[4]
_reads = sys.argv[5]

# Part 1:

## read .gtf file, store exons by transcript id

print('parsing transcripts from {0}...'.format(_gtf))
d = parse_transcripts(_gtf)
print('len(d):{0}'.format(len(d)))

## prob of single random read matching

## prob of random read matching w x tries

## prob of each base

print('calculating probability of each base in reference...')
f = parse_fasta(_fasta)
t = build_transcriptome_multiset(d)
p = [pct_char('A'),pct_char('T'),pct_char('C'),pct_char('G')]
print('A: {0}, T: {1}, C: {2}, G: {3}'.format(
    p[0],p[1],p[2],p[3]))

## calculate entropy using 0-order markov model

print('calculating entropy in reference...')
i = - .24 * math.log2(.25)
a_a = p[0] * math.log2(p[0]) * p[0]
a_t = p[1] * math.log2(p[1]) * p[1]
a_c = p[2] * math.log2(p[2]) * p[2]
a_g = p[3] * math.log2(p[3]) * p[3]
a = - sum([a_a,a_t,a_c,a_g])
r = i/a

print('UR entropy: {0}, true entropy: {1}, ratio: {2}'.format(
    i,a,r
))

## increase n to mimic maximum information (minimum entropy)

print('length adjustment: {0} -> {1}'.format(
    _read_len,float(_read_len)/r
))

print('parsing reads from fastq...')
q = parse_fastq(sys.argv[5])
q_a = pct_read_chr_cnt('A')
q_t = pct_read_chr_cnt('T')
q_c = pct_read_chr_cnt('C')
q_g = pct_read_chr_cnt('G')
print('probability of each base in reads...')
print('A: {0}, T: {1}, C: {2}, G: {3}'.format(
    q_a,q_t,q_c,q_g
))

ent = read_char_entropy()
print('Read entropy: {0}'.format(ent))

## review minimum supported feature from previous alignment

## adjust m down to less than minimum support

## + ceil/floor entropy, error rate ? assess

# Part 2:

## read .vcf file, store alt locations & counts?

print('parsing alternates from {0}...'.format(_vcf))
s = parse_alternates(_vcf)
print('len(s):{0}'.format(len(s)))

## find max alt density in read-length window

print('finding max alt density in {0}nt window...'.format(_read_len))
m = max_in_window(d, s, _read_len)
mlist = sorted(list(m), key=lambda x: str(x))
print('max alts in {0}nt window = {1}: {2}'.format(_read_len, len(mlist) - 1, mlist))

print('done.')