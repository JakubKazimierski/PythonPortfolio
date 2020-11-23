'''
First reverse from codersbyte
October 2020 Jakub Kazimierski
'''

def FirstReverse(strParam):
    '''
    Have the function FirstReverse(str) 
    take the str parameter being passed 
    and return the string in reversed order. 
    For example: if the input string is "Hello World and Coders" 
    then your program should return the string sredoC dna dlroW olleH.
    '''

    try:
      # Below returns string backwards
      return strParam[::-1]

    except TypeError:
      return -1

def _input():

    exampleInput = "abcd"

    return exampleInput

def _output():

    exampleOutput = "dcba"

    return exampleOutput          