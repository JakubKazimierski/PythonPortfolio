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

  #upper/lower case letters have the same value in this task
  #make all letters lower
  strCopy = strParam.lower()
  
  #list of indexes of a-letter
  indexesA = []
  #list of indexes of b-letter
  indexesB = []

  #append indexes of letters a and b to lists of indexes
  for i in range(0, len(strCopy)):
    if strCopy[i] == "a" and i not in indexesA:
      indexesA.append(i)
    if strCopy[i] == "b" and i not in indexesB:
      indexesB.append(i)  
          
  #check if for indexes of a letter index of a decreased or increased
  #by 4 is in list of indexes b, if it is return true if not return false
  for j in indexesA:
    if j+4 in indexesB or j-4 in indexesB:
      return "true"

  #Complexity of above algorithm is O(n^2)

  return "false"

