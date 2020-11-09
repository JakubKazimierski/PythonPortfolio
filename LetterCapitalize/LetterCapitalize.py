'''
LetterCapitalize from codersbyte
October 2020 Jakub Kazimierski
'''

import string

def LetterCapitalize(strParam):
  '''
  method to capitalize first letter of
  each word in given string
  '''

  #cause in python
  #strings are immutable
  #we are working on brand new ones XD
  wordBufor = ""
  word = ""

  for i in strParam:
    #append chars to string till space
    if i != " ":
      wordBufor += i
    else:
      #when space captalize word
      #and add to final output
      word += wordBufor.capitalize()
      word += " "
      #clear bufor
      wordBufor = ""
  
  #when loop end it end at word/letter, so it is necessary to make one more step
  word += wordBufor.capitalize()
  
  return word
