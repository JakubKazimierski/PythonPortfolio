'''
TimeConvert from Coderbyte
October 2020 Jakub Kazimierski
'''

import math

def TimeConvert(num):
    '''
    Have the function TimeConvert(num) 
    take the num parameter being passed 
    and return the number of hours and 
    minutes the parameter converts to 
    (ie. if num = 63 then the output should be 1:3). 
    Separate the number of hours and minutes with a colon.
    '''

    if num >= 0:
        # value after colon is rest of divison by 60 
        return ":".join(str(x) for x in [int(num//60), int(num%60)])

    else:
        return -1