'''
Counting Minutes I from coderbyte
November 2020 Jakub Kazimierski
'''

#For matching correct input
import re

def CountingMinutesI(strParam):
    '''
    Have the function CountingMinutesI(str) 
    take the str parameter being passed which 
    will be two times (each properly formatted with a colon and am or pm) 
    separated by a hyphen and return the total number of minutes between the two times. 
    The time will be in a 12 hour clock format. 
    For example: if str is 9:00am-10:00am then the output should be 60. 
    If str is 1:00pm-11:00am the output should be 1320.
    '''

    #Unfortunantely long regex, asserts for correct input format. 
    # ([from 10 to 12 or from 1 to 9 with optional leading 0]am or pm-[from 10 to 12 or from 1 to 9 with optional 0 at beginning])
    if re.search("((1[0-2]|0?[1-9]):([0-5][0-9])([ap][m]))-((1[0-2]|0?[1-9]):([0-5][0-9])([ap][m]))", strParam) != None:

        
        #Split string at "-" to have range of time separated
        timeList = strParam.split("-")

        #region Variables    
        #Strings to get just HH:MM format from string
        startHour = ""
        startHourList = []
        startHourMinutesFormat = None

        endHour = ""
        endHourList = []
        endHourMinutesFormat = None

        #Output values which is diff in minutes
        output = None
        #endregion

        #region Commentary
        #best way to count time beetween is to convert it
        #to format of 24 hours
        #what does not change in input is am or pm at two last indexes of string
        #actually we are interested just in index bfore last, those are letters 'a'  or 'p'
        #it defines hours as: ante (before) or post(after) meridiem (midday) (fun fact XD)
        #endregion


        #Region Change format to lists [HH,MM]
        
        #timeList will be always length of 2 thanks to input assertion
        #timeList[0] is for startHours timeList[1] is for endHours
        for j in range(0,2):
            for i in timeList[j]:

                #Till we get first a or p letter
                if i.isalpha() == False:
                    if j == 0:
                        startHour += i
                    else:
                        endHour += i
                else:
                    #If before midday just leave at is it
                    #and split string HH:MM to list od [HH,MM]
                    if i == "a":
                        if j == 0:
                            startHourList = startHour.split(":")
                        else:
                            endHourList = endHour.split(":")
                        break
                    #If after midday add 12 to hour and ovverwrite old value in startHourList
                    #["HH+12","MM"]
                    else:
                        if j == 0:
                            startHourList = startHour.split(":")
                            #Bufor value just for loop
                            newFormat = int(startHourList[0]) + 12
                            startHourList[0] = str(newFormat)
                        else:
                            endHourList = endHour.split(":")
                            newFormat = int(endHourList[0]) + 12
                            endHourList[0] = str(newFormat)
                        break

        #endregion

        #Start range in minutes
        startHourMinutesFormat = int(startHourList[0])*60 + int(startHourList[1])

        #End range in minutes
        endHourMinutesFormat = int(endHourList[0])*60 + int(endHourList[1])

        #region Commentary
        #cases of output:
        #24*60 is whole day in minutes

        #startHour is am and endHour is pm
            #difference = endHour-startHour
        #startHour is am/pm and endHour is am/pm before startHour
            # difference = 24*60 - (endHour-startHour)
        #startHour is am/pm and endHour is am/pm after startHour
            # difference = endHour-startHour
        #startHour is pm and endHour is am
            # difference = 24*60 - (endHour-startHour)

        #conclusion is if endHourMinutesFormat is less than startHourMinutesFormat
        # difference =  24*60 - (endHour-startHour)
        #else deifference = (endHour-startHour)
        #endregion

        if startHourMinutesFormat > endHourMinutesFormat:
            output = 24*60 - (startHourMinutesFormat-endHourMinutesFormat)
        else:    
            output = endHourMinutesFormat - startHourMinutesFormat

        return output

    else:
        return "Wrong Input"    