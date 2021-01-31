'''
Single Cycle Check from AlgoExpert.io
January 2021 Jakub Kazimierski
'''

def hasSingleCycle(array):
    '''
    You're given an array of integers where
    each integer represents a jump of its
    value in the array. For instance, the integer 2
    represents a jump of two indicies forward in the
    array; the integer -3 represents a jump of three
    indicies backward in the array.

    If a jump spills past the array's bounds, it wraps
    over to the other side. For instance, a jump of -1
    at index 0 brings us to the last index in the array.
    Similarly, a jump of 1 at the last index in the array
    brings us to index 0.

    Write a function that returns a boolean representing whether
    the jumps in the array form a single cycle. A single cycle occurs
    if, starting at any index in the array and following the jumps,
    every element in the array is visited exactly once before landing
    back on the starting index.
    '''

    # time O(n) | space O(1)
    jump_to = array[0]
    array[0] = float("inf")
    idx = jump_to % len(array)

    while array[idx] != float("inf") and idx != 0:
        # at each iteration match visited slot as float(inf)
        jump_to = array[idx]
        array[idx] = float("inf")
        idx = (idx + jump_to)%len(array)
        
    if idx == 0 and all(array[idx] == float("inf")  for idx in range(len(array))):        
        return True

    return False