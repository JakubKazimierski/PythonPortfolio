'''
Method for task ABCheck from coderbyte

Jakub Kazimierski October 2020
'''

def ABCheck(strParam):

  '''
  method created to check
  if between 'a' and 'b' in string
  are exactly 3 indexes of other
  return true or false
  '''

  output = "false"


  for i in range(0,len(strParam)):
    #when find a
    if strParam[i] == "a" or strParam[i] == "A":
      #assertion for proper indexes range
      if i > 3 and i < (len(strParam) - 1) - 3:
        if strParam[i-4] == "b" or strParam[i+4] == "b" or strParam[i-4] == "B" or strParam[i+4] == "B":
          output = "true"
      #if index is to few to decrease    
      elif i <= 3 and (i + 4) < len(strParam):
        if strParam[i+4] == "b" or strParam[i+4] == "B":    
          output = "true"
      else:
        #if index is to high to increase
        if i - 4 >= 0:
          if strParam[i-4] == "b" or strParam[i-4] == "B":    
            output = "true"

  
  return output

