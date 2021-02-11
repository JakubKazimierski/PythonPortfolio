'''
Sunset Views from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def sunsetViews(buildings, direction):
    '''
    Given an array of buildings and a direction
    that all of the buildings face, return an array
    of the indices of the buildings that can see the
    sunset.
    
    A building can see the sunset if it's strictly taller
    than all of the buildings that come after it in the
    direction ihat it faces.

    The input array named buildings contains positive, non-zero
    integers representing the heights of the buildings. A building
    at index i thus has a height denoted by buildings[i]. All of the 
    buildings face the same direction, and this direction is either
    east or west, denoted by the input string named direction, which
    will always be equal to either 'EAST' or 'WEST'. In relation
    to the input array, you can interpret these directions as right
    for east and left for west.

    Important note: the indicies in the output array should be sorted
    in ascending order.
    '''


    # TIME o(n) | SPACE O(n)
    
    if direction == 'EAST':
        start = len(buildings) - 1 
        end = -1
        iteration_step = -1
    else:
        start = 0
        end = len(buildings)
        iteration_step = 1
        
    output_arr = []
    max_curr_height = 0
    for idx in range(start, end, iteration_step):
        if buildings[idx] > max_curr_height:
            if direction == 'EAST':
                output_arr.insert(0, idx)
            else:
                output_arr.append(idx)

            max_curr_height = buildings[idx]
            
    return output_arr
