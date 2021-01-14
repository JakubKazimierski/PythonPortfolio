'''
Array Jumping from Coderbyte
January 2021 Jakub Kazimierski
'''

import copy

def ArrayJumping(arr):
    '''
    Have the function ArrayJumping(arr) 
    take the array of numbers stored in 
    arr and first determine the largest 
    element in the array, and then determine 
    whether or not you can reach that same 
    element within the array by moving left 
    or right continuously according to whatever 
    integer is in the current spot. If you can 
    reach the same spot within the array, 
    then your program should output the least 
    amount of jumps it took. 
    
    For example: if the input is [2, 3, 5, 6, 1] 
    you'll start at the spot where 6 is and if you 
    jump 6 spaces to the right while looping around 
    the array you end up at the last element where the 
    1 is. Then from here you jump 1 space to the left 
    and you're back where you started, so your program 
    should output 2. If it's impossible to end up back 
    at the largest element in the array your program 
    should output -1. The largest element in the array 
    will never equal the number of elements in the array. 
    The largest element will be unique.
    '''

    max_elem = max(arr)
    
    elems = [(max_elem, arr.index(max_elem))]
    visited = [(max_elem, arr.index(max_elem))]
    count = 0
    while True:
        nextElems = []
        # all possibilities from point are counted as 1
        for elem in elems:
            right = (elem[1] + elem[0]) % len(arr)
            left = (elem[1] - elem[0]) % len(arr)
            nextElems.append((arr[left], left))
            nextElems.append((arr[right], right))
        elems = copy.copy(nextElems)
        
        count += 1
        if (max_elem, arr.index(max_elem))  in elems:
            break
        
        # if each elem in array + 1 could be checked and max was not found (but i'm not 100% sure)
        if count > len(arr)+1:
          count = -1
          break

    return count 
 
