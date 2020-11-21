'''
Alphabet Soup from Coderbyte
Jakub Kazimierski October 2020
'''

def AlphabetSoup(strParam):

  '''
  Have the function AlphabetSoup(strParam)
  take the strParam string parameter being 
  passed and return the string with the letters 
  in alphabetical order (ie. hello becomes ehllo). 
  Assume numbers and punctuation symbols will not be included in the string.
  '''

  try:
 
    sortedString = sorted(strParam)
    
    return "".join(sortedString)

  except (AttributeError, TypeError):
    return -1

def _input():
  '''
  Returns example input for AlphabetSoup()
  '''
  sampleString = "abcde"

  return sampleString

def _output():
  '''
  Returns example output for AlphabetSoup()
  '''
  sampleString = "edcba"

  return sampleString  