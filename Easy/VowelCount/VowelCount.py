'''
VowelCount from codersbyte
October 2020 Jakub Kazimierski
'''

def VowelCount(strParam):
  '''
  function take the str string parameter being passed
  and return the number of vowels the string contains
  'y' is not count as a vowel
  '''

  #check if type of input parameter is correct
  if type(strParam) == str:
    #y is not consider as vowel here  
    vovels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    counter = 0 

    #O(n)
    for i in strParam:
      #O(1) cause list of vovels is const
      if i in vovels:
        counter += 1

    #if there is no vowels output is 0
    return counter
  else:
    return -1
