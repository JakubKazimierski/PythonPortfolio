'''
Longest Matrix Path from Coderbyte
December 2020 Jakub Kazimierski
'''

def TraverseLongest(matrix, path, row_id, column_id):

    moves = [(0,1), (0,-1), (1,0), (-1,0)]

    for move in moves:
        next_row = row_id + move[0]
        next_column = column_id + move[1]

        # if next elem exists in matrix, and is greater by 1 than previous
        if len(matrix) > next_row >= 0 and len(matrix[0]) > next_column >= 0:
            if int(matrix[next_row][next_column]) == int(matrix[row_id][column_id])+1:
                # increment path each time, after finding next num in sequence
                path.append(matrix[next_row][next_column])
                TraverseLongest(matrix, path, next_row, next_column)

    return path        

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
    
    paths_lenghts = []
    for row_id in range(0, len(strArr)):
        for column_id in range(0, len(strArr[row_id])):
            path = []
            paths_lenghts.append(TraverseLongest(strArr, path, row_id, column_id))


    return len(max(paths_lenghts, key=len))
