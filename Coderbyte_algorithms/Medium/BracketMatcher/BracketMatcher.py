'''
Bracket matcher from Coderbyte
Jakub Kazimierski October 2020
'''

def BracketMatcher(strParam):
  '''
  Have the function BracketMatcher(str) 
  take the str parameter being passed and return 1 
  if the brackets are correctly matched and 
  each one is accounted for. Otherwise return 0. 
  For example: if str is "(hello (world))", 
  then the output should be 1, but if str is 
  "((hello (world))" the the output should be 0 
  because the brackets do not correctly match up. 
  Only "(" and ")" will be used as brackets. 
  If str contains no brackets return 1.
  '''

  countBracketsSum = 0
  for i in strParam:

    if i == '(':
      countBracketsSum += 1
    elif i == ')':
      countBracketsSum -= 1

    # If ")" appears without previous pair with "(" bracket
    # output cannot be correct
    if countBracketsSum < 0:
      return 0

  # Bellow checks if there is "(" bracket without pair
  return 1 if countBracketsSum == 0 else 0
  
def _input():

  sampleString = "ab(cd)"

  return sampleString

def _output():

  sampleOutput = 1

  return sampleOutput
