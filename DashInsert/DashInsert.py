'''
DashInsert from Coderbyte
November 2020 Jakub Kazimierski
'''

def DashInsert(strParam):
    '''
    insert dashes ('-') between each two odd numbers in str
    and return changed output string
    '''

    if type(strParam) == str and len(strParam) > 0 :
        #output string
        #because strings are immutable create new one
        outputString = ""
        
        #ietrate array taking to values at once
        for i in range(len(strParam)-1):
            
            #take intiger val of string
            #and find odd ones coming after each other
            #thwn put '-\ beetwen them in new string
            if int(strParam[i])%2 == 1 and int(strParam[i+1])%2 == 1 :
                outputString += strParam[i]
                outputString += "-"
            else:
                outputString += strParam[i]    

        #loop dont concatenate last character of strParam
        outputString += strParam[-1]

        return outputString

    else:
        return -1
