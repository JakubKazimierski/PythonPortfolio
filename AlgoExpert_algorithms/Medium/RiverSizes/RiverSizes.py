'''
River Sizes from AlgoExpert.io
January 2021 Jakub Kazimierski
'''

def riverSizes(matrix):
    '''
    You're given a two-dimensional array
    (a matrix) of potentially unequal height
    and width containing only 0s and 1s.
    Each 0 represents land, and each 1 represents
    part of a river. A river consist of any number
    of 1s that are either horizontally or vertically
    adjacent (but not diagonally adjacent). The number
    of adjacent 1s forming a river, determines it's size.

    Note that a river can twist. In other words, it doesn't 
    have to be a straight vertical line or a straight horizontal
    line. It can be L-shaped, for example.

    Write a function that returns an array of the sizes of all
    rivers represented in the input matrix. The sizes don't need to
    in any particular order.
    '''

    # time O(columns*rows) | space O(columns*rows)

    def move_cross(row_id, col_id, length):
        '''
        Worst time is O(rows*columns) if all of them are 1's
        Returns length of river-path constructed from 1's.
        '''
        
        # mark visted 1s as 0 in order not to repeat the same path
        matrix[row_id][col_id] = 0
        
        length += 1
        
        # moves right, down, up, left
        moves = [(0,1), (1,0), (-1,0), (0,-1)]

        for move in moves:
            next_row = row_id+move[0]
            next_col = col_id+move[1]
            
            if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix[0]) and\
                matrix[next_row][next_col] == 1:
                return move_cross(next_row, next_col, length)

        return length


    lengths = []
    for row_id in range(len(matrix)):
        for col_id in range(len(matrix[row_id])):
            if matrix[row_id][col_id] == 1:
                lengths.append(move_cross(row_id, col_id, 0))

    return lengths

