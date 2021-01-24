'''
Move Element to End from AlgoExpert.io
January 2021  Jakub Kazimierski
'''

def moveElementToEnd(array, toMove):
    '''
    You're given an array of integers and an integer.
    Write a function that moves all instances of that 
    integer in the array to the end of the array
    and returns the array.

    The function should perform this in place(i.e. it should
    mutate the input array) and doesn't need to maintain
    the order of the other integers.
    '''
    
    '''
    # O(n) time | O(n) space
    to_extend = []    
    while toMove in array:
        to_extend.append(array.pop(array.index(toMove)))
    
    array.extend(to_extend)
    return array
    '''

    #O(n) time | O(1) space
    left_id = 0
    right_id = len(array)-1
    while left_id < right_id:
        # right_id stops when toMove elements at right side ends
        while left_id < right_id and array[right_id] == toMove:
            right_id -= 1
        # swao toMove elements with occurences of other elems    
        if array[left_id] == toMove:
            array[left_id], array[right_id] = array[right_id], array[left_id] 
        left_id += 1
    # althought order of other elements is not maintain               
    return array