'''
DivisionStringified from Coderbyte
November 2020 Jakub Kazimierski
'''

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

    try:

        # Below uses decimal collection for proper math rounding
        divResult = Decimal(num1/num2).to_integral_value(rounding=ROUND_HALF_UP)

        # Here format() is used to create string output of decimal number          
        return '{:,}'.format(divResult)

    except (AttributeError, TypeError,ZeroDivisionError):
        return "Not correct input"
  
