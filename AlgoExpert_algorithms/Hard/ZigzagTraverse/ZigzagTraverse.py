'''
Zigzag Traverse from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def zigzagTraverse(array):
    '''
    Write a function that takes in an 'n' x 'm'
    two-dimensional array (that can be square-shaped when
    n==m) and returns a one-dimensional array of all the array's
    elements in zigzag order.

    Zigzag order starts at te top left corner of the two-dimensional
    array, goes down by one element, and proceeds in a zigzag
    pattern all the way to the bottom right corner.
    '''


    def isOutOfBounds(col_id, row_id, height, width):
        '''
        Returns True if col or row id is out of matrix
        range. Time O(1) | Space O(1)
        '''
        
        return col_id > width or col_id < 0 or row_id < 0 or row_id > height


    col_id = row_id = 0
    goingDown = True
    result = []

    width = len(array[0]) - 1
    height = len(array) - 1

    # below takes O(n) time, and updates result array so space O(n) also
    while not isOutOfBounds(col_id, row_id, height, width):
        result.append(array[row_id][col_id])

        if goingDown:
            if col_id == 0 or row_id == height:
                goingDown = False

                if row_id == height:
                    col_id += 1
                else:
                    row_id += 1
            else:
                row_id += 1
                col_id -= 1
        else:
            if row_id == 0 or col_id == width:
                goingDown = True
                
                if col_id == width:
                    row_id += 1
                else:
                    col_id += 1
            else:
                row_id -= 1
                col_id += 1

    return result


