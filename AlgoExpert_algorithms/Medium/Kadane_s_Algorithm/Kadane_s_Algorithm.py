'''
Kadane's Algorithm from AlgoExpert.io
January 2021 Jakub Kazimierski
'''

def kadanesAlgorithm(array):
    '''
    Write a function that takes in a non-empty
    array of integers and returns the maximum
    sum that can be obtained by summing up all
    of the integers in a non-empty subarray of
    the input array. A subarray must only contain
    adjacent numbers (numbers next to each other
    in the input array)
    '''

    # time O(n) | space O(1)
    current_sum = array[0]
    max_sum = current_sum
    # below finds all max subarrays sums, and remember the greatest one
    for idx in range(1, len(array)):
        current_sum = max(current_sum+array[idx], array[idx])
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum