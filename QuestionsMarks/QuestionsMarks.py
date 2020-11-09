'''
QuestionMarks from codersbyte
October 2020 Jakub Kazimierski
'''

from collections import Counter


def QuestionsMarks(strParam):
  '''
  method return true if
  there are exactly 3 question marks
  between every pair of two numbers that add up to 10
  '''

  #make counter which contains
  #number of questionmarks
  #in renge beetween numbers that
  #add up to 10
  #frequencyQuestionMark = Counter(strParam)
  output = []

  #var to loop while length of given input string
  i = 0
  
  #start traverse
  while i < len(strParam):  #O(n)
    
    #if substring represent digit value
    if strParam[i].isdigit() == True:
      
      #find next digit value in range form i to next value
      for j in range(i, len(strParam)): #O(n)

        #if we find it
        if strParam[j].isdigit() == True:

          #if sum of digit values add up to 10
          if int(strParam[i]) + int(strParam[j]) == 10 and i < j:
          
            #count question marks between
            frequencyQuestionMark = Counter(strParam[i:j])
            #return true when there are 3 question marks
          
            if frequencyQuestionMark["?"] == 3:
          
              output.append("true")
              #reset counter
              frequencyQuestionMark.clear()
              #continue searching next digits
              i = j
          
            else:
          
              output.append("false")
              #reset counter
              frequencyQuestionMark.clear()
              i = j                
          
          #if sum is not valid i became value at j index in strParam
          #and whole process continue    
          else:
            i = j
            continue
    
    #if no of above conditions were true, just traverse further      
    i+=1

  #I assume that rhanks to 2 times loop complexity is O(n^2)

  #if input is correct return true or false
  if strParam != "" and type(strParam) == str:

    #if all digits that add up to 10 has 3 '?' between 
    #in output are only true values
    if "false" not in output and output != []:

      return "true"
    else:  

      return "false"
  else:

    #if input was not correct
    return -1
