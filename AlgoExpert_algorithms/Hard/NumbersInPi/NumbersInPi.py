'''
Numbers In Pi from AlgoExpert.io
March 2021 Jakub Kazimierski
'''

def numbersInPi(pi, numbers):
    '''        
    Given a string representation of the first n 
    digits of Pi and a list of positive integers 
    (all in string format), write a function that 
    returns the smallest number of spaces that can be 
    added to the n digits of Pi such that all resulting 
    numbers are found in the list of integers.
    
    Note that a single number can appear multiple times 
    in the resulting numbers. For example, if Pi is "3141"
    and the numbers are ["1", "3", "4"], the number "1"
    is allowed to appear twice in the list of resulting 
    numbers after three spaces are added: "3 | 1 | 4 | 1".

    If no number of spaces to be added exists such that all
    resulting numbers are found in the list of integers, the
    function should return -1.
    '''

    numbersTable = {number : True for number in numbers}
    minSpaces = getMinSpaces(pi, numbersTable, {}, 0)

    return -1 if minSpaces == float("inf") else minSpaces

def getMinSpaces(pi, numbersTable, cache, idx):
    '''
    Recurency method, based on dynamic programming
    approach finds minimum num of spaces.
    Time O(n^3) | space O(n + m) where n is length of pi
    and m is num of nubers in numbers Table.
    '''    

    if idx == len(pi):
        return -1
    if idx in cache:
        return cache[idx]
    minSpaces = float("inf")

    for idx_2 in range(idx, len(pi)):
        prefix = pi[idx : idx_2+1]
        
        if prefix in numbersTable:
            minSpacesSuffix = getMinSpaces(pi, numbersTable, cache, idx_2+1)
            # our base case cover this situation with returning -1 at the end
            minSpaces = min(minSpaces, minSpacesSuffix+1)

    cache[idx] = minSpaces
    return cache[idx]
