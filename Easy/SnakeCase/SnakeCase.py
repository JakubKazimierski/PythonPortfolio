'''
Snake Case from Coderbyte
December 2020 Jakub Kazimierski
'''
import re

def SnakeCase(strParam):
    '''
    Have the function SnakeCase(str) 
    take the str parameter being passed 
    and return it in proper snake case 
    format where each word is lowercased 
    and separated from adjacent words via an 
    underscore. The string will only contain 
    letters and some combination of delimiter 
    punctuation characters separating each word.

    For example: if str is "BOB loves-coding" 
    then your program should return 
    the string bob_loves_coding.
    '''
    try:
        words = re.split(r'[^a-zA-Z]', strParam)

        output = "_".join(word.lower() for word in words)

        return output

    except(TypeError):
        return -1

def _input():

  exampleInp = "BOB loves-coding" 

  return exampleInp

def _output():

  exampleOut = "bob_loves_coding"

  return exampleOut