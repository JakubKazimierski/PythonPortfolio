'''
SimpleSymbols from Codersbyte
October 2020 Jakub Kazimierski
'''

def SimpleSymbols(strParam):
  '''
  method check if each letter in given
  input string is surrounded by '+' character
  '''

  #counter of letters for check if input is correct
  counterLetters = 0

  for i in range(0, len(strParam)):
    #if letter is at index 0 false
    if strParam[i].isalpha() and i == 0:
      return "false"
    #if letter is at last index false  
    if strParam[i].isalpha() and i == len(strParam)-1:
      return "false"
    
    if i > 0 and i < len(strParam)-1:  
    #if letter is not neighbour with + at left false  
     if strParam[i].isalpha() and strParam[i-1] != "+":
        return "false"
    #if letter is not neighbour with + at right false    
     if strParam[i].isalpha() and strParam[i+1] != "+":
        return "false"

    #above cheks not correct cases

    if strParam[i].isalpha():
      counterLetters += 1

  #if there is no letters false
  if counterLetters == 0:
    return "false"
  else:  
    return "true"

# keep this function call here 
#print(SimpleSymbols(input()))