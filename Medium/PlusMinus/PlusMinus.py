'''
Plus Minus from Coderbyte
December 2020 Jakub Kazimierski
'''

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
    
    separated_digits = list(str(num))
    
    signs = []
    for _ in range(len(separated_digits)):
        signs.append("-")
    for _ in range(len(separated_digits)):        
        signs.append("+")
    
    sign_combinations = set(list(permutations(signs, len(separated_digits)-1)))

    possible_signs_order = []
    for signs in sign_combinations:
        output = ""
        for digit, sign in zip_longest(separated_digits, signs):
            if sign != None:
                output += digit + sign
            else:
                output += digit


        if eval(output) == 0:
            possible_signs_order.append(signs)

    if len(possible_signs_order) == 0:
        return "not possible"
    
    
    for signs in possible_signs_order:
        output = None
        max_minus = 0
        count_minus = 0    
        for sign in signs:
            if sign == "-":
                count_minus +=1
        if count_minus > max_minus:
            max_minus = count_minus
            output = signs

    return "".join(sign for sign in output)


