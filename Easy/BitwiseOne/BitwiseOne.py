'''
Bitwise One from Coderbyte
November 2020 Jakub Kazimierski
'''

def BitwiseOne(strArr):
    '''
    Have the function BitwiseOne(strArr) 
    take the array of strings stored in strArr, 
    which will only contain two strings of equal 
    length that represent binary numbers, and return 
    a final binary string that performed the bitwise 
    OR operation on both strings. 
    
    A bitwise OR operation places a 0 in the new string 
    where there are zeroes in both binary strings, 
    otherwise it places a 1 in that spot. 
    
    For example: if strArr is ["1001", "0100"] 
    then your program should return the string "1101"
    '''

    try:

        outputString = ""
        for bitI, bitII in zip(strArr[0], strArr[1]):
            if bitI == bitII:
                outputString += bitI
            else:
                outputString += "1"    


        return outputString
    except (AttributeError, TypeError):
        return -1
        
def _input():

    exampleInput = ["1001", "0100"]

    return exampleInput

def _output():

    exampleOutput = "1101"

    return exampleOutput
    