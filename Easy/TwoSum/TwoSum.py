'''
Two Sum from Coderbyte
December 2020 Jakub Kazimierski
'''

from itertools import chain, combinations

def all_subsets(arr):
    '''
    Returns chain of all possible combinations
    of elements in given at input array
    ''' 
    return list(combinations(arr[1:], 2))

def TwoSum(arr):
    '''
    Have the function TwoSum(arr) 
    take the array of integers stored in arr, 
    and determine if any two numbers 
    (excluding the first element) in the array 
    can sum up to the first element in the array. 
    
    For example: if arr is [7, 3, 5, 2, -4, 8, 11], 
    then there are actually two pairs that sum to the number 7: 
    [5, 2] and [-4, 11].
    Your program should return all pairs, with the numbers 
    separated by a comma, in the order the first number appears 
    in the array. 
    Pairs should be separated by a space. 
    So for the example above, your program would return: 5,2 -4,11

    If there are no two numbers that 
    sum to the first element in the array, return -1
    '''
    try:
        possible_combinations = list(all_subsets(arr))
        valid_pair_list = []
        string_pair_list = []
        
        for pair in possible_combinations:
            if sum(pair) == arr[0]:
                valid_pair_list.append(pair)

        if len(valid_pair_list) != 0:
            for pair in valid_pair_list:
                string_pair_list.append(",".join(str(number) for number in pair))
            
            return " ".join(string_pair for string_pair in string_pair_list)

        else:
            return -1
            
    except(AttributeError, TypeError):
        return -2


def _input():

    exampleInput = [7, 3, 5, 2, -4, 8, 11]

    return exampleInput

def _output():

    exampleOutput = "5,2 -4,11"

    return exampleOutput  