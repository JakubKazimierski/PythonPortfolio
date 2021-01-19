'''
Validate Subsequence from AlgoExpert.com
January 2021 Jakub Kazimierski
'''


def validateSubsequence(input_arr, input_seq):
    '''
    Given two non-empty arrays of integers, 
    write a function that determines whether 
    the second array is a subsequence of the first one.
    
    A subsequence of an array is a set of numbers that 
    aren't necessarily adjacent in the array but that 
    are in the same order as they appear in the array. For
    instance, the numbers [1, 3, 4]  form a subsequence of 
    the array [1, 2, 3, 4], and so do the numbers [2, 4]. Note
    that a single number in an array and the array itself are 
    both valid subsequences of the array.
    '''

    if len(input_seq) > len(input_arr) \
        or len(input_arr) == 0 or len(input_seq) == 0:
        return False

    ordered_seq = []
    while len(input_arr) > 0 and len(ordered_seq) < len(input_seq):
        elem = input_arr.pop(0)
        if elem in input_seq:
            ordered_seq.append(elem)

    if ordered_seq == input_seq:
        return True

    return False
