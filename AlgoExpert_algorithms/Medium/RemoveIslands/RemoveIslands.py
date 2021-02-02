'''
Remove Islands from AlgoExpert.io
January 2021 Jakub Kazimierski
'''

def removeIslands(matrix):
    '''
    You're given a two-dimensional array (a matrix)
    of potentially unequal height and width containing
    only 0s and 1s. The matrix represents atwo-toned image,
    where each 1 represents black and each 0 represents white.
    An island is defined as any number of 1's that are horizontally
    or vertically adjacent (but not diagonally adjacent) and that
    don't touch the border of the image. In other words, a group 
    of horizontally or vertically adjacent 1s isn't an island 
    if any of those 1s are in the first row, last row, first column,
    or last column of the input matrix.

    Note that an island can twist. In other words, it doesn't have
    to be a straight vertical line or a straight horizontal line; it
    can be L-shaped, for example.

    You can think of islands as patches of black that don't touch the border
    of the two-toned image.

    Write a function that returns a modified version of the input matrix,
    where all of the islands are removed. You remove an island by replacing
    it with 0s.

    Naturally, you're allowed to mutate the input matrix.
    '''

    def mark_as_two(row_id, col_id):
        '''
        Time O(rows*cols) worst case | space O(1)
        Changes adjacent 1s from border to 2s.
        '''

        matrix[row_id][col_id] = 2

        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for move in moves:
            next_row = row_id + move[0]
            next_col = col_id + move[1]
            if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix[0]):
                if matrix[next_row][next_col] == 1:
                    mark_as_two(next_row, next_col)

    # region bordersCheck
    # below two for loops, checks only borders of matrix for 1s
    # time O(rows+columns) | space O(1)
    for col_id in range(len(matrix[0])):
        if matrix[0][col_id] == 1:
            mark_as_two(0, col_id)
        if matrix[len(matrix)-1][col_id] == 1:
            mark_as_two(len(matrix)-1, col_id)

    for row_id in range(1, len(matrix)-1):
        if matrix[row_id][0] == 1:
            mark_as_two(row_id, 0)
        if matrix[row_id][len(matrix[0])-1] == 1:
            mark_as_two(row_id, len(matrix[0])-1)
    # endregion

    # time O(rows*columns) | space O(1)
    for row_id in range(len(matrix)):
        for col_id in range(len(matrix[row_id])):
            if matrix[row_id][col_id] == 2:
                matrix[row_id][col_id] = 1
            elif matrix[row_id][col_id] == 1:
                matrix[row_id][col_id] = 0            


    return matrix
