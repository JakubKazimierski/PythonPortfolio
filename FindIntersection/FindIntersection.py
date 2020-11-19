'''
find intersection from codersbyte
october 2020 Jakub Kazimierski
'''

def FindIntersection(strArr):
  '''
  Have the function FindIntersection(strArr) 
  read the array of strings stored in strArr which 
  will contain 2 elements: the first element will represent 
  a list of comma-separated numbers sorted in ascending order, 
  the second element will represent a second list of 
  comma-separated numbers (also sorted). 
  Your goal is to return a comma-separated string containing 
  the numbers that occur in elements of strArr in sorted order. 
  If there is no intersection, return the string false.

  For example: if strArr contains ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"] 
  the output should return "1,4,13" because those numbers appear 
  in both strings. The array given will not be empty, 
  and each string inside the array will be of numbers 
  sorted in ascending order and may contain negative numbers.
  '''
  try:

    #region Commentary
    #We can use built in method intersection
    #which is method for sets
    #so we have to make sets from our string array

    #Below splits values, we dont want char "," in our intersection
    #we are working on strings 
    #endregion
    arrayX = set(strArr[0].split(", "))
    arrayY = set(strArr[1].split(", "))

    #Sorts using integer value of str as key  
    result = sorted(list(arrayX.intersection(arrayY)), key=lambda str: int(str))

    #join() concatenate elements of set with separator  
    return ','.join(result) if len(result) > 0 else False
  
  except(AttributeError, TypeError):
    return -1
  