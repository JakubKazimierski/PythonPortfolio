'''
WordCount.py from codersbyte
October 2020 Jakub Kazimierski
'''

def WordCount(strParam):
  '''
  method take the str string parameter being passed
  and return the number of words the string contains   
  '''

  #check if input type is correct
  if type(strParam) == str:   
    counter = 0

    if strParam != "":            
    #if string is not empty
      for i in strParam:               
        if i == " ":    
          counter += 1
                
      #number of words is +1 greater than number of space
      #due to "Words will be separated by single spaces"
      #that implies that after last word is no more spaces
      
      #even if there is only one word output will be true
      #our counting is based on spaces
      counter += 1
                
      return counter
    else:
      return 0
  # code goes here
  else:
      return -1
