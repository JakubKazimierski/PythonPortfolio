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

    if type(strParam) == str and len(strParam) > 0 :
    
        #output string
        #because strings are immutable create new one
        outputString = ""
        
        #Iterate array taking two values at once
        for i in range(0, len(strParam)-1):
            
            #put str[i] + '-' if str[i] and str[i+1] are odd
            #else put just str[i]
            outputString += (strParam[i] + "-") if int(strParam[i])%2 != 0 \
                and int(strParam[i+1])%2 != 0 else  strParam[i]            

        #Loop does not concatenate last character of strParam
        outputString += strParam[-1]

        return outputString

    else:
        return -1
