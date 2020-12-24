'''
Trapping Water from Coderbyte
December 2020 Jakub Kazimierski
'''

def TrappingWater(arr):
    '''
    Have the function TrappingWater(arr) 
    take the array of non-negative integers 
    stored in arr, and determine the largest 
    amount of water that can be trapped. The 
    numbers in the array represent the height 
    of a building (where the width of each building is 1) 
    and if you imagine it raining, water will be trapped between 
    the two tallest buildings. 
    
    For example: if arr is [3, 0, 0, 2, 0, 4]
    then this array of building heights looks like 
    the following picture if we draw it out:
    
                   __
     __           |  |
    |  |     __   |  |
    |  |    |  |  |  |
    |  |____|  |__|  |

    Now if you imagine it rains and water gets trapped 
    in this picture, then it'll look like the following 
    (the x's represent water):

                   __
     __           |  |
    |  |XXXXXXXXXX|  |
    |  |XXXX|  |XX|  |
    |  |XXXX|  |XX|  |

    This is the most water that can be trapped in 
    this picture, and if you calculate the area you get 10, 
    so your program should return 10.
    '''

    
    lower_buildings  = 0
    water_amount = 0

    width = 1
    left_height = arr[0]
    for height in arr[1:]:

        width += 1

        # store lower heights
        if  left_height > height:
            lower_buildings += height

        # if next height is greater equal, than left height
        # count water as product of whole area minus buildings,
        # right border height is at max left height for counting 
        if left_height <= height:
            water_amount += \
                ((width*left_height) - lower_buildings - 2*left_height)
            width = 1
            lower_buildings = 0
            left_height = height

    return water_amount