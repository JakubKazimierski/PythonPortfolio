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
    

    # O(n) time | O(n) space
    to_extend = []    
    while toMove in array:
        to_extend.append(array.pop(array.index(toMove)))
    
    array.extend(to_extend)
    return array

