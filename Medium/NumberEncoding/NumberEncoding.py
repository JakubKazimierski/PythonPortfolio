'''
Number Encoding from Coderbyte
December 2020 Jakub Kazimierski
'''

import string

def NumberEncoding(strParam):
    '''
    Have the function NumberEncoding(str) 
    take the str parameter and encode the 
    message according to the following rule: 
    encode every letter into its corresponding 
    numbered position in the alphabet. Symbols 
    and spaces will also be used in the input. 
    
    For example: if str is "af5c a#!" 
    then your program should return 1653 1#!.
    '''
    
    letters = string.ascii_lowercase

    strParam = strParam.lower()
    # make trans convert chars to ascii number, without maketrans wee need 
    # to create trans table and define ascii number of letters on our own by ord()
    return strParam.translate({ord(letter): str(index + 1) for index, letter in enumerate(letters)})