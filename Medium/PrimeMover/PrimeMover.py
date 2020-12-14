'''
Prime Mover from Coderbyte
December 2020 Jakub Kazimierski
'''

from math import sqrt
from itertools import count, islice

# O(sqrt(n))
def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

def PrimeMover(num):
    '''
    Have the function PrimeMover(num) 
    return the numth prime number. 
    The range will be from 1 to 10^4. 
    For example: if num is 16 the output 
    should be 53 as 53 is the 16th prime number.
    '''
    
    count_nth = 0
    num_to_check = 1

    # num ~ n/ln(n) where n is amount of nums to check 
    # complexity is something like SUM from i = 1 to n sqrt(i) it is sth around nlog(n) i guess
    while count_nth < num:

        num_to_check += 1

        if is_prime(num_to_check):
            count_nth += 1


    return num_to_check
