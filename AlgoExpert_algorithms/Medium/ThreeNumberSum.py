'''
Three Number Sum from ALgoExpert.com
January 2021 Jakub Kazimierski
'''


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
    triplets = []

    for elem in array:
        second_target = targetSum - elem
        for elem_II in array:
            if elem_II != elem:
                final_target = second_target - elem_II
                if final_target != elem and final_target != elem_II:
                    if final_target in array and\
                        sorted([elem, elem_II, final_target]) not in triplets:
                        triplets.append(sorted([elem, elem_II, final_target]))                        
    return sorted(triplets)
