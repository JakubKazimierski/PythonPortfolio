'''
CountingMinutesI From Coderbyte
Implementation with datetaime() function
November 2020 Jakub Kazimierski
'''

import re
from datetime import datetime

def CountingMinutesI(strParam):
    '''
    Have the function CountingMinutesI(str) 
    take the str parameter being passed which 
    will be two times (each properly formatted with a colon and am or pm) 
    separated by a hyphen and return the total number of minutes between 
    the two times. The time will be in a 12 hour clock format. 
    For example: if str is 9:00am-10:00am then  the output should be 60. 
    If str is 1:00pm-11:00am the output should be 1320.
    '''
    # ([from 10 to 12 or from 1 to 9 with optional leading 0]am or pm-[from 10 to 12 or from 1 to 9 with optional 0 at beginning])
    if re.search("((1[0-2]|0?[1-9]):([0-5][0-9])([ap][m]))-((1[0-2]|0?[1-9]):([0-5][0-9])([ap][m]))", strParam) != None:
        
        # %I stands for hour, %M for minutes in format HH:MM, %p stands for pm or am  
        startHour = datetime.strptime(strParam.split("-")[0], '%I:%M%p')
        endHour = datetime.strptime(strParam.split("-")[1], '%I:%M%p')

        # Below parse differene into minutes format
        return (endHour-startHour).seconds/60
    else:
        return "Wrong Input"

