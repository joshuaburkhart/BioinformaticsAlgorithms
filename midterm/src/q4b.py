from random import randint

SIGMA = 'ARNDCQEGHILKMFPSTWYVBZX'


def r_char():
    """
    Generates a random character
    :return: a random character from SIGMA
    """
    return SIGMA[randint(0, len(SIGMA) - 1)]


def random_sequence(l):
    """
    Generates a random sequence
    :param l: length of random sequence to build
    :return: random sequence of length l
    """
    r_seq = ''
    for i in range(l):
        r_seq += r_char()
    return r_seq


def local_align_sequence(r_seq):
    """
    Matches middle third of the characters in r_seq
    :param r_seq: any random sequence
    :return: a sequence that will align locally to r_seq
    """
    l_seq = ''
    t3 = len(r_seq)
    t1 = int(len(r_seq) / 3)
    t2 = 2 * t1
    for i in range(t1):
        l_seq += r_char().lower()
    for i in range(t1, t2):
        l_seq += r_seq[i]
    for i in range(t2, t3):
        l_seq += r_char().lower()
    return l_seq


def global_align_sequence(r_seq):
    """
    Matches every third character in r_seq
    :param r_seq: any random sequence
    :return: a sequence that will align globally to r_seq
    """
    g_seq = ''
    for i in range(len(r_seq)):
        if i % 3 == 0:
            g_seq += r_seq[i]
        else:
            g_seq += r_char().lower()
    return g_seq


r = random_sequence(10)
l = local_align_sequence(r)
g = global_align_sequence(r)

print('r: ' + r)
print('l: ' + l)
print('g: ' + g)

