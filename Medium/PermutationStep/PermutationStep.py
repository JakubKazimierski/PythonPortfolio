'''
Permutation Step from Coderbyte
December 2020 Jakub Kazimierski
'''

from itertools import permutations

def PermutationStep(num):
    '''
    Have the function PermutationStep(num) 
    take the num parameter being passed and 
    return the next number greater than num 
    using the same digits. 
    For example: if num is 123 return 132, 
    if it's 12453 return 12534. If a number 
    has no greater permutations, return -1 (ie. 999).
    '''
    
    str_num = str(num)

    # make permutations without repeatitions
    num_permutations = set(permutations(str_num, len(str_num)))
    numbers_from_permutations = []

    for permutation in num_permutations:
        numbers_from_permutations.append(int("".join(permutation)))

    numbers_from_permutations = sorted(numbers_from_permutations)    

    next_greater_id = numbers_from_permutations.index(num) + 1

    if next_greater_id < len(numbers_from_permutations):
        return numbers_from_permutations[next_greater_id]
        
    return -1