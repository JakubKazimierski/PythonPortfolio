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
    point_I, point_II, point_III = eval(strArr[0]), eval(strArr[1]), eval(strArr[2])

    if point_I[0] != point_II[0]:
        tanges_a = (point_II[1] - point_I[1])/(point_II[0] - point_I[0])

        if tanges_a == 0:
            return "neither"
        b_factor = point_I[1] - point_I[0]*tanges_a

        if tanges_a*point_III[0] + b_factor == point_III[1]:
            return "neither"
        if tanges_a > 0:   
            if tanges_a*point_III[0] + b_factor > point_III[1]:
                return "right"
            if tanges_a*point_III[0] + b_factor < point_III[1]:
                return "left"        
        else:
            if tanges_a*point_III[0] + b_factor > point_III[1]:
                return "left"
            if tanges_a*point_III[0] + b_factor < point_III[1]:
                return "right"        

    else: 
        if point_III[0] > point_I[0]:
            return "right"
        elif point_III[0] < point_I[0]:
            return "left"
        else:
            return "neither"     


