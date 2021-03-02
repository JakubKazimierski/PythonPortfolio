'''
Min Number Of Jumps from AlgoExpert.io
March 2021 Jakub Kazimierski
'''

def minNumberOfJumps(array):
    '''
    You're given a non-empty array of positive
    integers where each integer represents the 
    maximum number of steps you can take forward
    in the array. For example, if the element at
    index 1 is 3, you can go from index 1 to index 2,
    3 or 4. 

    Write a function that returns the minimum number of jumps
    needed to reach the final index.

    Note that jumping from index i to index i+x always
    constitutes one jump, no matter how large x is.
    
    Jumps are > 0.
    '''

    # dynamic programming approach

    # O(n) space
    jumps = [float('inf')] * len(array)

    jumps[0] = 0

    # loop takes O(n^2) time 
    for idx in range(len(array)-1):
        for jump in range(1, array[idx]+1):
            if idx+jump < len(array) and jumps[idx] + 1 < jumps[idx+jump]:
                jumps[idx+jump] = jumps[idx] + 1

    return jumps[-1]            

    # Total:
    # time O(n^2) | space O(n)