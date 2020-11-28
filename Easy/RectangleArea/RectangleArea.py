'''
Rectangle Area from Coderbyte
November 2020 Jakub Kazimierski
'''

def RectangleArea(strArr):
    '''
    Have the function RectangleArea(strArr) 
    take the array of strings stored in strArr, 
    which will only contain 4 elements and be in the form (x y) 
    where x and y are both integers, and return the area of 
    the rectangle formed by the 4 points on a Cartesian grid. 
    The 4 elements will be in arbitrary order. 
    
    For example: if strArr is ["(0 0)", "(3 0)", "(0 2)", "(3 2)"] 
    then your program should return 6 because the width of the rectangle 
    is 3 and the height is 2 and the area of a rectangle 
    is equal to the width * height.
    '''

    try:
        # below creates list of X points without repeatition and of int type 
        Xpoints = list(set(map(lambda x:int(x.replace('(','').replace(')','').split(' ')[0]),strArr)))
        
        # below creates list of Y points without repeatition and of int type
        Ypoints = list(set(map(lambda x:int(x.replace('(','').replace(')','').split(' ')[1]),strArr)))
        

        # if len of lists is equal 1, this means that width or height is equal 0
        if len(Xpoints) > 1 and len(Ypoints) > 1: 
            width = abs(Xpoints[0]-Xpoints[1])
            height = abs(Ypoints[0]-Ypoints[1])

            return int(width*height)
        else:
            return 0

    except(AttributeError, TypeError):
        return -1

def _input():

    exampleInput = ["(0 0)", "(3 0)", "(0 2)", "(3 2)"]  

    return exampleInput

def _output():

    exampleOutput = 6

    return exampleOutput      