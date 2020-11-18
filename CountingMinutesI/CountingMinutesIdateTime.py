'''
CountingMinutesI From Coderbyte
Implementation with datetaime() function
November 2020 Jakub Kazimierski
'''

#To assert correct input
import re
#To parse given input
from datetime import datetime

def CountingMinutesI(strParam):

    # ([from 10 to 12 or from 1 to 9 with optional leading 0]am or pm-[from 10 to 12 or from 1 to 9 with optional 0 at beginning])
    if re.search("((1[0-2]|0?[1-9]):([0-5][0-9])([ap][m]))-((1[0-2]|0?[1-9]):([0-5][0-9])([ap][m]))", strParam) != None:
        #%I stands for hour in format HH:MM, %p stands for pm or am  
        startHour = datetime.strptime(strParam.split("-")[0], '%I:%M%p')
        endHour = datetime.strptime(strParam.split("-")[1], '%I:%M%p')

        #region Commentary
        #Below expression (endHour - startHour) holds difference between datetime objects
        #to get output in proper format, convert this diggerence to seconds, and divide by 60
        #to get output in minutes format 
        #endregion
        return (endHour-startHour).seconds/60
    else:
        return "Wrong Input"