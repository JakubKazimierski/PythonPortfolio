'''
Closest Enemy from Coderbyte
December 2020 Jakub Kazimierski
'''

def ClosestEnemy(arr):
    '''
    Have the function ClosestEnemy(arr) 
    take the array of numbers stored in arr 
    and from the position in the array where a 1 is, 
    return the number of spaces either left or right 
    you must move to reach an enemy which is represented by a 2. 
    
    For example: if arr is [0, 0, 1, 0, 0, 2, 0, 2] 
    then your program should return 3 because the closest enemy (2) is 3 
    spaces away from the 1. 
    The array will contain any number of 0's and 2's, 
    but only a single 1. It may not contain any 2's at all as well, 
    where in that case your program should return a 0.
    '''

    try:
        
        closest_enemy_spaces = []
        go_left = go_right = position_of_one = arr.index(1)


        while go_left > 0 :
            go_left -= 1
            if arr[go_left] == 2: 
                closest_enemy_spaces.append(position_of_one - go_left)
                break

        while go_right < len(arr)-1 :
            go_right += 1
            if arr[go_right] == 2:
                closest_enemy_spaces.append(go_right - position_of_one)
                break
        
        if len(closest_enemy_spaces) != 0:
            return min(closest_enemy_spaces)

        return 0

    except(AttributeError, TypeError):
        return -1
        
