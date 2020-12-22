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
    
    strArr = strArr.replace("\"", "")
    matrix = list(eval(strArr))
    
    output = []
    # append first element
    output.append(matrix[0][0])

    row_id = 0
    column_id = 0


    down_border = right_border = len(matrix)
    left_border = up_border = 0

    # while all elements are not appended to output list
    while len(output) < len(matrix)**2:


        # increment row id in order not to append previously visited
        row_id += 1

        # append elements while going right
        while row_id < right_border:
            output.append(matrix[column_id][row_id])
            row_id += 1

        # decrement index after while loop
        row_id -= 1    

        # increment column id in order not to append previously visited
        column_id += 1
        # at max right side start traversing down
        while column_id < down_border:
            output.append(matrix[column_id][row_id])
            column_id += 1

        column_id -= 1

        # decrement row id in order not to append previously visited
        row_id -= 1
        # at the bottom start traversing left
        while row_id >= left_border:
            output.append(matrix[column_id][row_id])
            row_id -= 1

        # increment index after while loop
        row_id += 1

        # decrement column id in order not to append previously visited
        column_id -= 1
        # at left bottom start traversing up but first elem is visited
        while column_id > up_border:
            output.append(matrix[column_id][row_id])
            column_id -= 1

        column_id += 1

        # decrement right and down border
        down_border -= 1
        right_border -= 1
        #increment up and left border
        up_border += 1
        left_border += 1

        # continue process for smaller bounds
        # those are not visited elements

    return ",".join(str(num) for num in output)
