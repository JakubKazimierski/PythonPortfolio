'''
Method for task ABCheck from coderbyte

Jakub Kazimierski October 2020
'''

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

  if type(strParam) == str and len(strParam) > 0:
    
    equalizedLettersString = strParam.lower()

    for letterIndex in range(0, len(equalizedLettersString)-4):
      # if a is first checks if b is separated by 3 indexes from a
      if equalizedLettersString[letterIndex] == 'a' and equalizedLettersString[letterIndex+4] == 'b':
        return 'true'
      # if b is first checks if a is separated by 3 indexes from b  
      if equalizedLettersString[letterIndex] == 'b' and equalizedLettersString[letterIndex+4] == 'a':
        return 'true'

    # complexity of above is O(n)    
    return 'false'
  
  else:
    return -1

