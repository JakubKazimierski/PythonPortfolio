'''
Palindrome from codersbyte
October 2020 Jakub Kazimierski
'''

def Palindrome(strParam):
  '''
  method return true if given input string is palindrome
  false if not, and -1 for wrong input
  '''

  #dont accept other types and empty string
  if type(strParam) == str and strParam != "":

    #in python strings are immutable
    #so i wor with new ones
    stringBackward = ""
    stringForward = ""

    #O(n)
    #copy input string
    for j in range(0, len(strParam), +1):
      #number of letter is const so O(1)
      if strParam[j].isalpha():
        stringForward += strParam[j]


    #O(n)
    #copy reversed input string
    #range (from, to, step)
    for i in range(1,len(strParam)+1):
      #number of letter is const so O(1)
      if strParam[-i].isalpha():
        stringBackward += strParam[-i]
      elif strParam[-i] == " ":
          #if space do nothing
          pass
      else:
          #if there are other chars than spaces and letters
          return -1  
    #O(n) because method lower()
    if stringBackward.lower() == stringForward.lower():
      return "true"
    else:
      return "false"

  else:
    return -1
