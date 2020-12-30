'''
Off Binary from Coderbyte
December 2020 Jakub Kazimierski
'''

import itertools

def OffBinary(strArr):
    '''
    Have the function OffBinary(strArr) 
    read the array of strings stored in strArr, 
    which will contain two elements, the first 
    will be a positive decimal number and the 
    second element will be a binary number. 
    Your goal is to determine how many digits 
    in the binary number need to be changed to 
    represent the decimal number correctly 
    (either 0 change to 1 or vice versa). 
    
    For example: if strArr is ["56", "011000"] 
    then your program should return 1 because only 1 
    digit needs to change in the binary number 
    (the first zero needs to become a 1) to correctly 
    represent 56 in binary.
    '''
    
    bin_format = bin(int(strArr[0]))[2:]

    count = 0
    for digit_I, digit_II in itertools.zip_longest(bin_format, strArr[1]):
        if digit_I != digit_II:
            count += 1

    return count