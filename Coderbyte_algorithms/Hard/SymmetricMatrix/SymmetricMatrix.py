'''
Symmetric Matrix from Coderbyte
January 2021 Jakub Kazimierski
'''

def SymmetricMatrix(strArr):
    '''
    Have the function SymmetricMatrix(strArr) 
    read strArr which will be an array of integers 
    represented as strings. Within the array there 
    will also be "<>" elements which represent break points. 
    The array will make up a matrix where the 
    (number of break points + 1) represents the number of rows. 
    
    Here is an example of how strArr may look: 
    ["1","0","1","<>","0","1","0","<>","1","0","1"]. There are two 
    "<>", so 2 + 1 = 3. Therefore there will be three rows in the 
    array and the contents will be row1=[1 0 1], row2=[0 1 0] and row3=[1 0 1]. 
    Your program should take the given array of elements, create the proper matrix, 
    and then determine whether the matrix is symmetric, in other words, if matrix M 
    is equal to M transpose. If it is, return the string symmetric and if it isn't 
    return the string not symmetric. A matrix may or may not be a square matrix and 
    if this is the case you should return the string not possible. For the example 
    above, your program should return symmetric.
    '''
    
    string_matrix = ",".join(strArr).split(",<>,")
    matrix = []
    for string in string_matrix:
        matrix.append([int(elem) for elem in string.split(",")])

    if len(matrix) != len(matrix[0]):
        return "not possible"

    transposed = {}

    for row_id in range(len(string_matrix)):        
        transposed[row_id] = []

    for row_id in range(len(matrix)):        
        for col_id in range(len(matrix[row_id])):
            transposed[col_id].append(matrix[row_id][col_id])

    if all(transposed[row] == matrix[row] for row in range(len(matrix))):
        return "symmetric"

    return "not symmetric"    