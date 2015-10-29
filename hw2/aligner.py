import sys

# see https://github.com/joshuaburkhart/Riviere/blob/master/app/controllers/task_controller.rb

__author__ = 'joshuaburkhart'

if len(sys.argv) < 3:
    print('Please supply two queries, S1 and S2')
    exit()
elif len(sys.argv) > 3:
    print('Usage: python aligner.py S1 S2\nExample: python aligner.py GWWPDT WRRKHY')
    exit()

_gap_penalty = -2
_s1 = sys.argv[1]
_s2 = sys.argv[2]
_hydrophobic = 'CAGVILMTKHYWF'
print(_s1)
print(_s2)

_s1 = ' ' + _s1
_s2 = ' ' + _s2

# create DP matrix with S1 + 1 columns and S2 + 1 rows
_dp = [[0 for x in range(len(_s1) + 1)] for x in range(len(_s2) + 1)]


def h(x, y):
    if x == ' ' or y == ' ':
        return _gap_penalty
    elif x == y:
        return 5
    elif x in _hydrophobic and y in _hydrophobic:
        return 1
    elif x in _hydrophobic or y in _hydrophobic:
        return -5
    else:
        return 0


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
                s1_alignment = '-' + s1_alignment
                s2_alignment = _s2[i] + s2_alignment
                i -= 1
            elif (_dp[i][j] - diag) == h(_s2[i],_s1[j]):
                s1_alignment = _s1[j] + s1_alignment
                s2_alignment = _s2[i] + s2_alignment
                i -= 1
                j -= 1
            elif (_dp[i][j] - left) == _gap_penalty:
                s1_alignment = _s1[j] + s1_alignment
                s2_alignment = '-' + s2_alignment
                j -= 1
        elif i > 0:  # up
            s1_alignment = '-' + s1_alignment
            s2_alignment = _s2[i] + s2_alignment
            i -= 1
        elif j > 0:  # left
            s1_alignment = _s1[j] + s1_alignment
            s2_alignment = '-' + s2_alignment
            j -= 1
    print(s1_alignment)
    print(s2_alignment)


print('S1: {0}'.format(_s1))
print('S2: {0}'.format(_s2))
print('h() matrix:')
print_h_matrix()
print('DP matrix:')
fill_dp_matrix()
print_dp_matrix()
backtrace()
