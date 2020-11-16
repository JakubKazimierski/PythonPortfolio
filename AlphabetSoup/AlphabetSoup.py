'''
Alphabet Soup from Coderbyte
Jakub Kazimierski October 2020
'''

def AlphabetSoup(strParam):

  '''
  Have the function AlphabetSoup(str)
  take the str string parameter being 
  passed and return the string with the letters 
  in alphabetical order (ie. hello becomes ehllo). 
  Assume numbers and punctuation symbols will not be included in the string.
  '''


  #Assert that numbers and punctuation symbols are not in string
  for i in strParam:
    if i.isalpha() == False and i != " ":
      return -1

  #Assign sorted string to variable
  #I prefer not to change input itself
  sortedList = sorted(strParam)
  
  #Define output string
  output = ""

  #Concatenate sorted elements with output string
  for j in sortedList:
    output += j

  return output
