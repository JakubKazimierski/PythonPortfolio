'''
Different Cases from Coderbyte
December 2020 Jakub Kazimierski
'''

import re

def DifferentCases(strParam):
    '''
    Have the function DifferentCases(strParam) 
    take the str parameter being passed and return 
    it in upper camel case format where the first 
    letter of each word is capitalized. The string 
    will only contain letters and some combination 
    of delimiter punctuation characters separating 
    each word.

    For example: if str is "Daniel LikeS-coding" then 
    your program should return the string DanielLikesCoding.
    '''
    try:

        words = re.split(r'[^a-zA-Z]', strParam)

        return "".join(word.capitalize() for word in words)    

    except(TypeError):
        return -1