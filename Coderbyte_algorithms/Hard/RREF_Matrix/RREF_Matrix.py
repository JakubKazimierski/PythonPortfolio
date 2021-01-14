'''
RREF Matrix from Coderbyte
January 2021 Jakub Kazimierski
'''

def RREF_Matrix(strArr):
    '''
    Have the function RREFMatrix(strArr) 
    take strArr which will be an array of 
    integers represented as strings. Within 
    the array there will also be "<>" elements 
    which represent break points. The array 
    will make up a matrix where the (number of 
    break points + 1) represents the number of rows. 
    
    Here is an example of how strArr may look: 
    ["5","7","8","<>","1","1","2"]. There is one "<>", 
    so 1 + 1 = 2. Therefore there will be two rows in 
    the array and the contents will be row1=[5 7 8] and 
    row2=[1 1 2]. Your program should take the given array 
    of elements, create the proper matrix, and then through 
    the process of Gaussian elimination create a reduced row 
    echelon form matrix (RREF matrix). For the array above, 
    the resulting RREF matrix would be: row1=[1 0 3], row2=[0 1 -1]. 
    Your program should return that resulting RREF matrix in string 
    form combining all the integers, like so: "10301-1". The matrix 
    can have any number of rows and columns (max=6x6 matrix and min=1x1 matrix). 
    The matrix will not necessarily be a square matrix. If the matrix is an nx1 
    matrix it will not contain the "<>" element. The integers in the array will 
    be such that the resulting RREF matrix will not contain any fractional numbers.
    '''
    
    rows = ",".join(strArr).split(",<>,")
    
    matrix = []

    for row in rows:
        matrix.append([int(elem) for elem in row.split(",")])

    def rref(matrix):
        '''
        Based on https://en.wikipedia.org/wiki/Row_echelon_form

        # comments are based on algorithm description from pseudocode
        
        Function does not return value, it's editing given matrix
        '''
        pivot = 0
        for row_id in range(len(matrix)):
            if pivot >= len(matrix[0]):
                return 
            temp_row = row_id
            while matrix[temp_row][pivot] == 0:
                temp_row += 1
                if temp_row == len(matrix):
                    temp_row = row_id
                    pivot += 1
                    if pivot == len(matrix[0]):
                        return 
            if temp_row != row_id:
                matrix[temp_row], matrix[row_id] = matrix[row_id], matrix[temp_row]
            
            divisor = matrix[row_id][pivot]
            for elem_id in range(len(matrix[row_id])):
                # Divide row matrix[row_id] by matrix[row_id][pivot]
                matrix[row_id][elem_id] = matrix[row_id][elem_id] // divisor

            for row_id_II in range(len(matrix)):
                if row_id_II != row_id:
                    #  Subtract matrix[row_id_II][pivot] multiplied by row matrix[row_id] from row matrix[row_id_II]
                    factor = matrix[row_id_II][pivot]
                    for elem_id in range(len(matrix[row_id_II])):
                        matrix[row_id_II][elem_id] = matrix[row_id_II][elem_id] - \
                            matrix[row_id][elem_id]*factor
            pivot += 1

    rref(matrix)
    return "".join("".join(map(str,elem)) for elem in matrix) 