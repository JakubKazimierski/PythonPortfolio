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

  #If 0 is input return 1 (Just to get proper factorial)
  if num == 0:
    return 1
  elif num in range(1,18):
    
    if num == 1:
        return 1
    else:
        #For immutable input types I prefer using copy of input 
        number = num

        return number * FirstFactorial(number-1)
        
  #For values out of range and different than 0 
  else: 
    return -1