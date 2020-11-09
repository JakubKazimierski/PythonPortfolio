'''
letterChanges from codersbyte
October 2020 Jakub Kazimierski
'''

import string

def LetterChanges(strParam):
  '''
  method to change letters to next one from alphabet
  e.g 'a' -> 'b' and also vowels became Uppercase
  '''
  #lists of lowercase and uppercase letters  
  letters = string.ascii_lowercase
  lettersBig = string.ascii_uppercase

  #string for applaying changes
  #because strings are immutable in python
  #so we cannot change given in input string
  word = ""

  for i in range(0, len(strParam)):#O(n)
    if strParam[i].isalpha():            
        for j in range(0, len(letters)):#O(1)
            if strParam[i] == letters[j]:
                #if vowel capitalize
                if letters[(j+1)%len(letters)] in ('a', 'e', 'i', 'o', 'u'):
                  word += lettersBig[(j+1)%len(letters)]
                else:  
                  word += letters[(j+1)%len(letters)]
    else:
        #if not alphabetic leave old value
        word += strParam[i]    
  
  # output goes here
  return word

# keep this function call here 
#print(LetterChanges(input()))