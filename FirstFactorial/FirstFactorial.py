'''
first factorial task from codersbyte
October 2020 Jakub Kazimierski
'''

def FirstFactorial(num):
  '''
  Method return factorial of given number
  '''

  #if num is 0 output is default 1
  #we work in range from 1 to 18
  if num in range (0, 18):
    output = 1
  else:
    output = -1  
  #work on extra variable 
  number = num

  #iterate over all integer in range [1, num]
  while number >= 1 :
    #output increase each time
    output *= number
    #number decrease each time
    #while it is >= 1
    number = number - 1

  return output
