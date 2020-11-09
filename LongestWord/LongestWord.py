'''
LongestWord from codersbyte
October 2020 Jakub Kazimierski
'''

def LongestWord(sen):
  '''
  method finds longest alphabetic word
  in given string
  '''
  
  #bufor for max length 
  buforLength = 0
  #bufor for max word
  buforWord = ""
  #concatenate chars while alphabetic
  concatChars = ""
  #count length while alphabetic
  counterLength = 0

  #traverse string only once so complexity is O(n)
  for i in sen:

 

    #if char is alphabetic
    if i.isalpha() == True:
      concatChars += i
      counterLength += 1
    
    #if new counted chars are longer than previous max
    #assign new longer value and new word
    #does not change if value of length is the same          
    if buforLength < counterLength:
      buforLength = counterLength
      buforWord = concatChars
    
    #reset values if not alphabettic
    if i.isalpha() == False:
      concatChars = ""
      counterLength = 0

          
  return buforWord