BLOSUM62 = {frozenset({'R', 'P'}): -2.0, frozenset({'S', 'G'}): 0.0, frozenset({'T', 'K'}): -1.0,
            frozenset({'N', 'G'}): 0.0, frozenset({'Z', 'G'}): -2.0, frozenset({'P', 'B'}): -2.0,
            frozenset({'T', 'W'}): -2.0, frozenset({'N', 'D'}): 1.0, frozenset({'*', 'N'}): -4.0, frozenset({'L'}): 4.0,
            frozenset({'Q', 'A'}): -1.0, frozenset({'N', 'K'}): 0.0, frozenset({'*', 'M'}): -4.0,
            frozenset({'N', 'A'}): -2.0, frozenset({'Q', 'P'}): -1.0, frozenset({'X', 'A'}): 0.0,
            frozenset({'Z', 'K'}): 1.0, frozenset({'*', 'K'}): -4.0, frozenset({'H', 'D'}): -1.0,
            frozenset({'C', 'D'}): -3.0, frozenset({'B', 'X'}): -1.0, frozenset({'Q', 'R'}): 1.0,
            frozenset({'W', 'P'}): -4.0, frozenset({'S', 'Y'}): -2.0, frozenset({'*', 'W'}): -4.0,
            frozenset({'W', 'D'}): -4.0, frozenset({'K', 'M'}): -1.0, frozenset({'I', 'V'}): 3.0,
            frozenset({'E', 'K'}): 1.0, frozenset({'C', 'Y'}): -2.0, frozenset({'R', 'D'}): -2.0,
            frozenset({'Z', 'B'}): 1.0, frozenset({'P', 'G'}): -2.0, frozenset({'Q', 'C'}): -3.0,
            frozenset({'R', 'S'}): -1.0, frozenset({'B', 'L'}): -4.0, frozenset({'R', 'Z'}): 0.0,
            frozenset({'I', 'F'}): 0.0, frozenset({'S', 'A'}): 1.0, frozenset({'I', 'B'}): -3.0,
            frozenset({'F', 'Y'}): 3.0, frozenset({'D', 'A'}): -2.0, frozenset({'E', 'C'}): -4.0,
            frozenset({'H', 'E'}): 0.0, frozenset({'I', 'C'}): -1.0, frozenset({'H', 'I'}): -3.0,
            frozenset({'Q', 'T'}): -1.0, frozenset({'V', 'D'}): -3.0, frozenset({'K', 'D'}): -1.0,
            frozenset({'Q', 'V'}): -2.0, frozenset({'C', 'B'}): -3.0, frozenset({'*', 'V'}): -4.0,
            frozenset({'X', 'Y'}): -1.0, frozenset({'F', 'V'}): -1.0, frozenset({'I', 'M'}): 1.0,
            frozenset({'P', 'M'}): -2.0, frozenset({'E', 'W'}): -3.0, frozenset({'W', 'A'}): -3.0,
            frozenset({'E', 'L'}): -3.0, frozenset({'T', 'Z'}): -1.0, frozenset({'*', 'E'}): -4.0,
            frozenset({'I', 'N'}): -3.0, frozenset({'E', 'Z'}): 4.0, frozenset({'H', 'A'}): -2.0,
            frozenset({'B', 'K'}): 0.0, frozenset({'M'}): 5.0, frozenset({'T', 'Y'}): -2.0, frozenset({'D', 'G'}): -1.0,
            frozenset({'K'}): 5.0, frozenset({'W', 'N'}): -4.0, frozenset({'I', 'X'}): -1.0, frozenset({'A'}): 4.0,
            frozenset({'N', 'L'}): -3.0, frozenset({'W', 'C'}): -2.0, frozenset({'H', 'W'}): -2.0,
            frozenset({'F', 'M'}): 0.0, frozenset({'S', 'D'}): 0.0, frozenset({'*', 'D'}): -4.0,
            frozenset({'P', 'X'}): -2.0, frozenset({'T', 'L'}): -1.0, frozenset({'L', 'M'}): 2.0,
            frozenset({'D', 'M'}): -3.0, frozenset({'*', 'T'}): -4.0, frozenset({'P', 'Y'}): -3.0,
            frozenset({'T', 'G'}): -2.0, frozenset({'R', 'Y'}): -2.0, frozenset({'I', 'P'}): -3.0,
            frozenset({'*', 'S'}): -4.0, frozenset({'S', 'W'}): -3.0, frozenset({'F', 'G'}): -3.0,
            frozenset({'I', 'T'}): -1.0, frozenset({'T', 'E'}): -1.0, frozenset({'G'}): 6.0, frozenset({'H', 'N'}): 1.0,
            frozenset({'W', 'Y'}): 2.0, frozenset({'V', 'M'}): 1.0, frozenset({'N', 'C'}): -3.0,
            frozenset({'V', 'L'}): 1.0, frozenset({'Q', 'Z'}): 3.0, frozenset({'R', 'G'}): -2.0,
            frozenset({'F', 'X'}): -1.0, frozenset({'W', 'B'}): -4.0, frozenset({'H', 'B'}): 0.0,
            frozenset({'V', 'A'}): 0.0, frozenset({'Z', 'Y'}): -2.0, frozenset({'W', 'L'}): -2.0,
            frozenset({'K', 'A'}): -1.0, frozenset({'T', 'A'}): 0.0, frozenset({'Y', 'D'}): -3.0,
            frozenset({'R', 'C'}): -3.0, frozenset({'X', 'M'}): -1.0, frozenset({'Q', 'L'}): -2.0,
            frozenset({'Q', 'D'}): 0.0, frozenset({'I', 'W'}): -3.0, frozenset({'E', 'D'}): 2.0,
            frozenset({'R', 'T'}): -1.0, frozenset({'Y', 'G'}): -3.0, frozenset({'S', 'E'}): 0.0,
            frozenset({'F', 'P'}): -4.0, frozenset({'S'}): 4.0, frozenset({'W'}): 11.0, frozenset({'C', 'A'}): 0.0,
            frozenset({'T', 'B'}): -1.0, frozenset({'R', 'F'}): -3.0, frozenset({'H', 'K'}): -1.0,
            frozenset({'H', 'M'}): -2.0, frozenset({'C', 'M'}): -1.0, frozenset({'S', 'M'}): -1.0,
            frozenset({'Q', 'I'}): -3.0, frozenset({'R'}): 5.0, frozenset({'F', 'C'}): -2.0,
            frozenset({'H', 'F'}): -1.0, frozenset({'V', 'G'}): -3.0, frozenset({'Z', 'L'}): -3.0,
            frozenset({'W', 'V'}): -3.0, frozenset({'*', 'Z'}): -4.0, frozenset({'H', 'C'}): -3.0,
            frozenset({'N', 'V'}): -3.0, frozenset({'L', 'D'}): -4.0, frozenset({'R', 'V'}): -3.0,
            frozenset({'Q', 'Y'}): -1.0, frozenset({'S', 'L'}): -2.0, frozenset({'N', 'M'}): -2.0,
            frozenset({'Z', 'M'}): -1.0, frozenset({'F', 'L'}): 0.0, frozenset({'H', 'G'}): -2.0,
            frozenset({'C', 'G'}): -3.0, frozenset({'F', 'Z'}): -3.0, frozenset({'V', 'B'}): -3.0,
            frozenset({'H', 'L'}): -3.0, frozenset({'E'}): 5.0, frozenset({'*', 'C'}): -4.0,
            frozenset({'H', '*'}): -4.0, frozenset({'F', 'B'}): -3.0, frozenset({'E', 'A'}): -1.0,
            frozenset({'R', 'A'}): -1.0, frozenset({'H', 'R'}): 0.0, frozenset({'E', 'N'}): 0.0,
            frozenset({'T', 'V'}): 0.0, frozenset({'*', 'B'}): -4.0, frozenset({'G', 'A'}): 0.0,
            frozenset({'H', 'S'}): -1.0, frozenset({'Q', 'F'}): -3.0, frozenset({'N', 'P'}): -2.0,
            frozenset({'D'}): 6.0, frozenset({'Z', 'X'}): -1.0, frozenset({'F', 'W'}): 1.0, frozenset({'N', 'Y'}): -2.0,
            frozenset({'X', 'D'}): -1.0, frozenset({'Z', 'V'}): -2.0, frozenset({'Q', '*'}): -4.0,
            frozenset({'Q', 'S'}): 0.0, frozenset({'L', 'K'}): -2.0, frozenset({'W', 'Z'}): -3.0,
            frozenset({'*', 'Y'}): -4.0, frozenset({'*', 'L'}): -4.0, frozenset({'Q'}): 5.0,
            frozenset({'L', 'A'}): -1.0, frozenset({'E', 'V'}): -2.0, frozenset({'I', 'Z'}): -3.0,
            frozenset({'I', 'K'}): -3.0, frozenset({'E', 'Y'}): -2.0, frozenset({'C', 'K'}): -3.0,
            frozenset({'I', 'Y'}): -1.0, frozenset({'*', 'G'}): -4.0, frozenset({'E', 'X'}): -1.0,
            frozenset({'S', 'X'}): 0.0, frozenset({'Q', 'X'}): -1.0, frozenset({'P', 'A'}): -1.0,
            frozenset({'F', 'K'}): -3.0, frozenset({'S', 'Z'}): 0.0, frozenset({'Z'}): 4.0, frozenset({'I', 'D'}): -3.0,
            frozenset({'Q', 'H'}): 0.0, frozenset({'*', 'F'}): -4.0, frozenset({'F', 'D'}): -3.0,
            frozenset({'T', 'D'}): -1.0, frozenset({'S', 'K'}): 0.0, frozenset({'I', '*'}): -4.0,
            frozenset({'S', 'T'}): 1.0, frozenset({'C', 'L'}): -1.0, frozenset({'E', 'P'}): -1.0,
            frozenset({'X'}): -1.0, frozenset({'R', 'X'}): -1.0, frozenset({'B', 'Y'}): -3.0,
            frozenset({'R', 'L'}): -2.0, frozenset({'E', 'M'}): -2.0, frozenset({'*', 'R'}): -4.0,
            frozenset({'H', 'V'}): -3.0, frozenset({'Q', 'W'}): -2.0, frozenset({'E', 'F'}): -3.0,
            frozenset({'Z', 'D'}): 1.0, frozenset({'P', 'V'}): -2.0, frozenset({'V', 'K'}): -2.0, frozenset({'N'}): 6.0,
            frozenset({'R', 'W'}): -3.0, frozenset({'S', 'P'}): -1.0, frozenset({'Z', 'A'}): -1.0,
            frozenset({'P', 'D'}): -1.0, frozenset({'*', 'X'}): -4.0, frozenset({'V', 'Y'}): -1.0,
            frozenset({'X', 'L'}): -1.0, frozenset({'I', 'G'}): -4.0, frozenset({'E', 'G'}): -2.0,
            frozenset({'L', 'Y'}): -1.0, frozenset({'P', 'K'}): -1.0, frozenset({'R', 'M'}): -1.0,
            frozenset({'R', 'K'}): 2.0, frozenset({'W', 'M'}): -1.0, frozenset({'C'}): 9.0, frozenset({'H'}): 8.0,
            frozenset({'I', 'S'}): -2.0, frozenset({'S', 'B'}): 0.0, frozenset({'X', 'G'}): -1.0,
            frozenset({'V', 'X'}): -1.0, frozenset({'L', 'G'}): -4.0, frozenset({'T', 'C'}): -1.0,
            frozenset({'T'}): 5.0, frozenset({'Q', 'E'}): 2.0, frozenset({'B'}): 4.0, frozenset({'P'}): 7.0,
            frozenset({'W', 'K'}): -3.0, frozenset({'I'}): 4.0, frozenset({'*'}): 1.0, frozenset({'R', 'B'}): -1.0,
            frozenset({'T', 'F'}): -2.0, frozenset({'T', 'M'}): -1.0, frozenset({'Z', 'N'}): 0.0,
            frozenset({'I', 'E'}): -3.0, frozenset({'T', 'N'}): 0.0, frozenset({'S', 'F'}): -2.0,
            frozenset({'E', 'B'}): 1.0, frozenset({'Y', 'A'}): -2.0, frozenset({'W', 'G'}): -2.0,
            frozenset({'I', 'R'}): -3.0, frozenset({'R', 'E'}): 0.0, frozenset({'Y'}): 7.0, frozenset({'F', 'N'}): -3.0,
            frozenset({'T', 'X'}): 0.0, frozenset({'G', 'M'}): -3.0, frozenset({'K', 'G'}): -2.0,
            frozenset({'S', 'C'}): -1.0, frozenset({'Z', 'C'}): -3.0, frozenset({'H', 'Z'}): 0.0,
            frozenset({'Q', 'B'}): 0.0, frozenset({'C', 'V'}): -1.0, frozenset({'V'}): 4.0, frozenset({'I', 'A'}): -1.0,
            frozenset({'H', 'Y'}): 2.0, frozenset({'W', 'X'}): -2.0, frozenset({'Q', 'N'}): 0.0,
            frozenset({'R', 'N'}): 0.0, frozenset({'B', 'D'}): 4.0, frozenset({'H', 'X'}): -1.0,
            frozenset({'C', 'X'}): -2.0, frozenset({'*', 'A'}): -4.0, frozenset({'N', 'B'}): 3.0,
            frozenset({'B', 'G'}): -1.0, frozenset({'*', 'P'}): -4.0, frozenset({'K', 'Y'}): -2.0,
            frozenset({'Y', 'M'}): -1.0, frozenset({'P', 'L'}): -3.0, frozenset({'Q', 'K'}): 1.0,
            frozenset({'S', 'V'}): -2.0, frozenset({'F'}): 6.0, frozenset({'M', 'A'}): -1.0,
            frozenset({'F', 'A'}): -2.0, frozenset({'N', 'X'}): -1.0, frozenset({'T', 'P'}): -1.0,
            frozenset({'S', 'N'}): 1.0, frozenset({'Q', 'G'}): -2.0, frozenset({'B', 'A'}): -2.0,
            frozenset({'H', 'P'}): -2.0, frozenset({'C', 'P'}): -3.0, frozenset({'X', 'K'}): -1.0,
            frozenset({'Q', 'M'}): 0.0, frozenset({'Z', 'P'}): -1.0, frozenset({'B', 'M'}): -3.0,
            frozenset({'I', 'L'}): 2.0, frozenset({'H', 'T'}): -2.0}

