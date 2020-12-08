'''
ASCII Conversion from Coderbyte
December 2020 Jakub Kazimierski
'''

def ASCII_conversion(strParam):
    '''
    Have the function ASCIIConversion(str) 
    take the str parameter being passed and 
    return a new string where every character, 
    aside from the space character, is replaced
    with its corresponding decimal character code. 
    For example: if str is "dog" then your program 
    should return the string 100111103 because 
    d = 100, o = 111, g = 103.
    '''
    
    try:
    
        words = strParam.split()
        ascii_words = []

        for word in words:
            ascii_word = ""
            for char in word:
                ascii_word += str(ord(char))
            ascii_words.append(ascii_word)    

        return " ".join(ascii_words)    
    
    except(AttributeError, TypeError):
        return -1

def _input():

  exampleInp = "hello world" 

  return exampleInp

def _output():

  exampleOut = "104101108108111 119111114108100"

  return exampleOut