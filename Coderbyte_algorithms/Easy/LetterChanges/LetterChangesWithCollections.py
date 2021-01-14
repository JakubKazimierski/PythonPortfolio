'''
letterChanges from codersbyte
October 2020 Jakub Kazimierski
'''

import string

def LetterChanges(strParam):
  '''
  Have the function LetterChanges(str) 
  take the str parameter being passed and 
  modify it using the following algorithm. 
  Replace every letter in the string with the 
  letter following it in the alphabet 
  (ie. c becomes d, z becomes a). 
  Then capitalize every vowel in this new string (a, e, i, o, u) 
  and finally return this modified string.
  '''

  if type(strParam) == str:
    
    #region Commentary
    #maketrans() function is used to construct the transition table 
    #i.e specify the list of characters that need to be replaced 
    # in the whole string or the characters that need to be deleted from the string
    #endregion

    translationTable = str.maketrans("abcdefghijklmnopqrstuvwxyz","bcdEfghIjklmnOpqrstUvwxyzA")
    
    #translate() function uses the translation, mapping specified signs from maketrans().
    output = strParam.lower().translate(translationTable)

    return output
  else:
    return -1

