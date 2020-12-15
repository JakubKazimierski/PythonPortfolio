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
    

    # create table of letters where num is beginning of new alphabet
    table_trans = letters_low[num:] + letters_low[:num] + letters_Capital[num:] + letters_Capital[:num]
    return strParam.translate(strParam.maketrans(letters_low + letters_Capital, table_trans))
