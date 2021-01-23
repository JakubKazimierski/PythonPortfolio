'''
Three Number Sum from ALgoExpert.com
January 2021 Jakub Kazimierski
'''

from itertools import combinations

def threeNumberSum(array, targetSum):
    '''
    Write a function that takes in a non-empty array of distinct integers
    and an integer representing a target sum. The function should find
    all triplets in the array that sum up to the target sum
    and return a two-dimensional array of all these triplets.

    The numbers in each triplet should be ordered in ascending
    order, and the triplets themselves should be ordered in ascending
    order with respect to the numbers they hold.

    If no three numbers sum up to the target sum, the function
    should return an empty array.
    '''
    
    comb = combinations(array, 3)
    triplets = []
    for combination in comb:
        if sum(list(combination)) == targetSum:
            triplets.append(sorted(list(combination)))

    return sorted(triplets)
