'''
Overlapping Rectangles from Coderbyte
December 2020 Jakub Kazimierski
'''


def OverlappingRectangles(strArr):
    '''
    Have the function OverlappingRectangles(strArr) 
    read the strArr parameter being passed which will 
    represent two rectangles on a Cartesian coordinate 
    plane and will contain 8 coordinates with the first 4 
    making up rectangle 1 and the last 4 making up rectange 2.
    It will be in the following format: 
    ["(0,0),(2,2),(2,0),(0,2),(1,0),(1,2),(6,0),(6,2)"] 
    Your program should determine the area of the space where the 
    two rectangles overlap, and then output the number of times this 
    overlapping region can fit into the first rectangle. 
    
    For the above example, the overlapping region makes up a rectangle of area 2, 
    and the first rectangle (the first 4 coordinates) makes up a rectangle of area 4, 
    so your program should output 2. The coordinates will all be integers. 
    If there's no overlap between the two rectangles return 0.
    '''
    
    points = eval(strArr[0])

    rec_I_X = set()
    rec_I_Y = set()
    for point in points[:4]:
        rec_I_X.add(point[0]) 
        rec_I_Y.add(point[1]) 

    rec_II_X = set()
    rec_II_Y = set()
    for point in points[4:]:
        rec_II_X.add(point[0]) 
        rec_II_Y.add(point[1])

    if max(rec_I_X) <= min(rec_II_X) or max(rec_I_Y) <= min(rec_II_Y):
        return 0

    area_I = (max(rec_I_X) - min(rec_I_X))*((max(rec_I_Y) - min(rec_I_Y)))    

    common_area = (max(rec_I_X) - min(rec_II_X))*(max(rec_I_Y) - min(rec_II_Y))

    return area_I/common_area
