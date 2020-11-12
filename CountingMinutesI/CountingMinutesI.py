'''
Counting Minutes I from coderbyte
November 2020 Jakub Kazimierski
'''

def CountingMinutesI(strParam):
    '''
    take the str parameter being passed which will be two times
    (each properly formatted with a colon and am or pm) 
    separated by a hyphen and return the total number of minutes
    between the two times
    e.g.  if str is 9:00am-10:00am then the output should be 60
    '''

    #assert inout is string and at least each hour is length 6 (H:MMnn) to 7(HH:MMnn) and also '-' sign
    #so at least string is 6+6+1 = 13 and largest range is 7+7+1 = 15, but HH:MMnnHH:MMnn is proper length
    #but it is wrong input so also string has to contain '-'
    if type(strParam) == str and len(strParam)>=13 and len(strParam)<=15 and "-" in strParam:

        
        #split string at "-" to have range of time separated
        timeList = strParam.split("-")

        #region Variables    
        #strings to get just HH:MM format from string
        startHour = ""
        startHourList = []
        startHourMinutesFormat = None

        endHour = ""
        endHourList = []
        endHourMinutesFormat = None

        #output values which is diff in minutes
        output = None
        #endregion

        #best way to count time beetween is to convert it
        #to format of 24 hours
        #what does not change in input is am or pm at two last indexes of string
        #actually we are interested just in index bfore last, those are letters 'a'  or 'p'
        #it defines hours as: ante (before) or post(after) meridiem (midday) (fun fact XD)
        
        #region Change format to lists [HH,MM]
        for i in timeList[0]:

            #till we get first a or p letter
            if i.isalpha() == False:
                startHour += i
            else:
                #if before midday just leave at is it
                #and split string HH:MM to list od [HH,MM]
                if i == "a":
                    startHourList = startHour.split(":")
                    break
                #if after midday add 12 to hour and ovverwrite old value in startHourList
                #["HH+12","MM"]
                elif i == "p":
                    startHourList = startHour.split(":")
                    #bufor value just for loop
                    newFormat = int(startHourList[0]) + 12
                    startHourList[0] = str(newFormat)
                    break
                else:
                    break    
        
        #same process goes for endHour
        for i in timeList[1]:

            #till we get first a or p letter
            if i.isalpha() == False:
                endHour += i
            else:
                #if before midday just leave at is it
                #and split string HH:MM to list od [HH,MM]
                if i == "a":
                    endHourList = endHour.split(":")
                    break
                #if after midday add 12 to hour and ovverwrite old value in endHourList
                #["HH+12","MM"]
                elif i == "p":
                    endHourList = endHour.split(":")
                    #bufor value just for loop
                    newFormat = int(endHourList[0]) + 12
                    endHourList[0] = str(newFormat)
                    break
                else:
                    break    


        #endregion

        #start range in minutes
        startHourMinutesFormat = int(startHourList[0])*60 + int(startHourList[1])

        #end range in minutes
        endHourMinutesFormat = int(endHourList[0])*60 + int(endHourList[1])


        #cases of output:

        #startHour is am and endHour is pm
            #just abs(endHour-startHour)
        #startHour is am/pm and endHour is am/pm before startHour
            # abs(24*60 - abs(endHour-startHour))
        #startHour is am/pm and endHour is am/pm after startHour
            #abs(endHour-startHour)
        #startHour is pm and endHour is am
            # abs(24*60 - abs(endHour-startHour))

        #conclusion is if endHourMinutesFormat is < startHourMinutesFormat
        # output is  abs(24*60 - abs(endHour-startHour))
        #else abs(endHour-startHour)
        
        #to avoid unexpected minus in output i'll use abs
        if startHourMinutesFormat > endHourMinutesFormat:
            output = abs(24*60 - abs(endHourMinutesFormat-startHourMinutesFormat))
        else:    
            output = abs(endHourMinutesFormat - startHourMinutesFormat)


        return output

    else:
        return "Wrong Input"    