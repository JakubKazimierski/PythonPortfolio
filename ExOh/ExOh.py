'''
ExOh from codersbyte
October 2020 Jakub Kazimierski
'''

def ExOh(strParam):
  '''
  method checks if number of x is equal
  number of o in input string
  '''

  #check if input variable has proper type
  if type(strParam) == str and strParam != "":
    #counters for x and o
    counterX = 0
    counterO = 0

    #O(n) one traversing is enough for this task
    for i in strParam:
      if i == "x" or i == "X":
        counterX += 1
      elif i == "o" or i == "O":
        counterO += 1
      else:
        return -1    

    #return true only when both counters are equall
    if counterO == counterX:
      return "true"
    else:
      return "false"

  else:
    return -1

