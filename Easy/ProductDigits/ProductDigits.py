'''
Product Digits from Coderbtyte
December 2020 Jakub Kazimierski
'''

import math
from itertools import count, islice

# return false if n==1 or n%i==0 , then number cannot be prime
# islice generates every number on-the-fly, it memorize just initial argument, not whole list of arguments in range
def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(math.sqrt(n)-1)))

def ProductDigits(num):
    '''
    Have the function ProductDigits(num) 
    take the num parameter being passed 
    which will be a positive integer, 
    and determine the least amount of digits 
    you need to multiply to produce it. 
    
    For example: if num is 24 then you can multiply 8 by 3 
    which produces 24, so your program should return 2 
    because there is a total of only 2 digits that are 
    needed. 
    
    Another example: if num is 90, you can multiply 10 * 9, 
    so in this case your program should output 3 
    because you cannot reach 90 without using a total of 3 
    digits in your multiplication.
    '''
    
    try:


        if is_prime(num) == True:
            return "This is prime number"

        else:

            if num > 9:
                # below cheks how many 9 is needed to get the number
                # and ceil it to the next integer (it is number of digits which are needed)
                # it is kind of "O(9)"" assurance
                output = int(math.ceil(math.log(num, 9)))
                return output

            else:
                return 2

    except(AttributeError, TypeError):
        return -1

def _input():

    sampleList = 24

    return sampleList

def _output():

    sampleString = 2

    return sampleString
