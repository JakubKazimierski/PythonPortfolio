'''
First Duplicate Value from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def firstDuplicateValue(array):
    '''
    Given an array of integers between 1 and n,
    inclusive, where n is the length of the array,
    write a function that returns the first integer that
    appears more than once (when the array is read from
    left to right)
    
    In other words, out of all the integers that might occur
    more than once in the input array, your function should
    return the one whose first duplicate value has the minimum
    index.

    If no integer appears more than once, your function should return -1.

    Note that you're allowed to mutate the input array.
    '''

    '''
    # O(n) time | O(n) space
    visited = []
    while len(array) > 0:
        check_elem = array.pop(0)

        if check_elem in visited:
            return check_elem

        visited.append(check_elem)    

    return -1
    '''

    # O(n) time | O(1) space
    # tricky one solution (use feature there is 1...n numbers and n slots)

    for idx in range(len(array)):

        visited = abs(array[idx])
        # assign index according to value
        proper_order_idx = visited - 1
        
        # first negative value is first duplicate
        if array[proper_order_idx] < 0:
            return visited

        # make value at that index  negative (that means this index was visited)
        array[proper_order_idx] = -1*array[proper_order_idx]


    return -1