'''
MaxSubsetSumNoAdjacent from AlgoExpert.io
January 2021 Jakub Kazimierski
'''

def maxSubsetSumNoAdjacent(array):
    '''
    Write a function that takes in an array
    of positive integers and returns the maximum
    sum of non-adjacent elements in the array.

    If the input array is empty, the function
    should return 0.
    '''
    # dynamic programming approach
    # O(n) time | O(1) space
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[-1]
    
    second = array[0]
    first = max(array[1], second)
    for idx in range(2, len(array)):
        current = max(first, second + array[idx])
        second = first
        first = current
    return first
