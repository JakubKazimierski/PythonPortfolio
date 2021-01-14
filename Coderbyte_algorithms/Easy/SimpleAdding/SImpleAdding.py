'''
SimpleAdding from Coderbyte
October 2020 Jakub Kazimierski
'''

def SimpleAdding(num):
  '''
  Have the function SimpleAdding(num) 
  add up all the numbers from 1 to num. 
  
  For example: if the input is 4 then 
  your program should return 10 because 
  1 + 2 + 3 + 4 = 10. 
  For the test cases, the parameter num will 
  be any number from 1 to 1000.
  '''

  try:

    # below uses formula for arythmetic sum
    output = int(((num + 1)*num)/2)
    return output
  
  except(ValueError, TypeError):
    return -1
  
