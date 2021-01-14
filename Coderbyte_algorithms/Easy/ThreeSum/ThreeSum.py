'''
Three Sum from Coderbyte
December 2020 Jakub Kazimierski
'''

from itertools import combinations, chain

def ThreeSum(arr):
    '''
    Have the function ThreeSum(arr) 
    take the array of integers stored in arr, 
    and determine if any three distinct numbers 
    (excluding the first element) in the array 
    can sum up to the first element in the array. 
    
    For example: if arr is [8, 2, 1, 4, 10, 5, -1, -1]
    then there are actually three sets of triplets that 
    sum to the number 8: [2, 1, 5], [4, 5, -1] and [10, -1, -1]. 
    
    Your program should return the string true if 3 
    distinct elements sum to the first element, 
    otherwise your program should return the string false. 
    The input array will always contain at least 4 elements.
    '''
    try:
        sums_of_three = [sum(three) for three in list(combinations(arr[1:], 3))]

        for element in sums_of_three:
            if element == arr[0]:
                return "true" 
            
        return "false"

    except(AttributeError, TypeError):
        return -1

