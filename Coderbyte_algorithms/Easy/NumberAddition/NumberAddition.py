'''
NumberAddition from Coderbyte
November 2020 Jakub Kazimierski
'''

import re

def NumberAddition(strParam):
    '''
    Have the function NumberSearch(str) 
    take the str parameter, search for all 
    the numbers in the string, add them together, 
    then return that final number. 
    For example: if str is "88Hello 3World!" 
    the output should be 91. 
    
    You will have to differentiate between single digit numbers 
    and multiple digit numbers like in the example above. 
    So "55Hello" and "5Hello 5" should return two different answers. 
    Each string will contain at least one letter or symbol.
    '''

    try:

        # regex split return empty values, so below filters list to not have them
        listOfNumbers = list(filter(None, re.split(r"[a-zA-Z ]", strParam)))

        return sum(int(i) for i in listOfNumbers)

    #if input type is wrong return error
    except (AttributeError, TypeError):
        return -1

