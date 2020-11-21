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

    # Assert correct input type
    if type(num) == int and num >= 0: 

        if num < 10:
            return 0
        else:
            # map as integer every charater of stringified num
            # sum it up and pass ass input to recursive call of AdditivePersistence()
            return 1 + AdditivePersistence(sum(map(int, str(num))))    

    else:
        return -1    