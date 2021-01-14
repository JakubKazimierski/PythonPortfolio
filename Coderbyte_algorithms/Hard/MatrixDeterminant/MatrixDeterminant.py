'''
Matrix Determinant from Coderbyte
January 2021 Jakub Kazimierski
'''

# deepcopy copies the nested lists, so it is a recursive copy. 
# With just copy, you have a new outer list, but inner lists are references.
from copy import deepcopy

def MatrixDeterminant(strArr):
    '''
    Have the function MatrixDeterminant(strArr)
    read strArr which will be an array of integers 
    represented as strings. Within the array there will 
    also be "<>" elements which represent break points. 
    The array will make up a matrix where the 
    (number of break points + 1) represents the number of rows. 
    
    Here is an example of how strArr may look: ["1","2","<>","3","4"]. 
    The contents of this array are row1=[1 2] and row2=[3 4]. Your program 
    should take the given array of elements, create the proper matrix, and 
    then calculate the determinant. 
    
    For the example above, your program should return -2. If the matrix is 
    not a square matrix, return -1. The maximum size of strArr will be a 6x6 
    matrix. The determinant will always be an integer.
    '''
    
    string_matrix = ",".join(strArr).split(",<>,")

    matrix = []
    for elem in string_matrix:
        matrix.append([int(digit) for digit in elem.split(",")])

    if len(matrix) != len(matrix[0]):
        return -1

    def cut_matrix(matrix, row_id, col_id):
        '''
        Returns matrix smaller by 1 (both rows and columns)
        relatively to row_id and col_id given at input.
        '''
        matrix_to_cut = deepcopy(matrix)

        matrix_to_cut.remove(matrix_to_cut[row_id])
        for row_in_column in range(len(matrix_to_cut)):
            matrix_to_cut[row_in_column].remove(matrix_to_cut[row_in_column][col_id])

        return matrix_to_cut


    def determinant(matrix):
        '''
        By recurency, count determinant of square matrix.
        '''
        if len(matrix) == 2:
            determ = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
            return  determ

        final_val = 0
        for col_id in range(len(matrix[0])):
            smaller_matrix = cut_matrix(matrix, 0, col_id)
            # recurency go to smaller matrix till it get 2x2 matrix
            final_val += (-1)**(0 + col_id) * matrix[0][col_id] * determinant(smaller_matrix)

        return final_val

    return determinant(matrix)