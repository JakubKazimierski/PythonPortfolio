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
    # O(n^2) time | O(n) space
    array.sort()
    triplets = []

    for index in range(len(array)-2):
        # if left index increments sum has to increment also
        left_p = index + 1
        # if right pointer decreases sum has to decrease also
        right_p = len(array)-1

        while left_p < right_p:
            currSum = array[index] + array[left_p] + array[right_p]

            if currSum == targetSum:
                triplets.append([array[index], array[left_p], array[right_p]])
                left_p += 1
                right_p -= 1
            elif currSum < targetSum:
                left_p += 1
            else:
                right_p -= 1

    return triplets


