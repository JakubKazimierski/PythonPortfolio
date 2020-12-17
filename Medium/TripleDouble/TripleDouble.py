'''
Triple Double from Coderbyte
December 2020 Jakub Kazimierski
'''

def TripleDouble(num1,num2):
    '''
    Have the function TripleDouble(num1,num2) 
    take both parameters being passed, and return 
    1 if there is a straight triple of a number at 
    any place in num1 and also a straight double of 
    the same number in num2. 
    
    For example: if num1 equals 451999277 and 
    num2 equals 41177722899, then return 1 because 
    in the first parameter you have the straight 
    triple 999 and you have a straight double, 99, 
    of the same number in the second parameter. 
    If this isn't the case, return 0.
    '''
    
    for num in set(str(num1)):
        if str(num) * 3 in str(num1) and str(num) * 2 in str(num2):
            return 1

    return 0

