'''
Powerset from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def powerset(array):
    '''
    Write a function that takes in
    an array of unique integers and
    returns its powerset.

    The powerset P(X) of a set X
    is the set of all subsets of X.
    For example, the powerset of [1, 2]
    is [[], [1], [2], [1, 2]].

    Note that the sets in the powerset do not
    need to be in any particular order.
    '''

    # initialize with empty set
    sets = [[]]

    # Time O((2^n)*n) - 2^n sets and avg len of iteration through set is n/2
    # Space O((2^n)*n)
    for elem in array:
        for idx in range(len(sets)):
            current_set = sets[idx]
            sets.append(current_set + [elem])

    return sets        
