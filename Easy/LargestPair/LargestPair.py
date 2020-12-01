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

    stringNum = str(num)

    greatest_pair = (0,0)
    for i in range(0, len(stringNum)-1):
        if (int(stringNum[i]),int(stringNum[i+1])) > greatest_pair:
            greatest_pair = (int(stringNum[i]),int(stringNum[i+1]))

    
    outputString = "".join(str(digit) for digit in greatest_pair)

    return int(outputString)  


def _input():

    exampleInput = ""

    return exampleInput

def _output():

    exampleOutput = "true"

    return exampleOutput  