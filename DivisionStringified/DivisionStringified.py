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
            #stringOutput variable
            reversedOutputString = ""
        
            #region Commentary
            #Output has to be stringified, and also (important!!!)
            #if we use just built in round() it rounds number to closest even number
            #Below uses method form collection decimal for proper math rounding
            #endregion

            divResult = str(Decimal(num1/num2).to_integral_value(rounding=ROUND_HALF_UP))

            #Below loop separates divResult with coma
            # divResut has at least length of 1 
            for i in range(1, len(divResult)+1):

                #region Commentary
                # Coma is 4th symbol after previous 3 digits
                # we also don't want to have coma at beginnig 
                # of output, so first index of output
                # cannot contains coma
                # also i%3 != 1 has to be first condition
                # to be read by python
                #endregion

                if i%3 != 1 or i == 1:
                    #Traversing from right to left to 
                    #put comas in correct places
                    reversedOutputString += divResult[-i]
                else:
                    reversedOutputString += "," 
                    reversedOutputString += divResult[-i]   

            #to reverse it again to proper version of digit
            return reversedOutputString[::-1]
        except ZeroDivisionError:
            return "num2 cannot be 0"
    else:
        return "Input type has to be Integer"
  
    