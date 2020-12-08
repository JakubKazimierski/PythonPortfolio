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

        ascii_word = ""
        for char in strParam:

            if char == " ":
                ascii_word += " "
            else:
                ascii_word += str(ord(char))    

        return ascii_word 
    
    except(AttributeError, TypeError):
        return -1

def _input():

  exampleInp = "hello world" 

  return exampleInp

def _output():

  exampleOut = "104101108108111 119111114108100"

  return exampleOut