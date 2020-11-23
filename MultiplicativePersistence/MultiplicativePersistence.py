'''
MultiplicativePersistence from Coderbyte
November 2020 Jakub Kazimierski
'''

# math collections to use prod()
import math 

def MultiplicativePersistence(num):
    '''
    Have the function MultiplicativePersistence(num) 
    take the num parameter being passed which will always 
    be a positive integer and return its multiplicative persistence 
    which is the number of times you must multiply the digits in num until 
    you reach a single digit. For example: if num is 39 then your program 
    should return 3 because 3 * 9 = 27 then 2 * 7 = 14 
    and finally 1 * 4 = 4 and you stop at 4.
    '''

    try:
        
        counterOfSteps = 0
        
        # as long as there is more than one digit
        while len(str(num)) > 1:

            # reassign num as product of it's digits
            num = math.prod([int(i) for i in str(num)])

            counterOfSteps += 1

        return counterOfSteps

    except ValueError:
        return -1    

def _input():

    exampleInput = 39

    return exampleInput

def _output():

    exampleOutput = 3

    return exampleOutput