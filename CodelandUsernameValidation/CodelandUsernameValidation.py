'''
CodelandUsernameValidation from codersbyte
October 2020 Jakub Kazimierski
'''

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

  # compile regex which validate string as object to match
  pattern = re.compile(r"^[a-zA-Z][a-zA-Z0-9_]{2,23}[a-zA-Z0-9]$")
  result = pattern.search(strParam)

  return "true"  if result != None else "false"
    
def _input():

  sampleString = "abc_de"

  return sampleString

def _output():

  sampleString = "true" 

  return sampleString 

