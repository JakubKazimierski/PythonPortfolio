'''
letterChanges from codersbyte
October 2020 Jakub Kazimierski
'''

import string

def LetterChanges(strParam):
  '''
  Have the function LetterChanges(str) 
  take the str parameter being passed and 
  modify it using the following algorithm. 
  Replace every letter in the string with the 
  letter following it in the alphabet 
  (ie. c becomes d, z becomes a). 
  Then capitalize every vowel in this new string (a, e, i, o, u) 
  and finally return this modified string.
  '''

  if type(strParam) == str:
    #Lists of lowercase and uppercase letters  
    letters = string.ascii_lowercase
    lettersBig = string.ascii_uppercase

    #Initialize output string
    word = ""

    for i in range(0, len(strParam)):#O(n)
      if strParam[i].isalpha():            
          for j in range(0, len(letters)):#O(1) array of letters is constant
              if strParam[i].lower() == letters[j]:
                  #If letter is vowel capitalize it
                  if letters[(j+1)%len(letters)] in ('a', 'e', 'i', 'o', 'u'):
                    word += lettersBig[(j+1)%len(letters)]
                  else:  
                    word += letters[(j+1)%len(letters)]
      else:
          #if not alphabetic leave old value
          word += strParam[i]    
    
    # output goes here
    return word
  
  else:
    return -1