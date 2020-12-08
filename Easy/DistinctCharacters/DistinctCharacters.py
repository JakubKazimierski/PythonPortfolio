'''
Distinct Characters from Coderbyte
December 2020 Jakub Kazimierski
'''

def DistinctCharacters(strParam):
    '''
    Have the function DistinctCharacters(str) 
    take the str parameter being passed and determine 
    if it contains at least 10 distinct characters, if so, 
    then your program should return the string true, 
    otherwise it should return the string false. 
    
    For example: if str is "abc123kkmmmm?" then your 
    program should return the string false because this string 
    contains only 9 distinct characters: a, b, c, 1, 2, 3, k, m, ? 
    adds up to 9.
    '''
    try:
        if len(set(strParam)) == 10:
            return "true"
        else:
            return "false"       


    except(AttributeError, TypeError):
        return -1

def _input():

  exampleInp = "abc123kkmmmm?"

  return exampleInp

def _output():

  exampleOut = "false"

  return exampleOut