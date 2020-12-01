'''
NonrepeatingCharacter from Coderbyte
December 2020 Jakub Kazimierski
'''
import collections

def NonrepeatingCharacter(strParam):
    '''
    Have the function NonrepeatingCharacter(str) 
    take the str parameter being passed, which 
    will contain only alphabetic characters and spaces, 
    and return the first non-repeating character.
    For example: if str is "agettkgaeee" then your 
    program should return k. 
    The string will always contain at least one 
    character and there will always be at least 
    one non-repeating character.
    '''

    try:

        counter_of_elements = collections.Counter(strParam)

        for key, value in zip(counter_of_elements.keys(), counter_of_elements.values()):
            if value == 1:
                return key
                
    except(AttributeError, TypeError):
        return -1
    

def _input():

    exampleInput = "agettkgaeee"

    return exampleInput

def _output():

    exampleOutput = "k"

    return exampleOutput  