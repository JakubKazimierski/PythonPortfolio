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
    
    try: 
        # this is cool
        return min(int(''.join(perm)) for perm in permutations(str(num)) if int(''.join(perm)) > num)
    except: 
        return -1
