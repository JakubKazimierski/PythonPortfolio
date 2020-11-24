'''
Palindrome from codersbyte
but do not accept nonsymetric spaces in string as palindrome
'''

def Palindrome(strParam):
  '''
  return true if string is palindrome
  false if not
  -1 for wrong input
  '''

  #check if input is correct
  if type(strParam) == str and strParam != "":

    #strings are immutable in python so 
    #we have to work on new one
    stringBackward = ""

    #O(n)
    #range (from, to, step)
    for i in range(len(strParam)-1, -1, -1):
      stringBackward += strParam[i]

    #O(n) because method lower()
    if stringBackward.lower() == strParam.lower():
      return "true"
    else:
      return "false"

  else:
    return -1
