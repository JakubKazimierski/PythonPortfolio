'''
Bitmap Holes from Coderbyte
December 2020 Jakub Kazimierski
'''

def pop_connected(row_id, char_id, arr):
    for coord in ((row_id, char_id - 1), (row_id, char_id + 1), (row_id - 1, char_id), (row_id + 1, char_id)):
        try:
            arr.remove(coord)
            # recurency call for removing connected zeros
            pop_connected(coord[0], coord[1], arr)
        
        # if index error occurs
        except: 
            continue

def BitmapHoles(strArr):
    '''
    Have the function BitmapHoles(strArr) 
    take the array of strings stored in strArr, 
    which will be a 2D matrix of 0 and 1's, and 
    determine how many holes, or contiguous regions of 0's, 
    exist in the matrix. A contiguous region is one where there 
    is a connected group of 0's going in one or more of four directions: 
    up, down, left, or right. 
    
    For example: if strArr is ["10111", "10101", "11101", "11111"], 
    then this looks like the following matrix:

    1 0 1 1 1
    1 0 1 0 1
    1 1 1 0 1
    1 1 1 1 1

    For the input above, your program should return 2 because there are 
    two separate contiguous regions of 0's, which create "holes" in the matrix. 
    You can assume the input will not be empty.
    '''

    zero_coords = []
    for row_id, row in enumerate(strArr):
        for char_id, char in enumerate(row):
            if char  == '0':
                zero_coords.append((row_id, char_id))
 

    count = 0
    while zero_coords:
        count += 1
        row_id, char_id = zero_coords.pop(0)
        pop_connected(row_id, char_id, zero_coords)

    return count 