'''
Maximal Rectangle from Coderbyte
January 2021 Jakub Kazimierski
'''

import numpy as np

def MaximalRectangle(strArr):
    '''
    Have the function MaximalRectangle(strArr) 
    take the strArr parameter being passed which 
    will be a 2D matrix of 0 and 1's, and determine 
    the area of the largest rectangular submatrix that 
    contains all 1's. 
    
    For example: if strArr is ["10100", "10111", "11111", "10010"] 
    then this looks like the following matrix:

    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0

    For the input above, you can see 
    the bolded 1's create the largest rectangular 
    submatrix of size 2x3, so your program should 
    return the area which is 6. You can assume the 
    input will not be empty.
    '''
    
    matrix = []
    for row in strArr:
        matrix.append([int(digit) for digit in list(row)])

    matrix = np.array(matrix)
    
    maximum = 0
    # below checks all possible rectangles
    for row_id in range(matrix.shape[0]):
        for rec_row_id in range(matrix.shape[0]):
            for col_id in range(matrix.shape[1]):
                for rec_col_id in range(matrix.shape[1]):
                    if rec_row_id >= row_id and rec_col_id >= col_id:
                        count_ones = np.sum(matrix[row_id : rec_row_id + 1, col_id : rec_col_id + 1])
                        area = (rec_row_id + 1 - row_id) * (rec_col_id + 1 - col_id)
                        # if rectangle area is created from all 1's
                        if area == count_ones and area > maximum:
                            maximum = area            

    return maximum