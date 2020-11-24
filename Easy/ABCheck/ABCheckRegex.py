'''
Method for task ABCheck from coderbyte

Jakub Kazimierski October 2020
'''

import re

def ABCheck(strParam):

  '''
  Have the function ABCheck(strParam) 
  take the str parameter being passed 
  and return the string true if the characters
  a and b are separated by exactly 3 places anywhere
  in the string at least once 
  (ie. "lane borrowed" would result in true because
  there is exactly three characters between a and b). 
  Otherwise return the string false.
  '''

  if type(strParam) == str and len(strParam) > 3:
    
    equalizedLettersString = strParam.lower()

    # dot in regex match every character
    if re.findall("a.{3}b|b.{3}a", equalizedLettersString):
        return "true"
    else:
        return "false"    

  else:
    return -1


def _input():
  '''
  Example input method for ABCheck(), returns string.
  '''
  stringInput = "example text"

  return stringInput

def _output():
  '''
  Example output method for ABCheck(), returns string.
  '''
  stringOutput = "false"

  return stringOutput