'''
Binary Search from AlgoExpert.com
January 2021 Jakub Kazimierski
'''

def binarySearch(array, target):
    '''
    Write a function that takes in a sorted array of integers
    as well as a target integer. The function should use the 
    Binary Search algorithm to determine if the target integer is
    contained in the array and should return its index if it is, 
    otherwise -1.
    '''

    # Time O(log(n)) | space O(1)
    L_pivot_id = 0
    R_pivot_id = len(array)-1
    median_id = (L_pivot_id + R_pivot_id)//2

    if array[L_pivot_id] == target:
        return L_pivot_id
    if array[R_pivot_id] == target:
        return R_pivot_id
            
    while abs(L_pivot_id - R_pivot_id) > 1:
        if array[median_id] < target:
            L_pivot_id = median_id
        elif array[median_id] > target:
            R_pivot_id = median_id
        else:
            return median_id

        median_id = (L_pivot_id + R_pivot_id)//2    

    return -1