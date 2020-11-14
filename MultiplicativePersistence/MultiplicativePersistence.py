'''
MultiplicativePersistence from Coderbyte
November 2020 Jakub Kazimierski
'''

#import math collections to use built in multiplication method
import math 

def MultiplicativePersistence(num):
    '''
    take the num parameter being passed 
    which will always be a positive integer
    and return its multiplicative persistence which is the number of times
    you must multiply the digits in num until you reach a single digit
    '''

    if type(num) == int and num >= 0:
        #counter
        counterOfSteps = 0
        #assign value of input to variable to work with
        buforNum = num


        #till we get one digit as output of multiplication
        #convert bufor to string to take length of it
        while len(str(buforNum)) > 1:

            #create list of digits
            #convert type int to string to get each elem 
            listOfDIgits = [int(i) for i in str(buforNum)]

            #assign new value after multiplication of elements to buforNum
            buforNum = math.prod(listOfDIgits)

            counterOfSteps += 1

        return counterOfSteps

    else:
        return -1    