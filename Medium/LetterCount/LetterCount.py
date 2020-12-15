'''
Letter Count from Coderbyte
December 2020 Jakub Kazimierski
'''

import re

def LetterCount(strParam):
    '''
    Have the function LetterCount(str) 
    take the str parameter being passed 
    and return the first word with the 
    greatest number of repeated letters. 
    For example: "Today, is the greatest day ever!" 
    should return greatest because it has 2 e's (and 2 t's) 
    and it comes before ever which also has 2 e's. 
    If there are no words with repeating letters return -1. 
    Words will be separated by spaces.
    '''
    
    words = list(filter(None, re.split(r'[^a-zA-Z]', strParam)))
    
    max_occurence_from_all = 1
    max_word = "-1"
    for word in words:
        max_occurence_current = max(word.count(letter) for letter in set(word))
        if max_occurence_current > max_occurence_from_all:
            max_occurence_from_all = max_occurence_current
            max_word = word

    return max_word

