'''
Check Nums from codersbyte

October 2020 Jakub Kazimierski
'''

def CheckNums(num1,num2):
  '''
  method checks if first number from input
  is equal, less or greater than other num from input
  '''

  #bufors for numbers
  buf1 = num1
  buf2 = num2

  #defaul output is emty string
  output = ""

  #check if tyoe of input are intiger
  if type(buf1) == int and type(buf2) == int:
    if buf1 < buf2 :
      output = "true"
    elif buf1 == buf2:
      output = "-1"
    else:
      output = "false"  
  return output
