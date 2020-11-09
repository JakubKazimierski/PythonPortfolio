'''
bracket matcher from coderbyte

Jakub Kazimierski October 2020
'''

def BracketMatcher(strParam):
  '''
  method check if brackets in string
  are even e.g (word) 
  and in correct order 
  e.g. )( is wrong
  '''

  #quite simple but cool
  #if one of brackets is without pair 
  #final sum cannot be 0 because not even numbers from [-1, 1]
  count = 0
  for i in strParam:
    #important here is
    #that elif works only when if is not working
    #what i mean by that is
    #when ) is first bracket it wont be counted
    #caause elif will never be seeing by interpeter in this specified case
    if i == '(':
      count += 1
    elif i == ')':
      count -= 1
    if count < 0: return 0

  return 1 if count == 0 else 0
  
