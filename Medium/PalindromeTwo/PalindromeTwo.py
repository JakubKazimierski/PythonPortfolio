'''
Palindrome Two from Coderbyte
December 2020 Jakub Kazimierski
'''

import re

def PalindromeTwo(strParam):
    '''
    Have the function PalindromeTwo(str) 
    take the str parameter being passed 
    and return the string true if the parameter 
    is a palindrome, (the string is the same forward 
    as it is backward) otherwise return the string false. 
    The parameter entered may have punctuation and symbols 
    but they should not affect whether the string is in fact a 
    palindrome. 
    
    For example: "Anne, I vote more cars race Rome-to-Vienna" 
    should return true.
    '''
    
    chars_list = re.split(r'[^a-zA-Z]', strParam)

    word = "".join(chars_list).lower()

    return "true" if word[::-1] == word else "false"