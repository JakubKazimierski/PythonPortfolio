'''
Prime Time from Coderbyte
December 2020 Jakub Kazimierski
'''

from math import sqrt
from itertools import count, islice

def is_prime(n):

    # isslice only needs to memorize the initial arguments you provide
    # and generates every number on-the-fly

    # if n%i == 0 then bool(0) == False
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))



def PrimeTime(num):
    '''
    Have the function PrimeTime(num) 
    take the num parameter being passed 
    and return the string true if the parameter 
    is a prime number, otherwise return the string false. 
    The range will be between 1 and 2^16.
    '''

    try:

        return str(is_prime(num)).lower()

    except(TypeError):
        return -1    