'''
CodelandUsernameValidation from codersbyte
October 2020 Jakub Kazimierski
'''

#To use regex formula
import re

def CodelandUsernameValidation(strParam):
  '''
  Have the function CodelandUsernameValidation(str) 
  take the str parameter being passed and determine 
  if the string is a valid username according to the following rules:

  1. The username is between 4 and 25 characters.
  2. It must start with a letter.
  3. It can only contain letters, numbers, and the underscore character.
  4. It cannot end with an underscore character.

  If the username is valid then your program should return the string true, 
  otherwise return the string false.
  '''

  #If length is not proper 
  if not (len(strParam) <= 25 and len(strParam) >= 4):
    return "false"
  
  #If first sign is not a letter 
  if not strParam[0].isalpha():
    return "false"

  # re.earch unlike re.match checks for a match anywhere in the string
  #Expression [^A-Za-z0-9_] matches each sign out of Unicode word characters
  #If match is not found
  if re.search("[^A-Za-z0-9_]", strParam):       
    return "false"
  
  #If last element is equal to "_"    
  if strParam[-1] == "_":
    return "false"

  #If none of forbidden conditions had place
  #return true
  return "true"
