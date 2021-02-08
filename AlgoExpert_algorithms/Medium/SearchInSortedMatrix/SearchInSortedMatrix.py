'''
Search In Sorted Matrix from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def searchInSortedMatrix(matrix, target):
    '''
    You're given a two-dimensional array (a matrix)
    of distinct integers and a target integer.
    Each row in the matrix is sorted, and each column
    is also sorted; the matrix doesn't necessarily have
    the same height and width.

    Write a function that returns an array of the row
    and column indices of the target integer if it's
    contained in the matrix, otherwise [-1, -1].
    '''

    row_id = 0
    col_id = len(matrix[row_id])-1

    # below traverses matrix from up right corner
    # to the left down, at worst case
    # Time O(rows+columns) | Space O(1)
    while row_id <= len(matrix)-1 and col_id >= 0:
        if matrix[row_id][col_id] > target:
            col_id -= 1
        elif matrix[row_id][col_id] < target:
            row_id += 1
        else:
            return [row_id, col_id]

    # if target was not found
    return [-1, -1] 

    
                   