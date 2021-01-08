'''
Noughts Determiner from Coderbyte
January 2021 Jakub Kazimierski
'''

def NoughtsDeterminer(strArr):
    '''
    Have the function NoughtsDeterminer(strArr) 
    take the strArr parameter being passed which will 
    be an array of size eleven. The array will take 
    the shape of a Tic-tac-toe board with spaces 
    strArr[3] and strArr[7] being the separators ("<>") 
    between the rows, and the rest of the spaces will be either 
    "X", "O", or "-" which signifies an empty space. 
    
    So for example strArr may be 
    ["X","O","-","<>","-","O","-","<>","O","X","-"]. 
    This is a Tic-tac-toe board with each row separated 
    double arrows ("<>"). Your program should output the 
    space in the array by which any player could win by 
    putting down either an "X" or "O". In the array above, 
    the output should be 2 because if an "O" is placed in 
    strArr[2] then one of the players wins. Each board 
    will only have one solution for a win, not multiple 
    wins. You output should never be 3 or 7 because 
    those are the separator spaces.
    '''

    # board is 3x3 matrix
    matrix = [row.split(",") for row in ",".join(strArr).split(",<>,")]

    def check_horizontal(matrix, first_row, col_id):
        
        if first_row == 0:
            second_row = row_id + 1
            third_row = row_id + 2
            
        elif first_row == 1:
            second_row = row_id - 1
            third_row = row_id + 1
        else:
            second_row = row_id - 1
            third_row = row_id -2        

        if matrix[second_row][col_id] == matrix[third_row][col_id] and\
            matrix[second_row][col_id] in ["O", "X"]:
            return True

        return False

    def check_vertical(matrix, row_id, first_col):
        
        if first_col == 0:
            second_col = first_col + 1
            third_col = first_col + 2
            
        elif first_col == 1:
            second_col = first_col - 1
            third_col = first_col + 1
        else:
            second_col = first_col - 1
            third_col = first_col -2        

        if matrix[row_id][second_col] == matrix[row_id][third_col] and\
            matrix[row_id][second_col] in ["O", "X"]:
            return True

        return False

    def check_oblique(matrix, first_row, firs_col):
        count_X = 0
        count_O = 0
        is_point_in_line = False        
        for index in range(3):
            if matrix[index][index] == "X":
                count_X += 1
            elif matrix[index][index] == "O":
                count_O += 1
            else:
                if first_row == firs_col == index:
                    is_point_in_line = True   

        row = 0
        count_X = 0
        count_O = 0
        for index in range(2, -1, -1):
            if matrix[row][index] == "X":
                count_X += 1
            elif matrix[row][index] == "O":
                count_O += 1
            else:
                if first_row == row and firs_col == index:
                    is_point_in_line = True   
            row += 1

        if is_point_in_line and (count_O == 2 or count_X == 2):
            return True

        return False



    for row_id in range(len(matrix)):
        for col_id in range(len(matrix[0])):
            if matrix[row_id][col_id] == "-":
                if check_horizontal(matrix, row_id, col_id) or\
                check_vertical(matrix, row_id, col_id) or\
                check_oblique(matrix, row_id, col_id):
                    if row_id == 0:
                        return col_id
                    elif row_id == 1:
                        return col_id + 1 + 3
                    else:
                        return col_id + 1 + 6
                        
    return -1