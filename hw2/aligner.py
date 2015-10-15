# usage: python aligner.py query_seq [base_seq]
import os
import sys

# see https://github.com/joshuaburkhart/Riviere/blob/master/app/controllers/task_controller.rb

__author__ = 'joshuaburkhart'
_base_seq = 'ATCTATATATATATGGGGGGGGGGG'

if len(sys.argv) < 2:
    print("query plz")
    exit()
elif len(sys.argv) > 3:
    print("check usage plz")
    exit()
elif len(sys.argv) == 3:
    _base_seq = sys.argv[2]

_gap_const = -2
_query_seq = sys.argv[1]
_hydrophobic = 'CAGVILMTKHYWF'
print(_query_seq)
print(_base_seq)
choice = 0

_dp_matrix = [[x for x in range(len(_query_seq))] for x in range(len(_base_seq))]

def dp_access(i,j):
    if i < 0 and j < 0:
        return 0
    elif i < 0:
        return _gap_const
    elif j < 0:
        return _gap_const
    else:
        return _dp_matrix[i][j]

def h(x,y):
    if x == y:
        return 5
    elif x in _hydrophobic and y in _hydrophobic:
        return 1
    elif x in _hydrophobic or y in _hydrophobic:
        return -5
    else:
        return 0

def fill_dp_matrix():
    global _dp_matrix
    for i in range(len(_base_seq)):
        for j in range(len(_query_seq)):
            _dp_matrix[i][j] = \
                max(dp_access(i-1,j-1) + h(_base_seq[i],_query_seq[j]),
                    dp_access(i-1,j) + _gap_const,
                    dp_access(i,j-1) + _gap_const)

def print_h_matrix():
    for c in range(len(_query_seq)):
        print('{0}'.format(_query_seq[c]).center(4,' '),end='')
    print()
    for i in range(len(_base_seq)):
        print('{0}'.format(_base_seq[i]),end='')
        for j in range(len(_query_seq)):
            print('{0}'.format(h(_base_seq[i],
                                 _query_seq[j])).center(4,' '),end='')
        print()

def print_dp_matrix():
    for c in range(len(_query_seq)):
        print('{0}'.format(_query_seq[c]).center(4,' '),end='')
    print()
    for i in range(len(_base_seq)):
        print('{0}'.format(_base_seq[i]),end='')
        for j in range(len(_query_seq)):
            print('{0}'.format(_dp_matrix[i][j]).center(4,' '),end='')
        print()

def print_backtrack():
    a_base_seq = ''
    a_query_seq = ''
    i = len(_base_seq) - 1
    j = len(_query_seq) - 1
    while i >= 0 or j >= 0:
            choice = max(dp_access(i-1,j-1),
                         dp_access(i,j-1),
                         dp_access(i-1,j))

            if choice == dp_access(i-1,j-1):
                global choice
                #print('diagonal, choice={0}, b:{1}, q:{2}'.format(choice,a_base_seq,a_query_seq))
                if i < 0:
                    a_base_seq = '-' + a_base_seq
                else:
                    a_base_seq = _base_seq[i] + a_base_seq
                if j < 0:
                    a_query_seq = '-' + a_query_seq
                else:
                    a_query_seq = _query_seq[j] + a_query_seq
                i -= 1
                j -= 1
            elif choice == dp_access(i,j - 1):
                global choice
                #print('left, choice={0}, b:{1}, q:{2}'.format(choice,a_base_seq,a_query_seq))
                a_query_seq = _query_seq[j] + a_query_seq
                if dp_access(i,j-1)>dp_access(i,j):
                    a_base_seq = '-' + a_base_seq
                else:
                    a_base_seq = _base_seq[i] + a_base_seq
                    i -= 1
                j -= 1
            else:
                global choice
                #print('up, choice={0}, b:{1}, q:{2}'.format(choice,a_base_seq,a_query_seq))
                a_base_seq = _base_seq[i] + a_base_seq
                if dp_access(i-1,j)>dp_access(i,j):
                    a_query_seq = '-' + a_query_seq
                else:
                    a_query_seq = _query_seq[j] + a_query_seq
                    j -= 1
                i -= 1
    print(a_query_seq)
    print(a_base_seq)

print('base_seq: {0}'.format(_base_seq))
print('query_seq: {0}'.format(_query_seq))
print('h matrix:')
print_h_matrix()
print('dp matrix:')
dp_matrix = fill_dp_matrix()
print_dp_matrix()
print_backtrack()




