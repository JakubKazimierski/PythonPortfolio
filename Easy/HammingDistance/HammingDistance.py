'''
Hamming Distance from Coderbyte
November 2020 Jakub Kazimierski
'''

def HammingDistance(strArr):
    '''
    Have the function HammingDistance(strArr) 
    take the array of strings stored in strArr, 
    which will only contain two strings of equal length 
    and return the Hamming distance between them. 
    
    The Hamming distance is the number of positions 
    where the corresponding characters are different. 
    For example: 
    if strArr is ["coder", "codec"] 
    then your program should return 1. 

    The string will always be of equal length and 
    will only contain lowercase characters from the 
    alphabet and numbers.
    '''

    try:
   
        return sum(1 for charI, charII in zip(strArr[0], strArr[1]) if charI != charII)    
   
    except (AttributeError, TypeError):
        return -1

