'''
Longest Matrix Path from Coderbyte
December 2020 Jakub Kazimierski
'''

def LongestMatrixPath(strArr):
    '''
    Have the function LongestMatrixPath(strArr) 
    take the array of strings stored in strArr, 
    which will be an NxM matrix of positive single-digit 
    integers, and find the longest increasing path composed 
    of distinct integers. When moving through the matrix, 
    you can only go up, down, left, and right. 
    
    For example: if strArr is ["345", "326", "221"], 
    then this looks like the following matrix:

    3 4 5
    3 2 6
    2 2 1

    For the input above, the longest increasing path 
    goes from: 3 -> 4 -> 5 -> 6. Your program should 
    return the number of connections in the longest path, 
    so therefore for this input your program should return 3. 
    There may not necessarily always be a longest path within the matrix.
    '''
    
    matrix = [[int(digit) for digit in row] for row in strArr]

    rows, columns = len(matrix), len(matrix[0])
    path_from_points = [[0] * columns for i in range(rows)]

    def find_longest(row_id, column_id):
        '''
        Nested function (can use variables of LongestMatrixPath(strArr)).
        Uses recurency to find longest possible sequence in matrix.
        '''
        # for unvisited points
        if path_from_points[row_id][column_id] == 0:

            val = matrix[row_id][column_id]
            # get lenght of longest sequence, traverse in all directions
            path_from_points[row_id][column_id] = 1 + max(
                # if there is no next elem in sequence returns 0, but each step is counted in recurency call by
                # path_from_points[row_id][column_id] = 1 + max(...)
                find_longest(row_id - 1, column_id) if row_id > 0 and val > matrix[row_id - 1][column_id] else 0,
                find_longest(row_id + 1, column_id) if row_id < row_id - 1 and val > matrix[row_id + 1][column_id] else 0,
                find_longest(row_id, column_id - 1) if column_id > 0 and val > matrix[row_id][column_id - 1] else 0,
                find_longest(row_id, column_id + 1) if column_id < columns - 1 and val > matrix[row_id][column_id + 1] else 0)
        
        return path_from_points[row_id][column_id]
        
    # do not count starting element in sequence
    return max(find_longest(row_id, column_id) for row_id in range(rows) for column_id in range(columns)) - 1

