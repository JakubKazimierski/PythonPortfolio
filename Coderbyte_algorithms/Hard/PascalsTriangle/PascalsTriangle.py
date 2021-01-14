'''
Pascals Triangle from Coderbyte
January 2021 Jakub Kazimierski
'''

import scipy.special

def PascalsTriangle(arr):
    '''
    Have the function PascalsTriangle(arr) 
    take arr which will be a partial row from 
    Pascal's triangle. Pascal's triangle starts 
    with a [1] at the first row of the triangle. 
    Then the second row is [1,1] and the third row is 
    [1,2,1]. The next row begins with 1 and ends with 1, 
    and the inside of the row is determined by adding 
    the k-1 and kth elements from the previous row. 
    The next row in the triangle would then be [1,3,3,1], 
    and so on. 
    
    The input, arr will be some almost completed 
    row from the triangle, for example [1,4,6,4] and your 
    program should return the next element in that row. 
    In this example your program should return 1. 
    
    Another example: if arr is [1,5,10] your program should 
    return 10. If the whole row is entered as input and 
    there is no next number, your program should return -1.

    The input array will contain at least 3 elements so
    [1] and [1,1] will not occur as inputs.
    '''
    
    # The binomial coefficient (n b) appears as the bth entry 
    # in the nth row of Pascal's triangle, b and n indexing from 0
    row_len = len(arr)
    row_num = arr[1]
    output = int(scipy.special.binom(row_num, row_len))

    # if number of possible combinations  is 0, that means bth entry > num_row
    return -1 if output == 0 else output