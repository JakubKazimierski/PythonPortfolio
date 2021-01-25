'''
Spiral Traverse from AlgoExpert.io
January 2021 Jakub Kazimierski
'''

def spiralTraverse(array):
    '''    
    Write a function that takes in an n x m two-dimensional array (that can be
    square-shaped when n == m) and returns a one-dimensional array of all the
    array's elements in spiral order.
        
    Spiral order starts at the top left corner of the two-dimensional array, goes
    to the right, and proceeds in a spiral pattern all the way until every element
    has been visited.
    '''

    # o(n*m) space (n-rows m-columns)| O(n*m) space
    output = []
    
    start_row = start_col = 0
    end_row = len(array)-1
    end_col = len(array[0])-1
    while start_row <= end_row and start_col <= end_col:

        for idx in range(start_col, end_col+1):
            # traverse right
            output.append(array[start_row][idx])

        for idx in range(start_row + 1, end_row+1):
            # traverse down
            output.append(array[idx][end_col])

        for idx in reversed(range(start_col, end_col)):
            # traverse left
            if start_row == end_row:
                # in order not to repeat values
                break
            
            output.append(array[end_row][idx])

        for idx in reversed(range(start_row+1, end_row)):
            if start_col == end_col:
                # in order not to repeat values
                break

            # traverse up
            output.append(array[idx][start_col])

        start_row += 1
        start_col += 1
        end_col -= 1
        end_row -=1            

    return output
