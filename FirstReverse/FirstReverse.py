'''
First reverse from codersbyte
October 2020 Jakub Kazimierski
'''

def FirstReverse(strParam):
  '''
  method return reversed string
  '''

  #do not work on given string
  outputString = ""

  #concatenate bufor string while iterate
  #reverse in given input string
  for i in reversed(strParam):
    outputString += i

  return outputString

