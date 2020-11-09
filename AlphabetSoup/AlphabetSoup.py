'''
Method return sorted in lexical order
letters from input

Jakub Kazimierski October 2020
'''

def AlphabetSoup(strParam):

  '''
  return string in lexical order
  '''

  outputString = ""
  bufString = sorted(strParam)
  
  #assert that nums and punctuation is not in string
  for i in strParam:
    if i.isalpha() == False and i != " ":
      return -1



  for j in bufString:
    outputString += j

  return outputString
