import sys


from src.lib.AltDensity import max_in_window
from src.lib.GTFReader import parse_transcripts
from src.lib.VCFReader import parse_alternates

USAGE = 'Usage: python3 final_proj.py <read length> <gtf file> <vcf file>\n' \
        'Example: python3 final_proj.py 100 ./data/input/example.gtf ./data/input/example.vcf'

if len(sys.argv) != 4:
    print(USAGE)
    exit()

# Part 1:

## read .gtf file, store exons by transcript id

d = parse_transcripts(sys.argv[2])

## read .vcf file, store alt locations & counts?

s = parse_alternates(sys.argv[3])

## find max alt density in read-length window

m = max_in_window(d,s,sys.argv[4])
print(m)

# Part 2:

## prob of single random read matching

## prob of random read matching w x tries

## calculate entropy using 0-order markov model

## increase n to mimic maximum information (minimum entropy)

## how good was our last model?

## review minimum supported feature from previous alignment

## adjust m down to less than minimum support

## + ceil/floor entropy, error rate ? assess