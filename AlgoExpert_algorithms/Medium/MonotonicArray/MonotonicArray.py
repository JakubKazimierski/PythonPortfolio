'''
Monotonic Array from AlgoExpert.com
January 2021 Jakub Kazimierski
'''

def monotonicArray(array):
    '''
    Write a function that takes in an array of integers
    and returns a boolean representing whether array 
    is monotonic.

    An array is said to be monotonic if its elements, from left
    to right, are entirely nonincreasing or entirely non-decreasing
   
    Non-increasing elements aren't necessarily exclusively decreasing; they simply
    don't increase. Similarly, non-decreasing elements aren't necessarily
    exclusively increasing; they simply don't decrease.

    Note that empty arrays and arrays of one element are monotonic.
    '''


    # time O(n) | space O(1)
    if len(array) < 3:
        return True

    # determine if array is increasing or decreasing
    direction = array[0] - array[1]
    for index in range(1, len(array)-1):
        # if it is not possible to determine direction
        # assign as direction first non zero difference
        if direction == 0:
            if (array[index] - array[index+1]) != direction:
                direction = (array[index] - array[index+1])
                continue
            
        # if array changes it's monotonic return false
        if (array[index] - array[index+1]) * direction < 0:
            return False

    return True
