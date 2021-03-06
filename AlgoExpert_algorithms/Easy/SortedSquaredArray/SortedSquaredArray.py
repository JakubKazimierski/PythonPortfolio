'''
Sorted Squared Array from AlgoExpert.io
March 2021 Jakub Kazimierski
'''

def sortedSquaredArray(array):
    '''
    Write a function that takes in a non-empty
    array of integers that are sorted in ascending
    order and returns a new array of the same length
    with the squares of the original integers also sorted
    in ascending order.
    '''

    # Tine O(n) | space O(n)
    output = [0]*len(array)

    left_id = 0
    right_id = to_insert_r = len(array)-1


    while left_id <= right_id:
        abs_left = abs(array[left_id])
        abs_right = abs(array[right_id])

        if abs_left > abs_right:
            output[to_insert_r] = abs_left*abs_left
            left_id += 1
            to_insert_r -= 1
        else:    
            output[to_insert_r] = abs_right*abs_right
            right_id -= 1
            to_insert_r -= 1

    return output    