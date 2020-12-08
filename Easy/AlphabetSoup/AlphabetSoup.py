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
 
    sortedStringList = sorted(strParam)
    
    return "".join(sortedStringList)

  except (AttributeError, TypeError):
    return -1

