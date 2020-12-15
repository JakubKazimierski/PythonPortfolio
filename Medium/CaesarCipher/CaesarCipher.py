'''
Caesar Cipher from Coderbyte
December 2020 Jakub Kazimierski
'''

import string

def CaesarCipher(strParam,num):
    '''
    Have the function CaesarCipher(str,num) 
    take the str parameter and perform a Caesar 
    Cipher shift on it using the num parameter 
    as the shifting number. 
    
    A Caesar Cipher works by shifting each letter 
    in the string N places in the alphabet 
    (in this case N will be num). Punctuation, 
    spaces, and capitalization should remain intact. 
    For example if the string is "Caesar Cipher" 
    and num is 2 the output should be "Ecguct Ekrjgt".
    '''
    
    letters_low = string.ascii_lowercase
    letters_Capital = string.ascii_uppercase
    
    output = ""
    for char in strParam:
        if char in letters_low:
            output += letters_low[(letters_low.index(char) + num) % len(letters_low)]
        elif char in letters_Capital:
            output += letters_Capital[(letters_Capital.index(char) + num) % len(letters_Capital)]
        else:
            output += char

    return output        