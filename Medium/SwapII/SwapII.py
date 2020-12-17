'''
Swap II from Coderbyte
December 2020 Jakub Kazimierski
'''

import string

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

        # digit which can be swap has to be at most at index 3rd from end and last one
        if char_id < len(strParam_list) - 2:
            if strParam_list[char_id].isdigit() and strParam_list[char_id+1].isalpha():
                next_digit_id = char_id + 1
                while next_digit_id <= len(strParam_list)-1 and strParam_list[next_digit_id].isalpha():
                    next_digit_id += 1

                if strParam_list[next_digit_id].isdigit():
                    strParam_list[char_id], strParam_list[next_digit_id] = \
                        strParam_list[next_digit_id], strParam_list[char_id]

    return "".join(strParam_list)            