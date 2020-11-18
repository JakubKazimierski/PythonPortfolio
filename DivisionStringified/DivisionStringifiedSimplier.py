'''
DivisionStringified from Coderbyte
November 2020 Jakub Kazimierski
'''

#Import for proper math rounding
from decimal import Decimal, ROUND_HALF_UP

def DivisionStringified(num1,num2):
    '''
    Have the function DivisionStringified(num1,num2) 
    take both parameters being passed, divide num1 by num2, 
    and return the result as a string with properly formatted commas. 
    If an answer is only 3 digits long, return the number 
    with no commas (ie. 2 / 3 should output "1"). 
    For example: if num1 is 123456789 and num2 is 10000 the output should be "12,346".
    '''

    #Assertion for input values to be integers
    if type(num1) == int and type(num2) == int:
        
        try:

            #region Commentary
            #Output has to be stringified, and also (important!!!)
            #if we use just built in round() it rounds number to closest even number
            #Below uses method form collection decimal for proper math rounding
            #endregion

            divResult = Decimal(num1/num2).to_integral_value(rounding=ROUND_HALF_UP)

            #Built in method to format output in declared way            
            return '{:,}'.format(divResult)

        except ZeroDivisionError:
            return "num2 cannot be 0"
    else:
        return "Input type has to be Integer"
  
    