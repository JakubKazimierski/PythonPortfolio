'''
Tetris Move from Coderbyte
January 2021 Jakub Kazimierski
'''

from copy import deepcopy

def TetrisMove(strArr):
    '''
    Have the function TetrisMove(strArr) 
    take strArr parameter being passed which 
    will be an array containing one letter 
    followed by 12 numbers representing a Tetris 
    piece followed by the fill levels for the 12 
    columns of the board. Calculate the greatest 
    number of horizontal lines that can be completed 
    when the piece arrives at the bottom assuming it 
    is dropped immediately after being rotated and moved 
    horizontally from the top. Tricky combinations of 
    vertical and horizontal movements are excluded. 
    The piece types are represented by capital letters.
    
    Picture_1.png

    For example, with an input of 
    ["L","3","4","4","5","6","2","0","6","5","3","6","6"], 
    the board will look something like this:

    Picture_2.png

    Your result should be 3 because the L piece can be rotated 
    and dropped in column 6-7 which will complete 3 full rows of blocks.
    '''

    def check_filled_rows(matrix):
        '''
        Returns amount of filled rows.
        '''
        count_filled = 0
        for row_id in range(len(matrix)):
            if all(matrix[row_id][col_id] == 1 \
                for col_id in range(len(matrix[row_id]))):
                    count_filled += 1
        return count_filled            

    # dictionary contains indexes of picturing blocks in matrix (relative to (row_id, col_id) from it is created)
    rotation_I = {"I":[(0,0), (1, 0), (2, 0), (3, 0)], "J":[(0,0), (1, 0), (2, 0), (2, -1)],\
        "L":[(0,0), (0, 1), (1, 1), (2, 1)], "O":[(0,0), (0, 1), (1, 1), (1, 0)], "S":[(0,0), (1, 0), (1, 1), (2, 1)],\
            "T":[(0,0), (1, 0), (1, -1), (2, 0)], "Z":[(0,0), (1, 0), (1, -1), (2, -1)]}

    rotation_II = {"I":[(0,0), (1, 0), (2, 0), (3, 0)], "J":[(0,0), (0, 1), (1, 0), (2, 0)],\
        "L":[(0,0), (1, 0), (2, 0), (2, 1)], "O":[(0,0), (0, 1), (1, 1), (1, 0)], "S":[(0,0), (1, 0), (1, 1), (2, 1)],\
            "T":[(0,0), (1, 0), (1, 1), (2, 0)], "Z":[(0,0), (1, 0), (1, -1), (2, -1)]}

    rotation_III = {"I":[(0,0), (0, 1), (0, 2), (0, 3)], "J":[(0,0), (0, 1), (0, 2), (-1, 0)],\
        "L":[(0,0), (0, 1), (0, 2), (-1, 2)], "O":[(0,0), (0, 1), (1, 1), (1, 0)], "S":[(0,0), (0, 1), (-1, 1), (-1, 2)],\
            "T":[(0,0), (0, 1), (-1, 1), (0, 2)], "Z":[(0,0), (0, 1), (1, 1), (1, 2)]}

    rotation_IV = {"I":[(0,0), (0, 1), (0, 2), (0, 3)], "J":[(0,0), (0, 1), (0, 2), (1, 2)],\
        "L":[(0,0), (0, 1), (0, 2), (1, 0)], "O":[(0,0), (0, 1), (1, 1), (1, 0)], "S":[(0,0), (0, 1), (-1, 1), (-1, 2)],\
            "T":[(0,0), (0, 1), (1, 1), (0, 2)], "Z":[(0,0), (0, 1), (1, 1), (1, 2)]}

    rotations = [rotation_I, rotation_II, rotation_III, rotation_IV]

    matrix_area = []
    for row in range(10):
        matrix_area.append([])
        for column in range(12):
            matrix_area[-1].append(0)

    maxes = []
    for rotation in rotations:
        block_parameters = rotation[strArr[0]]

        # below fills 1's as blocks into area
        index = 0
        for block in strArr[1:]:
            for row_id in range(1, int(block) + 1):
                matrix_area[(-1)*row_id][index] = 1
            index += 1    

        max_filled_rows = 0
        for row_id in range(len(matrix_area)):
            for col_id in range(len(matrix_area[row_id])):
                # if block fits into area and does not conflict with rendered blocks
                if all( 0 <= row_id + param[0] < len(matrix_area) and\
                    0 <= col_id + param[1] < len(matrix_area[row_id])\
                        and matrix_area[row_id + param[0]][col_id + param[1]] + 1< 2\
                            for param in block_parameters):
                                    # fill copy of matrix with 1 at place where block is
                                temp_matrix = deepcopy(matrix_area)
                                for param in block_parameters:
                                    temp_matrix[row_id + param[0]][col_id + param[1]] = 1
                                    # count filled rows
                                temp_filled = check_filled_rows(temp_matrix)
                                if max_filled_rows < temp_filled:
                                    max_filled_rows = temp_filled
        maxes.append(max_filled_rows)
    
    return max(maxes)
