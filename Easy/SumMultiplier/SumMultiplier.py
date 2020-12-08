'''
Sum Multiplier from Coderbyte
December 2020 Jakub Kazimierski
'''

from itertools import combinations
import operator


def SumMultiplier(arr):
    '''
    Have the function SumMultiplier(arr) 
    take the array of numbers stored in arr 
    and return the string true if any two 
    numbers can be multiplied so that the 
    answer is greater than double the sum of 
    all the elements in the array. If not, 
    return the string false. 
    
    For example: if arr is 
    [2, 5, 6, -6, 16, 2, 3, 6, 5, 3] 
    then the sum of all these elements is 42 
    and doubling it is 84. 
    There are two elements in the array, 
    16 * 6 = 96 and 96 is greater than 84, 
    so your program should return the string true.
    '''
    try:
        double_sum_arr = sum(arr)*2

        pair_combinations = list(combinations(arr, 2))

        for pair in pair_combinations:
            if operator.mul(pair[0], pair[1]) > double_sum_arr:
                return "true"

        return "false"

    except(TypeError):
        return -1    