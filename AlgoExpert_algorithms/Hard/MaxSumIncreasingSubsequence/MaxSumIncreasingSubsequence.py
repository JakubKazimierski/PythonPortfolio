'''
Max Sum Increasing Subsequence from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def maxSumIncreasingSubsequence(array):
    '''
    Write a function that takes in a non-empty
    array of integers and returns the greatest
    sum that can be generated from a strictly
    increasing subsequence in the array as well 
    as an array of the numbers in that subsequence.

    A subsequence of an array is a set of numbers
    that aren't necessarily adjacent in the array
    but that are in the same order as they appear
    in the array. For instance, the numbers [1, 3, 4]
    form a subsequence of the array [1, 2, 3, 4] and
    so do the numbers [2, 4]. Note that a singlee number 
    in an array and the array itself are both valid subsequences
    of the array.

    You can assume that there will only be one increasing subsequence
    with the greatest sum.
    '''

    # Dynamic programming approach

    indexes_sequence = [None] * len(array)
    max_sums = []

    max_sum = array[0]
    max_sum_idx = 0
    out_sequence = []

    # O(n^2) time | O(n) space
    for idx in range(len(array)):
        max_sums.append(array[idx])
        
        for idx_2 in range(0, idx):
            if array[idx_2] < array[idx]:
                curr_sum = max_sums[idx_2] + array[idx]
                if  curr_sum > max_sums[idx]:
                    max_sums[idx] = curr_sum
                    indexes_sequence[idx] = idx_2

                if max_sums[idx] > max_sum:
                    max_sum = max_sums[idx]
                    max_sum_idx = idx

    # O(n) time | O(n) space
    while indexes_sequence[max_sum_idx] != None:
        out_sequence.insert(0, array[max_sum_idx])
        max_sum_idx = indexes_sequence[max_sum_idx]
    out_sequence.insert(0, array[max_sum_idx])
    
    return [max_sum, out_sequence]    

    




