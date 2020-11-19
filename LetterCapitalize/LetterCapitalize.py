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

  #Below makes list of words by splitting  given string at spaces
  wordsList = strParam.split(" ")

  outputList = []

  #Below loop iterates words list and capitalize each one
  for i in wordsList:
     outputList.append(i.capitalize())
    

  #Join capitalized words in list by spaces
  return " ".join(outputList)
