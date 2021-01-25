'''
Longest Peak from AlgoExpert.io
January 2021 Jakub Kazimierski
'''

def longestPeak(array):
    '''
    Write a function that takes in an array of integers
    and returns the length of the longest peak in the 
    array.

    A peak is defined as adjacent integers in the array that are
    strictly increasing until they reach a tip (the highest
    value in the peak), at which point they become strictly decreasing.
    At least three integers are required to form a peak.

    For example, the integers 1,4 10, 2 form a peak, but integers
    4, 0, 10 don't and neither do the integers 1, 2, 2, 0. Similiary, the
    integers 1, 2, 3, don't form a peak because there aren't any strictly
    decreasing integers after the 3.
    '''

    # time O(n) | space O(1)
    max_len = 0
    point_left = point_right = 0
    count_middle = 1
    count_left = count_right = 0
    for idx in range(len(array)-2):
        # when peak is found
        if array[idx] < array[idx+1] > array[idx+2]:
            point_left = idx
            point_right = idx + 2
            # count it's left size
            while point_left >= 0 and array[point_left] < array[point_left + 1]:
                point_left -= 1
                count_left += 1
            # count it's right size    
            while point_right < len(array) and array[point_right] < array[point_right - 1]:
                point_right += 1
                count_right += 1

            if count_left + count_right + count_middle > max_len:
                max_len = count_left + count_right + count_middle
                count_left = count_right = 0

    return max_len