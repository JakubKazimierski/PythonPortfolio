'''
LongestWord from Coderbyte
October 2020 Jakub Kazimierski
'''

import string

def LongestWord(sen):
  '''
  Have the function LongestWord(sen) 
  take the sen parameter being passed and return 
  the largest word in the string. If there are 
  two or more words that are the same length, 
  return the first word from the string with that length. 
  Ignore punctuation and assume sen will not be empty.
  '''
  
  #string.punctuation contains punctuation signs in python
  #if intersection of set created from input string and punctuation set is equal to empty set
  if set(sen).intersection(string.punctuation) == set() and sen != "":
    #Below creates list of words
    wordsList = sen.split(" ")

    longestLength = 0
    longestWord = ""

    for i in wordsList:
      #If current word's length is greater
      if len(i) > longestLength:
        longestLength = len(i)  
        longestWord = i
            
    return longestWord

  else:
    return -1