'''
TimeConvert from Codersbyte
October 2020 Jakub Kazimierski
'''

import math

def TimeConvert(num):
  '''
  take the num parameter being passed and return
  the number of hours and minutes
  (ie. if num = 63 then the output should be 1:3)
  '''

  #for modulo 60 
  outputMin = 0
  #for int division 
  outputHour = 0
  #concatenate above
  finalOutput = ""

  #check if input data type is correct
  if type(num) == int and num > 0:
    
    #round floor, cause ceil will not be full hour if rounded
    outputHour = math.floor(num/60)
    #min is modulo 60
    outputMin = num%60

  finalOutput += str(outputHour)
  finalOutput += ":"
  finalOutput += str(outputMin)

  return finalOutput
