'''
PowersOfTwo from Coderbyte
November 2020 Jakub Kazimierski
'''

import math

def PowersOfTwo(num):
    '''
    Have the function PowersofTwo(num) 
    take the num parameter being passed 
    which will be an integer and return 
    the string true if it's a power of two. 
    If it's not return the string false.

    For example if the input is 16 then your 
    program should return the string true but 
    if the input is 22 then the output should 
    be the string false.
    '''


    try:
        # if logarithm of base 2 from absolute value of given number 
        # is integer, diff between float form and int form of result is equal 0
        # and number is power of two
        if math.log2(abs(num)) - int(math.log2(abs(num))) == 0 :
            return "true"
        else:
            return "false"     

    except (AttributeError, TypeError, ValueError):
        return -1    

