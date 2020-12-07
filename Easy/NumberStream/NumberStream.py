'''
Number Stream from Coderbyte
December 2020 Jakub Kazimierski
'''

def NumberStream(strParam):
    '''
    Have the function NumberStream(str) 
    take the str parameter being passed 
    which will contain the numbers 2 through 9, 
    and determine if there is a consecutive stream 
    of digits of at least N length where N is the 
    actual digit value. If so, return the string true, 
    otherwise return the string false. 
    
    For example: if str is "6539923335" then your 
    program should return the string true because there 
    is a consecutive stream of 3's of length 3. 
    The input string will always contain at least one digit.
    '''
    

    for i in range(2,10):
        # below cheks if one of possible streams is in input
        if f'{i}'*i in strParam:
            return "true"

    return "false"

def _input():

  exampleInp = "example text"

  return exampleInp

def _output():

  exampleOut = "false"

  return exampleOut