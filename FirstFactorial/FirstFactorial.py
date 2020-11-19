'''
First Factorial from Coderbyte
October 2020 Jakub Kazimierski
'''

def FirstFactorial(num):
  '''
  Have the function FirstFactorial(num) 
  take the num parameter being passed and 
  return the factorial of it. For example: 
  if num = 4, then your program should return 
  (4 * 3 * 2 * 1) = 24. For the test cases, 
  the range will be between 1 and 18 and the 
  input will always be an integer.
  '''

  #region Commentary
  #If num is 0 output is default 1
  #we work in range from 0 to 18 but when input is 0
  #output is 1 by default, no by counting.
  #endregion
  if num in range (0, 19):
    output = 1
  else:
    return -1

  #For immutable input types I prefer using copy of input 
  number = num

  #Loop iterates over all integers in from num to 1
  while number >= 1 :
    #output increases each time
    output *= number

    #number decreases each time till it is >= 1
    number = number - 1

  return output
