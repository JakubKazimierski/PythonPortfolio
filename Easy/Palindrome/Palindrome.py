'''
Palindrome from codersbyte
October 2020 Jakub Kazimierski
'''

def Palindrome(strParam):
    '''
    Have the function Palindrome(str) 
    take the str parameter being passed 
    and return the string true if the parameter 
    is a palindrome, (the string is the same forward as it is backward) 
    otherwise return the string false. 
    For example: "racecar" is also "racecar" backwards. 
    Punctuation and numbers will not be part of the string.
    '''
    
    try:

        # ignore size of letters
        if strParam[::-1].lower() == strParam.lower():
            return "true"
        else:
            return "false"      

    except(AttributeError, TypeError):
        return -1

def _input():

    exampleInput = "racecar" 

    return exampleInput

def _output():

    exampleOutput = "true"

    return exampleOutput