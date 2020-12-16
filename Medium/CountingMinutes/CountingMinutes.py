'''
Counting Minutes from Coderbyte
December 2020 Jakub Kazimierski
'''

import re
from datetime import datetime

def CountingMinutes(strParam):
    '''
    Have the function CountingMinutes(strParam) 
    take the str parameter being passed which will 
    be two times (each properly formatted with a colon 
    and am or pm) separated by a hyphen and return the 
    total number of minutes between the two times. 
    The time will be in a 12 hour clock format. 
    
    For example: if str is 9:00am-10:00am then the 
    output should be 60. If str is 1:00pm-11:00am 
    the output should be 1320.
    '''
    
    # hours : minutes am/pm
    FMT = '%I:%M%p'

    start, stop = re.split(r'-', strParam)[0], re.split(r'-', strParam)[1]

    # time diff, strptime() method creates a datetime object from the given string
    tdelta = datetime.strptime(stop, FMT) - datetime.strptime(start, FMT)

    return tdelta.seconds/60

