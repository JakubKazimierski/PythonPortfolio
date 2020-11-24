'''
SimpleAdding from codersbyte
October 2020 Jakub Kazimierski
'''

def SimpleAdding(num):
  '''
  function SimpleAdding(num) add up
  all the numbers from 1 to num.
  '''

  if type(num) == int:
    #to make program simple
    #i reccomend to use formula for arythmetic sum

    output = int(((num + 1)*num)/2)
    return output
  
  else:
    return -1
  

