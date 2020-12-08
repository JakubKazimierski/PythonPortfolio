'''
ExOh from codersbyte
October 2020 Jakub Kazimierski
'''

import re

def ExOh(strParam):
    '''
    Have the function ExOh(str) 
    take the str parameter being passed 
    and return the string true if there is
    an equal number of x's and o's, 
    otherwise return the string false. 
    Only these two letters will be entered in the string, 
    no punctuation or numbers. For example: 
    if str is "xooxxxxooxo" then the output should return false 
    because there are 6 x's and 5 o's.
    '''

    # Checks if input matches x or o letters
    if re.search("^[xX|oO]+$", strParam) != None:

      # Below converts letters to lower in order to compare just values of letters
        return "true" if strParam.lower().count("x") == strParam.lower().count("o") \
          else "false"

    else:
      return -1

