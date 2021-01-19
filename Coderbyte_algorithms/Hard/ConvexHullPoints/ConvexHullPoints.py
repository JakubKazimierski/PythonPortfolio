'''
Convex Hull Points from Coderbyte
January 2021 Jakub Kazimierski
'''

import sys

def orientation(point_I, point_II, point_III): 
    ''' 
    To find orientation of ordered triplet (point_I, point_II, point_III).  
    The function returns following values  
    0 --> point_I, point_II and point_III are colinear  
    1 --> Clockwise  
    2 --> Counterclockwise  
    
    Slope of line segment (p1, p2): σ = (y2 - y1)/(x2 - x1)
    Slope of line segment (p2, p3): τ = (y3 - y2)/(x3 - x2)
    '''
    val = (point_II[1] - point_I[1]) * (point_III[0] - point_II[0]) -\
         (point_II[0] - point_I[0]) * (point_III[1] - point_II[1]) 

    if val == 0: 
        return 0
    elif val > 0: 
        return 1
    else: 
        return 2

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

    hull = []
    min_point = (sys.maxsize, sys.maxsize)
    points_arr = []
    for elem in strArr:
        points_arr.append(eval(elem))

    # find top left_down point
    for point in points_arr:
        if point[0] < min_point[0] and point[1] < min_point[1]:
            min_point = point


    point_I_id = points_arr.index(min_point) 
    point_II_id = 0
    while(True): 
          
        # Add current point to result  
        hull.append(point_I_id) 
  
        ''' 
        Search for a point 'q' such that orientation(p, x,  
        q) is counterclockwise for all points 'x'. The idea  
        is to keep track of last visited most counterclock-  
        wise point in q. If any point 'i' is more counterclock-  
        wise than q, then update q.  
        '''
        point_II_id = (point_I_id + 1) % len(points_arr) 
  
        for point_index in range(len(points_arr)): 
              
            # If point_index is more counterclockwise  
            # than current point_II_id, then update point_II_id  
            if(orientation(points_arr[point_I_id], points_arr[point_index], points_arr[point_II_id]) == 2): 
                point_II_id = point_index 
  
        ''' 
        Now q is the most counterclockwise with respect to p  
        Set p as q for next iteration, so that q is added to  
        result 'hull'  
        '''
        point_I_id = point_II_id 
  
        # While we don't come to first point 
        if(point_I_id ==  points_arr.index(min_point)): 
            break


    return len(hull)