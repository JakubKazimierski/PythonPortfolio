'''
Three Number Sort from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def threeNumberSort(array, order):
    '''
    You're given an array of integers and 
    another array of three distinct integers.
    The first array is guaranteed to only contain
    integers that are in the second array, and the
    second array represents a desired order for the
    integers in the first array. For example, a second
    array of [x, y, z] represents a desired order
    of [x, x, ..., x, y, y, ..., y, z, z, ..., z]
    in the first array.

    Write a function that sorts the first array according
    to the desired order in the second array.

    The function should perform this in place (i.e. it should
    mutate the input array), and it shouldn't use any auxiliary
    space (i.e it should run with constant space: O(1) space).

    Note that the desired order won't necessarily be ascending or
    descending and that the first array won't necessarily contain
    all three integers found in the second array--it might only
    contain one or two.
    '''

    # O(n) time | O(1) space
    buckets = [0, 0, 0]

    # below conuts occurences of elements
    for elem in array:
       idx_bucket = order.index(elem)
       buckets[idx_bucket] += 1

    start_idx = end_idx = 0
    for idx in range(len(order)):

        end_idx += buckets[idx]
        # below assigns elements in correct order
        for elem_idx in range(start_idx, end_idx):
            array[elem_idx] = order[idx]
        start_idx += buckets[idx]    
    
    return array    