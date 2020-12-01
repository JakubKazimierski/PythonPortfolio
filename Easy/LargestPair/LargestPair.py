'''
Largest Pair from Coderbyte
December 2020 Jakub Kazimierski
'''

def LargestPair(num):
    '''
    Have the function LargestPair(num) 
    take the num parameter being passed 
    and determine the largest double digit 
    number within the whole number. 
    
    For example: if num is 4759472 then your 
    program should return 94 because that is the 
    largest double digit number. 
    The input will always contain at least two positive digits.
    '''

    # below finds max number in list created from number's combinatios of 2digit numbers 
    return max([int(str(num)[i] + str(num)[i+1]) for i in range(0,len(str(num))-1)])


def _input():

    exampleInput = ""

    return exampleInput

def _output():

    exampleOutput = "true"

    return exampleOutput  