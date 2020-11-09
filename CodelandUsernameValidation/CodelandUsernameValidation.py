'''
CodelandUsernameValidation from codersbyte
October 2020 Jakub Kazimierski
'''

import re

def CodelandUsernameValidation(strParam):
  '''
  method checks if username from input is correctly created
  1. The username is between 4 and 25 characters.
  2. It must start with a letter.
  3. It can only contain letters, numbers, and the underscore character.
  4. It cannot end with an underscore character.
  '''

  #according to task
  #true when string has proper length
  length = False
  #true if string match regex
  match = False
  #output value
  isValid = False

  #proper length of string
  if len(strParam) <= 25 and len(strParam) >= 4:
     length = True

  #match string from beginning ^
  #include proper charachters
  #closure of whole regular expression
  #end of string
  if re.match("^[A-Za-z0-9_]*$", strParam):
    match = True
  #check if first char is letter  
  if strParam[0].isalpha() == False:
    match = False
  #check if last character is not '_'  
  if strParam[-1] == '_':
    match = False   
  # code goes here

  #usernem is correctly made if match and length are true
  if match == True and length == True:
    isValid = True

  return isValid


#uncomment if you want to use method in terminal
# if __name__ == "__main__":
#     insert = input("Check your login:")
#     # keep this function call here 
#     print(CodelandUsernameValidation(insert))