def h(char_i, char_j):
    """
    simply wraps dictionary
    """
    return BLOSUM62[frozenset([char_i, char_j])]

_gap_penalty = -4 # taken from blosum matrix above

def set_globs(s1,s2):
    global _s1
    global _s2
    global _dp
    _s1 = '*' + s1
    _s2 = '*' + s2

    # create DP matrix with S1 + 1 columns and S2 + 1 rows
    _dp = [[0 for x in range(len(_s1) + 1)] for x in range(len(_s2) + 1)]

def fill_l_dp_matrix():
    global _dp
    for i in range(len(_s2)):
        for j in range(len(_s1)):
            if i > 0 and j > 0:
                _dp[i][j] = max(_dp[i - 1][j - 1] + h(_s2[i], _s1[j]),
                                _dp[i - 1][j] + _gap_penalty,
                                _dp[i][j - 1] + _gap_penalty,
                                0) # allow for local alignment
            elif i > 0:
                _dp[i][j] = _dp[i - 1][j] + _gap_penalty
            elif j > 0:
                _dp[i][j] = _dp[i][j - 1] + _gap_penalty
            else:
                _dp[i][j] = 0

def fill_dp_matrix():
    global _dp
    for i in range(len(_s2)):
        for j in range(len(_s1)):
            if i > 0 and j > 0:
                _dp[i][j] = max(_dp[i - 1][j - 1] + h(_s2[i], _s1[j]),
                                _dp[i - 1][j] + _gap_penalty,
                                _dp[i][j - 1] + _gap_penalty)
            elif i > 0:
                _dp[i][j] = _dp[i - 1][j] + _gap_penalty
            elif j > 0:
                _dp[i][j] = _dp[i][j - 1] + _gap_penalty
            else:
                _dp[i][j] = 0


