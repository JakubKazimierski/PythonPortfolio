'''
Array Addition from Coderbyte
December 2020 Jakub Kazimierski
'''

from itertools import combinations, chain

def ArrayAddition(arr):
    '''
    Have the function ArrayAddition(arr) 
    take the array of numbers stored in arr 
    and return the string true if any combination 
    of numbers in the array (excluding the largest number) 
    can be added up to equal the largest number in the array, 
    otherwise return the string false. 
    
    For example: if arr contains [4, 6, 23, 10, 1, 3] the output 
    should return true because 4 + 6 + 10 + 3 = 23. The array will 
    not be empty, will not contain all the same elements, and may 
    contain negative numbers.
    '''
    
    max_num = max(arr)

    arr.pop(arr.index(max_num))

    # below chains all combinations into one iterable
    combinations_list = chain(*map(lambda x: combinations(arr, x), range(1, len(arr)+1)))

    for combination in combinations_list:
        if sum(combination) == max_num:
            return "true" 

    return "false"     