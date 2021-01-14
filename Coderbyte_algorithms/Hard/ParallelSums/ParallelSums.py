'''
Parallel Sums from Coderbyte
January 2021 Jakub Kazimierski
'''

from itertools import combinations
import copy

def ParallelSums(arr):
    '''
    Have the function ParallelSums(arr) 
    take the array of integers stored in arr 
    which will always contain an even amount 
    of integers, and determine how they can 
    be split into two even sets of integers 
    each so that both sets add up to the 
    same number. If this is impossible return -1. 
    If it's possible to split the array into two sets, 
    then return a string representation of the first set 
    followed by the second set with each integer separated 
    by a comma and both sets sorted in ascending order. 
    The set that goes first is the set with the smallest first integer.

    For example: if arr is [16, 22, 35, 8, 20, 1, 21, 11], 
    then your program should output 1,11,20,35,8,16,21,22
    '''
    
    comb_len = len(arr)//2

    combinations_list = list(combinations(arr, comb_len))

    for comb in combinations_list:
        # create second set by removing from arr elements from first set
        comb_II = copy.copy(arr)
        for elem in comb:
            comb_II.pop(comb_II.index(elem))

        # if sums of those evenly of length combinations are equal
        if sum(comb) == sum(comb_II):
            sorted_comb = sorted(list(comb))
            sorted_comb_II = sorted(list(comb_II))

            output_list = []
            if sorted_comb[0] < sorted_comb_II[0]:
                output_list.extend(sorted_comb)
                output_list.extend(sorted_comb_II)
            else:
                output_list.extend(sorted_comb_II)
                output_list.extend(sorted_comb)

            return ",".join(str(digit) for digit in output_list)

    return -1
                