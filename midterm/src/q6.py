
D1 = 'TTGATC'
D2 = 'ATCTTG'


def circular_suffix_array(dna_string):
    """
    No need to add a terminal character as circles don't
    end.
    :param dna_string: a dna string
    :return: a circular suffix array of dna_string
    """
    csa = []
    [csa.append(dna_string[substring:] + dna_string[:substring]) for substring in range(len(dna_string))]
    return sorted(csa)

def bwt(dna_string):
    """
    Just ripping the last characters off the circular
    suffix array.
    :param dna_string: a dna string
    :return: a BWT string representation
    """
    csa = circular_suffix_array(dna_string)
    return ''.join([suffix[-1:] for suffix in csa])

def rotations_of_each_other(d1,d2):
    """
    Checking for matching BWT's
    :param d1: a dna string to compare
    :param d2: a dna string to compare
    :return: True if d1,d2 are rotations, else False
    """
    return bwt(d1) == bwt(d2)

print(rotations_of_each_other(D1,D2))