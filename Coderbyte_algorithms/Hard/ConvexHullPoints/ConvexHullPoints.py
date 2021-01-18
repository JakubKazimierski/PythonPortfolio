'''
Convex Hull Points from Coderbyte
January 2021 Jakub Kazimierski
'''

import sys

def ConvexHullPoints(strArr):
    '''
    Have the function ConvexHullPoints(strArr) 
    take strArr which will be an array of integer 
    coordinates that exist on a Cartesian plane in 
    the form: (x,y). Your program should return the 
    minimum number of points that are needed to form a 
    convex hull around all the points. 
    
    For example: if the input is ["(2,2)", "(3,1)", "(2,6)", "(0,-2)"] 
    then your program should return 3 because only 3 points are needed 
    to create a convex hull that encloses all the points. The input array 
    will always contain at least 3 points.
    '''
    

    def orientation(p, q, r): 
        ''' 
        To find orientation of ordered triplet (p, q, r).  
        The function returns following values  
        0 --> p, q and r are colinear  
        1 --> Clockwise  
        2 --> Counterclockwise  
        '''
        val = (q.y - p.y) * (r.x - q.x) - \ 
            (q.x - p.x) * (r.y - q.y) 
    
        if val == 0: 
            return 0
        elif val > 0: 
            return 1
        else: 
            return 2

    points_arr = []
    for elem in strArr:
        points_arr.append(eval(elem))



    return 0