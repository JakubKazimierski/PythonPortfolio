'''
VowelCount from Coderbyte
October 2020 Jakub Kazimierski
'''

def VowelCount(strParam):
    '''
    Have the function VowelCount(str) 
    take the str string parameter being 
    passed and return the number of vowels 
    the string contains 
    (ie. "All cows eat grass and moo" would return 8). 
    Do not count y as a vowel for this challenge.
    '''

    try:

        # y is not consider as vowel here  
        vovels = ["a", "e", "i", "o", "u"]
 
        return sum(1 for letter in strParam if letter.lower() in vovels)

    except (AttributeError, TypeError):
        return -1

def _input():

    exampleInput = "All cows eat grass and moo"

    return exampleInput

def _output():

    exampleOutput = 8

    return exampleOutput
