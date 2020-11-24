'''
DashInsert from Coderbyte
November 2020 Jakub Kazimierski
'''

def DashInsert(strParam):
    '''
    Have the function DashInsert(str) 
    insert dashes ('-') between each two 
    odd numbers in str. For example: if str 
    is 454793 the output should be 4547-9-3. 
    Don't count zero as an odd number.
    '''

    try:    
        outputString = ""

        for i in range(0, len(strParam)-1):
            
            if int(strParam[i])%2 != 0 and int(strParam[i+1])%2 != 0:   
                outputString += (strParam[i] + "-")  
            else:
                outputString += strParam[i]            

        #Loop does not concatenate last character of strParam
        outputString += strParam[-1]

        return outputString

    except(AttributeError, TypeError, IndexError):
        return -1

def _input():

    exampleInput = "56730"

    return exampleInput

def _output():

    exampleOutput = "567-30"

    return exampleOutput     