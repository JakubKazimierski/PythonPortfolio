'''
Better implementation of CountingMinutesI.py
Task from Coderbyte, November 2020 Jakub Kazimierski
'''

#To assert correct input match
import re

def CountingMinutesI(strParam):

    # ([from 10 to 12 or from 1 to 9 with optional leading 0]am or pm-[from 10 to 12 or from 1 to 9 with optional 0 at beginning])
    if re.search("((1[0-2]|0?[1-9]):([0-5][0-9])([ap][m]))-((1[0-2]|0?[1-9]):([0-5][0-9])([ap][m]))", strParam) != None:  
        #Array for time in minutes  
        times = []
        #Split range of time from input gives [["HH:MMam/pm"]["HH:MMam/pm"]]
        timeStrings = strParam.split('-')

        for timeString in timeStrings:
            #region Commentary
            #If time is after midday add 12*60 minutes to it's minutes format
            #We can define it thanks to index before last index which contains 'a' or 'p' letter
            #When last index contains 'm' letter
            #endregion
            times.append(720) if timeString[-2:] == 'pm' else times.append(0)
            #Assign to current time, which is last appended element 
            #in times array values of hour*60 minutes + value of minutes
            times[-1] += int(timeString.split(':')[0])*60 + int(timeString.split(':')[1][0:-2])
        
        #region Commentary
        #Below expression is very important it defines that each calculation is in group modulo C_1440 which is whole day in minute
        #So if we e.g. counting expression 2-3 it is not equal -1 because this number is not in this group
        #it will be equal to 1440 - 1 = 1439 because range of available numbers is from 0 to 1439,  there will be no 1440 in this range
        #Because 1440%1440 = 0
        #endregion

        return (times[1] - times[0]) % (24*60)
    else:
        return "Wrong Input"