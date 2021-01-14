'''
SimpleSymbols from Codersbyte
October 2020 Jakub Kazimierski
'''

import re

def SimpleSymbols(strParam):
    '''
    Have the function SimpleSymbols(str) 
    take the str parameter being passed 
    and determine if it is an acceptable 
    sequence by either returning the string 
    true or false. 
    
    The str parameter will be composed of + and = 
    symbols with several characters between them 
    (ie. ++d+===+c++==a) and for the string to be 
    true each letter must be surrounded by a "+" symbol.
    So the string to the left would be false. 
    The string will not be empty and will have at least one letter.
    '''

    #  is first or last element is letter output cannot be true
    if strParam[-1].isalpha() or strParam[0].isalpha():
        return "false"


    # remove "+" from string and make list of splitted characters
    listWithout_plus = strParam.split("+")


    for i in listWithout_plus:
        # if element of list is not letter it is allowed to contain only "=" characters
        if i.isalpha() != True:
          if re.search("[a-zA-z]",i) != None:
              return "false"      

    return "true"
  
