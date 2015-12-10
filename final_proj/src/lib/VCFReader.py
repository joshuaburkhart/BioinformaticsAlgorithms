import re

_alt_data = '[0-9]+?\s+(?P<locus>[0-9]+)'

def parse_alternates(vcf_filename):
    s = ([])
    in_fptr = open(vcf_filename)
    while 1:
        line = in_fptr.readline()
        if not line:
            break
        m = re.fullmatch(_alt_data, line)
        if m:
            s.append(m.group('locus'))
    in_fptr.close()
    return s