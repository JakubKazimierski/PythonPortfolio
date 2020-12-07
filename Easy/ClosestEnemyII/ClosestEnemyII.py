'''
ClosestEnemyII from Coderbyte
December 2020 Jakub Kazimierski
'''

def ClosestEnemyII(strArr):
    '''
    Have the function ClosestEnemyII(strArr) 
    read the matrix of numbers stored in strArr 
    which will be a 2D matrix that contains only 
    the integers 1, 0, or 2. Then from the position 
    in the matrix where a 1 is, return the number of 
    spaces either left, right, down, or up you must 
    move to reach an enemy which is represented by a 2. 
    You are able to wrap around one side of the matrix 
    to the other as well. For example: if strArr is 
    ["0000", "1000", "0002", "0002"] then this looks like 
    the following:

    0 0 0 0
    1 0 0 0
    0 0 0 2
    0 0 0 2

    For this input your program should return 2 because 
    the closest enemy (2) is 2 spaces away from the 1 
    by moving left to wrap to the other side and then 
    moving down once. The array will contain any number 
    of 0's and 2's, but only a single 1. 
    It may not contain any 2's at all as well, where in 
    that case your program should return a 0.
    '''
    
    # region Attributes
    is_two_in = False

    width = len(strArr)
    lenght = len(strArr[0])

    left_steps = 0
    right_steps = 0

    one_X_coord = 0
    one_Y_coord = 0
    
    steps_list = []

    # endregion

    # below finds one coordinates
    for Y_index in range(0, len(strArr)):
        if "1" in strArr[Y_index]:
            one_X_coord, one_Y_coord = strArr[Y_index].index("1"), Y_index
        if "2" in strArr[Y_index]:
            is_two_in = True    

    go_left = go_right = one_X_coord    

    if is_two_in == True:
        
        # region LookForEnemy

        # below traverses left and right at once
        while left_steps <=3 :

            up_down_steps_r = 0
            up_down_steps_l = 0
            go_up_left = go_down_left = go_up_right = go_down_right = one_Y_coord

            while up_down_steps_l <= 3 :
                if strArr[go_up_left][go_left] == "2" or strArr[go_down_left][go_left] == "2":
                    steps_list.append(left_steps + up_down_steps_l)

                # below traverses up and down at once
                go_up_left = (go_up_left - 1) % lenght
                go_down_left = (go_down_left + 1) % lenght
                up_down_steps_l += 1
            
            while up_down_steps_r <= 3 :
                if strArr[go_up_right][go_right] == "2" or strArr[go_down_right][go_right] == "2":
                    steps_list.append(right_steps + up_down_steps_r)

                # below traverses up and down at once
                go_up_right = (go_up_right - 1) % lenght
                go_down_right = (go_down_right + 1) % lenght
                up_down_steps_r += 1
            
            go_right = (go_right + 1) % width
            go_left = (go_left - 1) % width
            left_steps += 1
            right_steps += 1
        
        return min(steps_list)
        # endregion
    else:
        return 0

def _input():

    sampleInp = ["0000", "2010", "0000", "2002"]

    return sampleInp 

def _output():

    sampleOut = 2

    return sampleOut