'''
First reverse from codersbyte
October 2020 Jakub Kazimierski
'''

def FirstReverse(strParam):
  '''
  Have the function FirstReverse(str) 
  take the str parameter being passed 
  and return the string in reversed order. 
  For example: if the input string is "Hello World and Coders" 
  then your program should return the string sredoC dna dlroW olleH.
  '''

  try:

    #region Commentary
    #the slice statement [::-1] means 
    #start at the end of the string and 
    #end at position 0, move with the step -1, 
    #which means one step backwards.
    #endregion
    return strParam[::-1]

  except TypeError:
    return -1