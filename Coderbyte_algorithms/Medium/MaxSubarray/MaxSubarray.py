'''
Max Subarray from Coderbyte
December 2020 Jakub Kazimierski
'''

import sys

def MaxSubarray(arr):
    '''
    Have the function MaxSubarray(arr) 
    take the array of numbers stored in 
    arr and determine the largest sum 
    that can be formed by any contiguous 
    subarray in the array. 
    
    For example, if arr is [-2, 5, -1, 7, -3] 
    then your program should return 11 because the 
    sum is formed by the subarray [5, -1, 7]. 
    Adding any element before or after this subarray 
    would make the sum smaller.
    '''

    max_sum = -sys.maxsize - 1

    for start in range(0, len(arr)):
        end = start + 1
        while end <= len(arr):
            possible_max = sum(arr[start:end])
            if possible_max > max_sum:
                max_sum = possible_max
            if end < sys.maxsize:      
                end += 1    

    return max_sum