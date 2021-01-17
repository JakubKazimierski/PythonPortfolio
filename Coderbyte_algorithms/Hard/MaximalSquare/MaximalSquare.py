'''
Maximal Square from Coderbyte
January 2021 Jakub Kazimierski
'''

def MaximalSquare(strArr):
    '''
    Have the function MaximalSquare(strArr) 
    take the strArr parameter being passed 
    which will be a 2D matrix of 0 and 1's, 
    and determine the area of the largest 
    square submatrix that contains all 1's. 
    A square submatrix is one of equal width 
    and height, and your program should return 
    the area of the largest submatrix that contains 
    only 1's. 
    
    For example: if strArr is 
    ["10100", "10111", "11111", "10010"] 
    then this looks like the following matrix:

    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0

    For the input above, you can see the bolded 1's 
    create the largest square submatrix of size 2x2, 
    so your program should return the area which is 4.
    You can assume the input will not be empty.
    '''

    matrix = []
    for row in strArr:
        matrix.append(list(row))

    max_area = 0
    area_border = 1
    # below increments area border at each iteration
    for length in range(len(matrix)):
        # from each point from which square can fit into matrix 
        # below cheks possible square created from 1's 
        for row_id in range(len(matrix) - length):
            for col_id in range(len(matrix[row_id]) - length):
                is_square = True         

                # below checks square area of given border length
                for right_id in range(0, area_border):
                    for down_id in range(0, area_border):
                        if is_square:
                            if area_border == 1:
                                if matrix[row_id + down_id][col_id + right_id] == '1':
                                    max_area = 1
                            else:
                                if matrix[row_id + down_id][col_id + right_id] == '0':
                                    is_square = False
                if is_square:
                    max_area = area_border**2    

        area_border += 1

    return max_area