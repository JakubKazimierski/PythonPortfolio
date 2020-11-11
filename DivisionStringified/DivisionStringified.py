'''
DivisionStringified from Coderbyte
November 2020 Jakub Kazimierski
'''
from decimal import Decimal, ROUND_HALF_UP

def DivisionStringified(num1,num2):
    '''
    function return nearest integer result
    of division of num1 by num2
    input values are intigers
    '''

    #we want just intigers at input
    if type(num1) == int and type(num1) == int:
        
        #stringOutput variable
        reversedOutputString = ""
        #output has to be stringified, and also important!!!
        #if we use just built in round() it rounds number to closest even num
        #use Decimal for proper math rounding
        divResult = str(Decimal(num1/num2).to_integral_value(rounding=ROUND_HALF_UP))

        #we also want to have coma separated output
        #by each 3digit period
        
        for i in range(1, len(divResult)+1):

            #coma is 4th symbol after previous 3 digits
            #we also dont want coma at beginnig so first index
            #is not acceptable to have coma
            if i%3 != 1 or i == 1:
                #we traverse from right to left to 
                #put comas in correct places
                reversedOutputString += divResult[-i]
            else:
                reversedOutputString += "," 
                reversedOutputString += divResult[-i]   

        #to reverse it again to proper version of digit
        return reversedOutputString[::-1]
    else:
        return "Input type has to be Intiger"
  
    