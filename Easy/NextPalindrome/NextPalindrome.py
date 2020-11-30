'''
Next Palindrome from Coderbyte
November 2020 Jakub Kazimierski
'''

def NextPalindrome(num):
    '''
    Have the function NextPalindrome(num) 
    take the num parameter being passed and 
    return the next largest palindromic number. 
    The input can be any positive integer. 
    
    For example: if num is 24, then your program 
    should return 33 because that is the next largest 
    number that is a palindrome.
    '''
    
    if type(num) == int and num > 0 :
        
        num += 1
        while str(num)[::-1] != str(num):
            num += 1

        return num
    else:
        return -1

def _input():

    exampleInput = 24

    return exampleInput

def _output():

    exampleOutput = 33
    return exampleOutput