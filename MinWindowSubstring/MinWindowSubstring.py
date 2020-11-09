'''
MinWindow substring from codersbyte
October 2020 Jakub Kazimierski
'''

from collections import Counter

#A Counter is a dict subclass for counting hashable objects
#>>> cnt = Counter()
#>>> for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
#        cnt[word] += 1
#>>> cnt
#Counter({'blue': 3, 'red': 2, 'green': 1})

EMPTY_COUNTER = Counter()

def MinWindowSubstring(strArr):
  '''
  method for finding min substring of first from
  two give strings, which has to contain all letters from second one
  '''
  
  #N - left first parameter
  # K - second parameter  
  N, K = strArr

  #count uniqe elements in K   
  #uniqe will be letters
  frequencyK = Counter(K)
  options = []

  #iterate over N complexity O(n)
  for i in range(0, len(N)):
    #counter for N (check if it has same count values like K)
    curr = Counter()

    #O(n)
    #iterate from i to end of N
    for j in range(i, len(N)):
      curr[N[j]] += 1

      #if we found vlid syntax (same symbols in N and K)
      #even before j == len(N)-1 what is [last index in N]
      #N can contain more symbols at this moment than K
      #we want to be sure that all symbols from K are in N at this moment
      if frequencyK - curr == EMPTY_COUNTER and frequencyK != EMPTY_COUNTER:

        #add our window to our optional outputs  
        options.append(N[i:j + 1])
        #go to i = i+1 and repeat process
        break

  #return min of valid windows, so key is length 
  # if there are any non empty options 
  if options != []:
    return min(options, key=len)
  else:
      return False    
  #above program is based on Counters of  hashable objects
  # and also  based on left and right pointers (in this case i is left pointer and j is right pointer)    
  


