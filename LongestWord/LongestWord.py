'''
LongestWord from Coderbyte
October 2020 Jakub Kazimierski
'''

import re
# import string

def LongestWord(sen):
    '''
    Have the function LongestWord(sen) 
    take the sen parameter being passed and return 
    the largest word in the string. If there are 
    two or more words that are the same length, 
    return the first word from the string with that length. 
    Ignore punctuation and assume sen will not be empty.
    '''
    
    try:
        
        # replace each non alphabetic and non whitespace sign with empty string
        ignoredPunctuationString = re.sub("[^\w\s]","",sen)

        # same effect will be gain thanks to below
        # ignoredPunctuationString = sen.translate(str.maketrans("","", string.punctuation))

        wordsList = ignoredPunctuationString.split(" ")
         
        return max(wordsList, key=len)

    except(AttributeError, TypeError):
      return -1