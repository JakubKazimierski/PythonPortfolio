'''
Simple Mode from Coderbyte
December 2020 Jakub Kazimierski
'''

from collections import Counter


def SimpleMode(arr):
    '''
    Have the function SimpleMode(arr) 
    take the array of numbers stored in 
    arr and return the number that appears 
    most frequently (the mode). For example: 
    if arr contains [10, 4, 5, 2, 4] the output 
    should be 4. If there is more than one mode 
    return the one that appeared in the array first 
    (ie. [5, 10, 10, 6, 5] should return 5 because 
    it appeared first). If there is no mode return -1. 
    The array will not be empty.
    '''

    counted_el = Counter(arr)

    # most common returns tuple in list
    if counted_el.most_common(1)[0][1] > 1:
        return counted_el.most_common(1)[0][0]

    return -1    
    