def print_h_matrix():
    for c in range(len(_s1)):
        print(' {0}'.format(_s1[c]).center(4, ' '), end='')
    print()
    for i in range(len(_s2)):
        print('{0}'.format(_s2[i]), end='')
        for j in range(len(_s1)):
                print('{0}'.format(h(_s2[i],
                                    _s1[j])).center(4, ' '), end='')
        print()


def print_dp_matrix():
    for c in range(len(_s1)):
        print(' {0}'.format(_s1[c]).center(4, ' '), end='')
    print()
    for i in range(len(_s2)):
        print('{0}'.format(_s2[i]), end='')
        for j in range(len(_s1)):
            print('{0}'.format(_dp[i][j]).center(4, ' '), end='')
        print()

def lbacktrace():
    s1_alignment = ''
    s2_alignment = ''
    i = len(_s2) - 1
    j = len(_s1) - 1
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            diag = _dp[i - 1][j - 1]
            up = _dp[i - 1][j]
            left = _dp[i][j - 1]
            if (_dp[i][j] - up) == _gap_penalty:
                s1_alignment = '*' + s1_alignment
                s2_alignment = _s2[i] + s2_alignment
                i -= 1
            elif (_dp[i][j] - diag) == h(_s2[i],_s1[j]):
                s1_alignment = _s1[j] + s1_alignment
                s2_alignment = _s2[i] + s2_alignment
                i -= 1
                j -= 1
            elif (_dp[i][j] - left) == _gap_penalty:
                s1_alignment = _s1[j] + s1_alignment
                s2_alignment = '*' + s2_alignment
                j -= 1
            else: # skip
                s1_alignment = _s1[j] + s1_alignment
                s2_alignment = '*' + s2_alignment
                i -= 1
                j -= 1
        elif i > 0:  # up
            s1_alignment = '*' + s1_alignment
            s2_alignment = _s2[i] + s2_alignment
            i -= 1
        elif j > 0:  # left
            s1_alignment = _s1[j] + s1_alignment
            s2_alignment = '*' + s2_alignment
            j -= 1
    print(s1_alignment)
    print(s2_alignment)

