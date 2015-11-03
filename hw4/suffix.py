import sys

S_TERM = '$'

def suffix_array(instring):
    instring += S_TERM
    sa = []
    [sa.append(instring[x:]) for x in range(len(instring))]
    return sorted(sa)

def circular_suffix_array(instring):
    instring += S_TERM
    sa = []
    [sa.append(instring[x:] + instring[:x]) for x in range(len(instring))]
    return sorted(sa)

a = suffix_array(sys.argv[1])
b = circular_suffix_array(sys.argv[1])
print('Suffix Array')
print('------------')
print('\n'.join(a))
print()
print('BW Matrix')
print('---------')
print('\n'.join(b))