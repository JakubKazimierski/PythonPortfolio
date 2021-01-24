'''
Smallest Differene from AlgoExpert.com
January 2021 Jakub Kazimierski
'''

def smallestDifference(arrayOne, arrayTwo):
    '''
    Write a function that takes in two non-empty arrays
    of integers, finds the pair of numbers (one from each array)
    whose absolute difference is closest to zero, and returns an array
    containing these two numbers, with the number from the first
    array in the first position.

    Note that the absolute differnce of two integers is the distance 
    between them on the real number line. For example, the absolute
    difference of -5 and 5 is 10, and the absolute difference of 
    -4 and -5 is 1.

    You can assume that there will only be one pair of numbers with
    the smallest difference.
    '''
    
    # time O(n*log(n) + m*log(m)) n legth of first arr, m second one
    # space O(1)
    arrayOne.sort()
    arrayTwo.sort()

    # as arrays are sorted if pointers increments
    # values of these pointers increments also
    pointer_One_id = pointer_Two_id = 0
    min_diff = float("inf")
    pair = []

    
    curr_diff = abs(arrayOne[pointer_One_id] - arrayTwo[pointer_Two_id])
    
    while pointer_One_id < len(arrayOne) and pointer_Two_id < len(arrayTwo):
        curr_diff = abs(arrayOne[pointer_One_id] - arrayTwo[pointer_Two_id])
        if curr_diff < min_diff:
            min_diff = curr_diff
            pair = [arrayOne[pointer_One_id], arrayTwo[pointer_Two_id]]
        
        if arrayOne[pointer_One_id] < arrayTwo[pointer_Two_id]:
            pointer_One_id += 1
        else:
            pointer_Two_id += 1


    return pair