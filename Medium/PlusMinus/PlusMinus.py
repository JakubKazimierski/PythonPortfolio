'''
Plus Minus from Coderbyte
December 2020 Jakub Kazimierski
'''
import itertools
from itertools import permutations
from itertools import zip_longest

def PlusMinus(num):
    '''
    Have the function PlusMinus(num) 
    read the num parameter being passed 
    which will be a combination of 1 or 
    more single digits, and determine if 
    it's possible to separate the digits 
    with either a plus or minus sign to get 
    the final expression to equal zero. 
    
    For example: if num is 35132 then it's 
    possible to separate the digits the following way,
    3 - 5 + 1 + 3 - 2, and this expression equals zero. 
    Your program should return a string of the signs you 
    used, so for this example your program should 
    return -++-. If it's not possible to get the digit 
    expression to equal zero, return the string not possible.

    If there are multiple ways to get the final expression to equal zero, 
    choose the one that contains more minus characters. 
    
    For example: if num is 26712 your program should return -+-- 
    and not +-+-.
    '''

    num_str = str(num); N_oper = len(num_str) - 1
    if not N_oper: return 'not possible'
    # all possible combinations as binary representation of each num to 2^n
    for n in range(2**N_oper):
        combo = f'{n:0{N_oper}b}'.replace('0', '-').replace('1', '+') + ' '
        # returns first occurence, because it's starting with '-' combinations
        if not eval(''.join(''.join(pair) for pair in zip(num_str, combo))): return combo[:-1]
    return 'not possible'
    

