'''
Charlie the Dog from Coderbyte
December 2020 Jakub Kazimierski
'''

import sys
import itertools

def countSteps(pos1, pos2):
    '''
    Counts steps in matrix grid from point to point.
    '''
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

def CharlieTheDog(strArr):
    '''
    Have the function CharlietheDog(strArr) 
    read the array of strings stored in strArr 
    which will be a 4x4 matrix of the characters 
    'C', 'H', 'F', 'O', where C represents Charlie the dog, 
    H represents its home, F represents dog food, and O represents 
    and empty space in the grid. Your goal is to figure out the least 
    amount of moves required to get Charlie to grab each piece of food 
    in the grid by moving up, down, left, or right, and then make it home 
    right after. Charlie cannot move onto the home before all pieces of 
    food have been collected. 
    
    For example: if strArr is ["FOOF", "OCOO", "OOOH", "FOOO"], 
    then this looks like the following grid:
     _____
    |f   f|
    | c   |
    |    h|
    |f    |     
    '''''''
    For the input above, the least amount of steps 
    where the dog can reach each piece of food, 
    and then return home is 11 steps, so your program should 
    return the number 11. The grid will always contain between 
    1 and 8 pieces of food.
    '''

    foodArr = []

    for i in range(len(strArr)):
        for j in range(len(strArr[0])):
            if strArr[i][j] == 'F':
                foodArr.append((i,j))
            elif strArr[i][j] == 'C':
                start = (i,j)
            elif strArr[i][j] == 'H':
                end = (i,j)

    # permutations of order of gaining food
    routes = list(itertools.permutations(foodArr))

    minSteps = sys.maxsize

    for route in routes:
        steps = countSteps(start, route[0]) + countSteps(end, route[-1])
        for index in range(len(route) - 1):
            steps += countSteps(route[index], route[index+1])
        if steps < minSteps:
            minSteps = steps

    return minSteps

