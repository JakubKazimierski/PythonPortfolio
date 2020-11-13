'''
AdditivePersistence from Coderbyte
November 2020 Jakub Kazimierski
'''


def AdditivePersistence(num):
    '''
    take the num parameter being passed
    which will always be a positive integer
    and return its additive persistence which 
    is the number of times you must add the digits 
    in num until you reach a single digit.
    '''

    #assert correct input type
    if type(num) == int and num >= 0: 
        #do not work on input directly
        numBufor = num

        #
        counter = 0

        #while sum of digits will be more than one
        while len(str(numBufor)) > 1:
                
            #in order to split digits, convert int
            #to string and next while traversing sum up int val of
            #characters of string (substrings len 1)    
            listOfDigits = [int(i) for i in str(numBufor)]

            #assign sum of digits as new value
            numBufor = sum(listOfDigits)        

            #count steps
            counter += 1

        return counter

    else:
        return -1    