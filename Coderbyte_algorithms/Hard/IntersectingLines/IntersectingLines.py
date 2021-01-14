'''
Intersecting Lines from Coderbyte
January 2021 Jakub Kazimierski
'''

from fractions import Fraction

def IntersectingLines(strArr):
    '''
    Have the function IntersectingLines(strArr) 
    take strArr which will be an array of 4 
    coordinates in the form: (x,y). Your 
    program should take these points where 
    the first 2 form a line and the last 2 form a 
    line, and determine whether the lines intersect, 
    and if they do, at what point. 
    
    For example: if strArr is ["(3,0)","(1,4)","(0,-3)","(2,3)"], 
    then the line created by (3,0) and (1,4) and the line created 
    by (0,-3) (2,3) intersect at (9/5,12/5). Your output should 
    therefore be the 2 points in fraction form in the following 
    format: (9/5,12/5). If there is no denominator for the resulting 
    points, then the output should just be the integers like so: (12,3). 
    If any of the resulting points is negative, add the negative sign to 
    the numerator like so: (-491/63,-491/67). If there is no intersection, 
    your output should return the string "no intersection". The input points 
    and the resulting points can be positive or negative integers.
    '''
    
    line_I_a, line_I_b = eval(strArr[0]), eval(strArr[1])
    line_II_a, line_II_b = eval(strArr[2]), eval(strArr[3])

    def tanges_a(point_I, point_II):
        '''
        Returns tanges betwen two points.
        '''
        if point_II[0] != point_I[0]:
            tanges = (point_II[1] - point_I[1])/(point_II[0] - point_I[0])
            return tanges
        else:
            return "no tanges"

    if line_I_a[0] == line_I_b[0] and line_II_a[0] == line_II_b[0]:
        return "no intersection"

    # line equation is  f(x) = tang_a * x + b_factor
    tang_line_I = tanges_a(line_I_a, line_I_b)
    tang_line_II = tanges_a(line_II_a, line_II_b)

    if tang_line_I != "no tanges":
        b_factor_line_I = line_I_a[1] - tang_line_I*line_I_a[0]
    if tang_line_II != "no tanges":
        b_factor_line_II = line_II_a[1] - tang_line_II*line_II_a[0]

    # I assume that it won't be exactly same lines for this task
    if tang_line_I == tang_line_II:
        return "no intersection"

    # f(x) = tang_a * x + b_factor, g(x) = tang2_a * x + b2_factor, so look for f(x) = b(x)
    if tang_line_I == "no tanges":
        x_intersection = float(line_I_a[0])
        y_intersection = float(tang_line_II*x_intersection + b_factor_line_II)
    elif tang_line_II == "no tanges":
        x_intersection = float(line_II_a[0])
        y_intersection = float(tang_line_I*x_intersection + b_factor_line_I)
    else:
        x_intersection = float((b_factor_line_II - b_factor_line_I)/\
            (tang_line_I - tang_line_II))    
        y_intersection = float(tang_line_I*x_intersection + b_factor_line_I)

    return '('+str(Fraction(x_intersection).limit_denominator())+","+\
        str(Fraction(y_intersection).limit_denominator())+')'
