'''
PowerSetCount from Coderbyte
December 2020 Jakub Kazimierski
'''

from itertools import chain,combinations

def PowerSetCount(arr):
    '''
    Have the function PowerSetCount(arr) 
    take the array of integers stored in arr, 
    and return the length of the power set 
    (the number of all possible sets) 
    that can be generated. 
    
    For example: if arr is [1, 2, 3], 
    then the following sets form the power set:

    []
    [1]
    [2]
    [3]
    [1, 2]
    [1, 3]
    [2, 3]
    [1, 2, 3]

    You can see above all possible sets, 
    along with the empty set, are generated. 
    Therefore, for this input, your program should return 8.
    '''
    
    try:

        # below chains all combinations into one iterable, then converts object into list
        power_set = list(chain(*map(lambda x: combinations(arr, x), range(0, len(arr)+1))))

        return len(power_set)

    except(AttributeError, TypeError):
        return -1

