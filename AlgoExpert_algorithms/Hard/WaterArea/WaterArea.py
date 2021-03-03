'''
Water Area from AlgoExpert.io
March 2021 Jakub Kazimierski
'''

def waterArea(heights):
    '''
    You're given an array of non-negative
    integers where each non-zero integer
    represents the height of a pillar of
    width 1. Imagine water being poured over
    all of the pillars; write a function that
    returns the surface area of the water
    trapped between the pillars viewed from the front.
    Note that spilled water should be ignored.
    '''

    # O(n) time | O(n) space

    left_highest = []
    right_highest =[]

    water_sum = 0

    curr_left_highest = 0
    curr_right_highest = 0
    for elem in heights:
        left_highest.append(curr_left_highest)    
        if elem > curr_left_highest:
            curr_left_highest = elem


    for elem in reversed(heights):
        right_highest.insert(0, curr_right_highest)        
        if elem > curr_right_highest:
            curr_right_highest = elem


    # water holds on min value of buildings heights
    for idx in range(len(heights)):
        min_height = min(left_highest[idx], right_highest[idx])

        if heights[idx] < min_height:
            water_sum += (min_height-heights[idx])
        else:
            water_sum += 0 

    return water_sum               
