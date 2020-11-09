'''
find intersection from codersbyte
october 2020 Jakub Kazimierski
'''

def FindIntersection(strArr):
  '''
  method looks for intersection of numbers in two strings array
  '''

  #we can use built in method intersection
  #it is method for sets
  #so we have to make sets from our string array

  #split values, we dont want char "," in our intersection
  #we are working on strings 
  arrayX = set(strArr[0].split(", "))
  arrayY = set(strArr[1].split(", "))

  #sort using integer value of str as key  
  result = sorted(list(arrayX.intersection(arrayY)), key=lambda str: int(str))

  #join concatenate elements of set with separator  
  return ','.join(result) if len(result) > 0 else False


  
