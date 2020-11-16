'''
AdditivePersistence from Coderbyte
November 2020 Jakub Kazimierski
'''


def AdditivePersistence(num):
    '''
    Have the function AdditivePersistence(num) 
    take the num parameter being passed which will always be 
    a positive integer and return its additive persistence 
    which is the number of times you must add the digits in num 
    until you reach a single digit. 
    For example: if num is 2718 then your program should return 2 
    because 2 + 7 + 1 + 8 = 18 and 1 + 8 = 9 and you stop at 9.
    '''

    #Assert correct input type
    if type(num) == int and num >= 0: 
        #To does not work on input directly
        numBufor = num
        #Counter of addition
        counter = 0

        #While sum of digits will be more than one
        while len(str(numBufor)) > 1:
                
            #In order to split digits, convert int
            #to string and next while traversing string sum up int val of
            #characters of string (substrings len 1)    
            listOfDigits = [int(i) for i in str(numBufor)]

            #Assign sum of digits as a new value
            numBufor = sum(listOfDigits)        

            #Count steps
            counter += 1

        return counter

    else:
        return -1    