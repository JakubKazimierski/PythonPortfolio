'''
Matrix Spiral from Coderbyte
December 2020 Jakub Kazimierski
'''

def MatrixSpiral(strArr):
    '''
    Have the function MatrixSpiral(strArr) 
    read the array of strings stored in strArr 
    which will represent a 2D N matrix, and your 
    program should return the elements after printing 
    them in a clockwise, spiral order. You should return 
    the newly formed list of elements as a string with 
    the numbers separated by commas. 
    
    For example: if strArr is "[1, 2, 3]", "[4, 5, 6]", "[7, 8, 9]"
    then this looks like the following 2D matrix:

    1 2 3
    4 5 6
    7 8 9

    So your program should return the elements of this matrix in a clockwise, 
    spiral order which is: 1,2,3,6,9,8,7,4,5
    '''
    
    # evaluate input to integers array
    matrix = []
    for row in strArr:
        row = eval(row)
        matrix.append(row)
    
    rows = len(matrix)
    columns = len(matrix[0])
     
    # ranges of moves 
    border_top = 1
    border_bottom = rows-1
    border_left = 0
    border_right = columns-1

    # Up = "U", Right = "R", Down = "D", Left = "L"
    direction = 'R'
    row = column = 0
    output = []
    
    # in range of length of all elements in matrix
    for _ in range(rows*columns):
        
        output.append(str(matrix[row][column]))

        # change direction when element get max range       
        if direction == 'R':
            if column == border_right: 
                direction = 'D'
                # after raching border, decrement it's range
                border_right -= 1
            else: column += 1

        if direction == 'D':
            if row == border_bottom:
                direction = 'L'
                border_bottom -= 1
            else: row += 1

        if direction == 'L':
            if column == border_left:
                direction = 'U'
                border_left += 1
            else: column -= 1
            
        if direction == 'U':
            if row == border_top:
                direction = 'R'
                border_top += 1
                column += 1
            else: row -= 1
    
    
    return ','.join(output)
