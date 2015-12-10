import sys
from src.lib.AltDensity import max_in_window
from src.lib.GTFReader import parse_transcripts
from src.lib.VCFReader import parse_alternates

USAGE = 'Usage: python3 final_proj.py <read length> <gtf file> <vcf file>\n' \
        'Example: python3 final_proj.py 100 ./data/input/example.gtf ./data/input/example.vcf'

if len(sys.argv) != 4:
    print(USAGE)
    exit()

_read_len = int(sys.argv[1])
_gtf = sys.argv[2]
_vcf = sys.argv[3]

# Part 1:

## read .gtf file, store exons by transcript id

print('parsing transcripts from {0}...'.format(_gtf))
d = parse_transcripts(_gtf)
print('len(d):{0}'.format(len(d)))

## read .vcf file, store alt locations & counts?

print('parsing alternates from {0}...'.format(_vcf))
s = parse_alternates(_vcf)
print('len(s):{0}'.format(len(s)))

## find max alt density in read-length window

print('finding max alt density in {0}nt window...'.format(_read_len))
m = max_in_window(d, s, _read_len)
print('max alts in {0}nt window = {1}: {2}'.format(_read_len,len(m),m))

# Part 2:

## prob of single random read matching

## prob of random read matching w x tries

## calculate entropy using 0-order markov model

## increase n to mimic maximum information (minimum entropy)

## how good was our last model?

## review minimum supported feature from previous alignment

## adjust m down to less than minimum support

## + ceil/floor entropy, error rate ? assess

print('done.')