'''
Swap II from Coderbyte
December 2020 Jakub Kazimierski
'''

import string
import re

def SwapII(strParam):
    '''
    Have the function SwapII(str) 
    take the str parameter and swap 
    the case of each character. Then, 
    if a letter is between two numbers 
    (without separation), switch the places 
    of the two numbers. 
    For example: if str is "6Hello4 -8World, 7 yes3" 
    the output should be "4hELLO6 -8wORLD, 7 YES3".
    '''
    
    strParam_list = list(strParam)
 
    for char_id in range(0, len(strParam_list)):
        if strParam_list[char_id].isalpha():
            strParam_list[char_id] = strParam_list[char_id].swapcase()

    strParam = "".join(strParam_list)

    # swap 3rd group with first group where first and third are numbers and second are alphabetic signs
    strParam = re.sub(r'([\d])([\w]+)([\d])',r'\3\2\1',strParam)


    return strParam           