'''
Division from Coderbyte
December 2020 Jakub Kazimierski
'''

import math

def Division(num1,num2):
    '''
    Have the function Division(num1,num2) 
    take both parameters being passed and 
    return the Greatest Common Factor. That 
    is, return the greatest number that evenly 
    goes into both numbers with no remainder. 
    For example: 12 and 16 both are divisible 
    by 1, 2, and 4 so the output should be 4. 
    9The range for both parameters will be from 1 to 10^3.
    '''

    # the simplest solution
    #return math.gcd(num1, num2)    
   
    while(num2):
        num1, num2 = num2, num1%num2

    return num1    