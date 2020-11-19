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

  #Initialize output string
  outputString = ""

  #Below makes list of words by splitting 
  #given string at spaces
  wordsList = strParam.split(" ")

  #Below loop iterates words list and capitalize each one
  for i in wordsList:
    outputString += i.capitalize()
    outputString += " "

  
  #After loop ends last sign is space, and it is not expected in output
  return outputString[:-1]
