'''
Palindrome Check from AlgoExpert.com
January 2021 Jakub Kazimierski
'''

def palindromeCheck(string):
    '''
    Write a function that takes in a non-empty string
    and that returns a boolean representing
    whether the string is a palindrome.

    A palindrome is defined as a string that's written the same
    forward and backward. Note that single-character strings
    are palindromes.
    '''
    return True if string == string[::-1] else False
