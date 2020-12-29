'''
Three Points from Coderbyte
December 2020 Jakub Kazimierski
'''

def ThreePoints(strArr):
    '''
    Have the function ThreePoints(strArr) 
    read the array of strings stored in strArr 
    which will always contain 3 elements and be 
    in the form: ["(x1,y1)", "(x2,y2)", "(x3,y3)"]. 
    Your goal is to first create a line formed by the 
    first two points (that starts from the first point 
    and moves in the direction of the second point and that 
    stretches in both directions through the two points), 
    and then determine what side of the line point 3 is on. 
    The result will either be right, left, or neither. 
    
    For example: if strArr is ["(1,1)", "(3,3)", "(2,0)"] 
    then your program should return the string right because the 
    third point lies to the right of the line formed by the 
    first two points.
    '''

    (x1, y1), (x2, y2), (x3, y3) = map(eval, strArr)
    if y1 == y2: return 'neither'
    
    if x1 == x2: 
        line = x1 
        orient = y2 - y1 > 0
        if x3 > line: return 'right' if orient else 'left'
        if x3 < line: return 'left' if orient else 'right'
        return 'neither'

    a_factor = (y2 - y1) / (x2 - x1)
    b_factor = y1 - a_factor*x1

    line = a_factor*x3 + b_factor
    orient = (x2 - x1) > 0
    
    if y3 < line: return 'right' if orient else 'left'
    if y3 > line: return 'left' if orient else 'right'
    
    return 'neither'
