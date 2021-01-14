'''
String Scramble from Coderbyte
December 2020 Jakub Kazimierski
'''

import collections

def StringScramble(str1,str2):
    '''
    Have the function StringScramble(str1,str2) 
    take both parameters being passed and return 
    the string true if a portion of str1 characters 
    can be rearranged to match str2, otherwise return 
    the string false. 
    
    For example: if str1 is "rkqodlw" and str2 is "world" 
    the output should return true. Punctuation and symbols will 
    not be entered with the parameters.
    '''

    counter_I = collections.Counter(str1)
    counter_II = collections.Counter(str2) 

    # below checks occurence of chars from shorter string in longer
    # or at least equal string 
    if len(str1) < len(str2):
        for char in str1:
            if counter_I[char] > counter_II[char]:
                return "false"
    else:
        for char in str2:
            if counter_II[char] > counter_I[char]:
                return "false"


    return "true" 