def backtrace():
    s1_alignment = ''
    s2_alignment = ''
    i = len(_s2) - 1
    j = len(_s1) - 1
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            diag = _dp[i - 1][j - 1]
            up = _dp[i - 1][j]
            left = _dp[i][j - 1]
            if (_dp[i][j] - up) == _gap_penalty:
                s1_alignment = '*' + s1_alignment
                s2_alignment = _s2[i] + s2_alignment
                i -= 1
            elif (_dp[i][j] - diag) == h(_s2[i],_s1[j]):
                s1_alignment = _s1[j] + s1_alignment
                s2_alignment = _s2[i] + s2_alignment
                i -= 1
                j -= 1
            elif (_dp[i][j] - left) == _gap_penalty:
                s1_alignment = _s1[j] + s1_alignment
                s2_alignment = '*' + s2_alignment
                j -= 1
        elif i > 0:  # up
            s1_alignment = '*' + s1_alignment
            s2_alignment = _s2[i] + s2_alignment
            i -= 1
        elif j > 0:  # left
            s1_alignment = _s1[j] + s1_alignment
            s2_alignment = '*' + s2_alignment
            j -= 1
    print(s1_alignment)
    print(s2_alignment)

def lalign(s1,s2):
    set_globs(s1.upper(),s2.upper())

    print('h() matrix:')
    print_h_matrix()
    print('DP matrix:')
    fill_l_dp_matrix()
    print_dp_matrix()
    lbacktrace()

def galign(s1,s2):
    set_globs(s1.upper(),s2.upper())

    print('h() matrix:')
    print_h_matrix()
    print('DP matrix:')
    fill_dp_matrix()
    print_dp_matrix()
    backtrace()

lalign(r,l)
lalign(r,g)