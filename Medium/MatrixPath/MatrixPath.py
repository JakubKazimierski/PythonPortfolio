'''
Matrix Path from Coderbyte
December 2020 Jakub Kazimierski
'''

def TraversePath(strArr, id_row, id_column, path):

    moves = [(0,1), (1,0), (0,-1), (-1,0)]

    try:
        for move in moves:
            next_row = id_row + move[0]
            next_column = id_column + move[1]
            if len(strArr) > next_row >= 0 and len(strArr[0]) > next_column >= 0:
                if strArr[next_row][next_column] == '1' and (next_row, next_column) not in path:
                    path.append((next_row, next_column))
                    TraversePath(strArr, next_row, next_column, path)

        return path
    except:
        return    

def MatrixPath(strArr):
    '''
    Have the function MatrixPath(strArr) 
    take the strArr parameter being passed which 
    will be a 2D matrix of 0 and 1's of some arbitrary size, 
    and determine if a path of 1's exists from the top-left of 
    the matrix to the bottom-right of the matrix while moving 
    only in the directions: up, down, left, and right. If a path 
    exists your program should return the string true, otherwise 
    your program should return the number of locations in the matrix 
    where if a single 0 is replaced with a 1, a path of 1's will be 
    created successfully. If a path does not exist and you cannot create 
    a path by changing a single location in the matrix from a 0 to a 1, 
    then your program should return the string not possible. 
    
    For example: if strArr is ["11100", "10011", "10101", "10011"] 
    then this looks like the following matrix:

    1 1 1 0 0
    1 0 0 1 1
    1 0 1 0 1
    1 0 0 1 1

    For the input above, a path of 1's from the top-left to the 
    bottom-right does not exist. But, we can change a 0 to a 1 in 2 places 
    in the matrix, namely at locations: [0,3] or [1,2]. So for this input
    your program should return 2. The top-left and bottom-right of the input 
    matrix will always be 1's.
    '''
    path_start = []
    path_start_neighbours = set()

    path_end = []
    path_end_neighbours = set()

    path_start = TraversePath(strArr, 0, 0, path_start)
    path_end = TraversePath(strArr, len(strArr)-1, len(strArr[0])-1, path_end)
  
    if any(elem == (len(strArr)-1, len(strArr[0])-1) for elem in path_start):
        return "true"
 
    moves = [(0,1), (1,0), (0,-1), (-1,0)]
    for move in moves:    
        for elem in path_start:
            neighbour_row = elem[0] + move[0]
            neighbour_column = elem[1] + move[1]
            if len(strArr) > neighbour_row >= 0 and len(strArr[0]) > neighbour_column >= 0:
                path_start_neighbours.add((neighbour_row, neighbour_column))    

        for elem in path_end:
            neighbour_row = elem[0] + move[0]
            neighbour_column = elem[1] + move[1]
            if len(strArr) > neighbour_row >= 0 and len(strArr[0]) > neighbour_column >= 0:
                path_end_neighbours.add((neighbour_row, neighbour_column))    

    if len(path_start_neighbours.intersection(path_end_neighbours)) > 0:
        return len(path_start_neighbours.intersection(path_end_neighbours))

    return "not possible"    
    
