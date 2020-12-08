'''
LetterCapitalize from Coderbyte
October 2020 Jakub Kazimierski
'''

import string

def LetterCapitalize(strParam):
      '''
      Have the function LetterCapitalize(str) 
      take the str parameter being passed and 
      capitalize the first letter of each word. 
      Words will be separated by only one space.
      '''

      wordsList = strParam.split(" ")

      # return capitalized words joined by spaces         
      return " ".join((word.capitalize() for word in wordsList))

