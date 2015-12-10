
#representing the tree as a list of nested tuples
S = [
    ('T',
     (('','ATT$'),
      ('','T$'),
      ('','$'))
    ),
    ('A',
     (('','ATATT$'),
     ('T',
      (('','ATT$'),
      ('','T$'))))
    ),
    ('','$')]

L = 0 # label
D = 1 # data

def terminal(node):
    """
    # is this a terminal node?
    :param node: a node in a suffix tree
    :return: True if node is terminal, else False
    """
    return node[L] == ''

def distinct_substr_counter(st):
    """
    Classic BFS w inner node & terminal node length counting.
    By summing the lengths of the inner nodes of our tree and
    our terminal (leaf) nodes, we are able to count the distinct
    substrings of our suffix tree. This leverages the non-redundant
    structure of the tree and is able to achieve a runtime of O(n).
    """
    count = 0
    for node in st: # bound by 2 x |S| (Bioinformatics Algorithms Volume 2, p. 131)
        if terminal(node):
            count += len(node[D]) - 1
        else:
            count += len(node[L])
            """
            I'm unsure how Python handles this but it can be performed in
            constant time in a language that allows direct memory access (C/C++).
            We just need to append a reference to this node to the list we're
            iterating over.
            """
            [st.append(x) for x in node[D]]
    return count

print(distinct_substr_counter(S))