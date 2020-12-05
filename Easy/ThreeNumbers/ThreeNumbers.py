'''
Three Numbers from Coderbyte
December 2020 Jakub Kazimierski
'''

import re

def ThreeNumbers(strParam):
    '''
    Have the function ThreeNumbers(str) 
    take the str parameter being passed 
    and determine if exactly three unique, 
    single-digit integers occur within each 
    word in the string. 
    
    The integers can appear anywhere in the word, 
    but they cannot be all adjacent to each other. 
    If every word contains exactly 3 unique integers 
    somewhere within it, then return the string true, 
    
    otherwise return the string false. For example: if str is 
    "2hell6o3 wor6l7d2" then your program should return "true" 
    but if the string is "hell268o w6or2l4d" then your program 
    should return "false" because all the integers are adjacent 
    to each other in the first word.
    '''
    
    try:

        only_words = re.split(" ", strParam)
        
        for word in only_words:

            # split numeric characters
            only_numbers = list(filter(None, re.split(r"[a-zA-z]", word)))
            
            if len(only_numbers) == 3:
                # if any splitted character has lenght > 1 return false
                for number in only_numbers:
                    if len(number) > 1:
                        return "false" 
            else:
                return "false"    

        # if none of forbidden case had place
        return "true"

    except(AttributeError, TypeError):
        return -1


def _input():

    sampleList = ["[5, 9]", "[1, 2, 6, 7]"]

    return sampleList

def _output():

    sampleString = "2,6"

    return sampleString
