'''
Number Of Ways To Traverse Graph from AlgoExpert.io
February 2021 Jakub Kazimierski



You're given two positive integers representing the width and height of a
grid-shaped, rectangular graph. Write a function that returns the number of
ways to reach the bottom right corner of the graph when starting at the top
left corner. Each move you take must either go down or right. In other words,
you can never move up or left in the graph.


For example, given the graph illustrated below, with width = 2 and
height = 3. there are three ways to reach the bottom right corner
when starting at the top left corner:
  _ _
 |_|_|
 |_|_|
 |_|_|

1. Down, Down, Right
2. Right, Down, Down
3. Down, Right, Down

Note: you may assume that width * height >= 2. In other words,
the graph will never be a 1x1 grid.
'''

# Newton formula based approach
# def numberOfWaysToTraverseGraph(width, height):
#     '''
#     O(width + height) time | O(1) space
#     Permutation based approach.
#     '''
#     x_ways_right = width - 1
#     y_ways_down = height - 1

#     def factorial(num):
#         '''
#         O(num) time | o(1) space
#         Returns factorial of numebr.
#         '''

#         factorial = 1

#         for number in range(2, num+1):
#             factorial = factorial*number

#         return factorial

#     # newton fomula
#     factor_up = (factorial(x_ways_right+y_ways_down))
#     factor_down = (factorial(x_ways_right)*factorial(y_ways_down))
#     return factor_up//factor_down    


# Recurency approach
# def numberOfWaysToTraverseGraph(width, height):
#     '''
#     O(2^(width + height)) time | O(width+height) space
#     Recurency based approach.
#     '''

#     if width == 1 or height == 1:
#         return 1

#     return numberOfWaysToTraverseGraph(width - 1, height) + numberOfWaysToTraverseGraph(width, height - 1)

def numberOfWaysToTraverseGraph(width, height):
    '''
    O(width * height) time | O(width * height) space
    Dynamic Programming based approach.
    '''

    num_of_ways = [[0]*width]*height

    for row_id in range(height):
        for col_id in range(width):
            if col_id == 0 or row_id == 0:
                num_of_ways[row_id][col_id] = 1
            else:
                num_of_ways[row_id][col_id] = num_of_ways[row_id - 1][col_id] +\
                    num_of_ways[row_id][col_id - 1]
    
    return num_of_ways[height-1][width-1]                



