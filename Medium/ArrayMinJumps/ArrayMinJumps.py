'''
Array Min Jumps from Coderbyte
December 2020 Jakub Kazimierski
'''
import sys

def min_Jumps_l(arr):
    '''
    Bottom up approach. O(n^2)
    '''
    
    jumps = [0 for i in range(len(arr))]
 
    if len(arr) == 0 or arr[0] == 0:
        return sys.maxsize
 
    jumps[0] = 0
 
    # Find the minimum number of 
    # jumps to reach arr[index] from 
    # arr[0] and assign this 
    # value to jumps[index]
    for index in range(1, len(arr)):
        jumps[index] = sys.maxsize
        for previous_id in range(index):
            # if index is in range of jump
            if (index <= previous_id + arr[previous_id]) and (jumps[previous_id] != sys.maxsize):
                jumps[index] = min(jumps[index], jumps[previous_id] + 1)
                break
    return jumps[-1]


   

def ArrayMinJumps(arr):
    '''
    Have the function ArrayMinJumps(arr) 
    take the array of integers stored in arr, 
    where each integer represents the maximum number 
    of steps that can be made from that position, 
    and determine the least amount of jumps that can 
    be made to reach the end of the array. 
    
    For example: if arr is [1, 5, 4, 6, 9, 3, 0, 0, 1, 3] 
    then your program should output the number 3 
    because you can reach the end of the array from the beginning 
    via the following steps: 1 -> 5 -> 9 -> END or
    1 -> 5 -> 6 -> END. 
    Both of these combinations produce a series of 3 steps. 
    And as you can see, you don't always have to take the maximum 
    number of jumps at a specific position, you can take less jumps 
    even though the number is higher.

    If it is not possible to reach the end of the array, return -1.
    '''

    output = min_Jumps_l(arr)

    if output == sys.maxsize:
        return -1

    return output
