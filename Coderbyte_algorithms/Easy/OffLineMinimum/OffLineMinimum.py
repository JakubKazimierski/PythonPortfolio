'''
Off Line Minimum from Coderbyte
November 2020 Jakub Kazimierski
'''

import collections
import string

def OffLineMinimum(strArr):
    '''
    Have the function OffLineMinimum(strArr) 
    take the strArr parameter being passed 
    which will be an array of integers ranging 
    from 1...n and the letter "E" and return 
    the correct subset based on the following rules. 
    
    The input will be in the following format: 
    ["I","I","E","I",...,"E",...,"I"] 
    where the I's stand for integers and the E 
    means take out the smallest integer currently 
    in the whole set. 
    
    When finished, your program should return 
    that new set with integers separated by commas. 
    For example: if strArr is ["5","4","6","E","1","7","E","E","3","2"] 
    then your program should return 4,1,5.

    '''
    try:

        result = []
        currentNumbersList = []

        for value in strArr:

            if value.isdigit():
                currentNumbersList.append(value)

            if value.isalpha() and len(currentNumbersList) > 0:
                currentNumbersList = sorted(currentNumbersList)
                result.append(currentNumbersList[0])
                currentNumbersList.pop(0)
            
        result = ",".join(result)
        return result
    
    except (ValueError, AttributeError, TypeError):
        return -1

