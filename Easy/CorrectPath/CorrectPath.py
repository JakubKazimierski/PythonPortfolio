'''
Correct Path from Coderbyte
December 2020 Jakub Kazimierski
'''

import operator
from itertools import product

def CorrectPath(strParam):
    '''
    Have the function CorrectPath(str) 
    read the str parameter being passed, 
    which will represent the movements made 
    in a 5x5 grid of cells starting from the top 
    left position. The characters in the input 
    string will be entirely composed of: r, l, u, d, ?. 
    
    Each of the characters stand for the direction to 
    take within the grid, for example: 
    r = right, 
    l = left, 
    u = up, 
    d = down. 
    
    Your goal is to determine what characters 
    the question marks should be in order for 
    a path to be created to go from the top left 
    of the grid all the way to the bottom right 
    without touching previously travelled on cells in the grid.

    For example: if str is "r?d?drdd" 
    then your program should output the 
    final correct string that will allow a 
    path to be formed from the top left of 
    a 5x5 grid to the bottom right. 
    
    For this input, your program should 
    therefore return the string "rrdrdrdd". 
    There will only ever be one correct 
    path and there will always be at least 
    one question mark within the input string.
    '''
    
    # below solution is brute force, so in some cases it won't be fast, but it returns 100% proper way
    try:
        moves_dict = {"u":(-1,0), "r":(0,1), "d":(1,0), "l":(0,-1) }

        unknown_moves = [m for m in list(strParam) if m == "?"]
        
        # itertools.product() creates Cartesian product of input iterables.
        # For example, product(moves_dict, repeat=2) means the same as product(moves_dict, moves_dict).
        # So it returns all possible combinations of available moves
        for permutation in product(moves_dict, repeat=len(unknown_moves)):
            permutation = list(permutation)
            
            path=""
            position = (0, 0)
            visited = [position]

            for move in list(strParam):
                if move == '?':
                    # assign key from permutations of dictionary of moves
                    move = permutation.pop()
                    
                path += move
                # change position after each move
                position = tuple(map(operator.add, position, moves_dict[move]))
            
                if position in visited:
                    break
                # below checks if after move  we are still in 5x5 matrix (indexed from 0 to 4) 
                if max(position) > 4 or min(position) < 0:
                    break

                visited.append(position)

                # end point
                if position == (4,4):
                    return path

    except(AttributeError, TypeError, KeyError):
        return -1

def _input():

    sampleList = "???rrurdr?"

    return sampleList

def _output():

    sampleString = "dddrrurdrd"

    return sampleString
