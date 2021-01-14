'''
Simple Password from Coderbyte
December 2020 Jakub Kazimierski
'''

import re

def SimplePassword(strParam):
    '''
    Have the function SimplePassword(str) 
    take the str parameter being passed and 
    determine if it passes as a valid password 
    that follows the list of constraints:

    1. It must have a capital letter.
    2. It must contain at least one number.
    3. It must contain a punctuation mark or 
        mathematical symbol.
    4. It cannot have the word "password" in the string.
    5. It must be longer than 7 characters and 
        shorter than 31 characters.

    If all the above constraints are met within the string, 
    then your program should return the string true, otherwise 
    your program should return the string false. 
    
    For example: if str is "apple!M7" then your program 
    should return "true".
    '''
    
    if re.search(r'[A-Z]', strParam) == None or re.search(r'[0-9]', strParam) == None\
        or re.search(r'\W', strParam) == None:
        return "false"

    if 'password' in strParam.lower() or 31 <= len(strParam) or 7 >= len(strParam):
        return 'false'

    return "true"