'''
Triple Double from Coderbyte
December 2020 Jakub Kazimierski
'''

def TripleDouble(num1,num2):
    '''
    Have the function TripleDouble(num1,num2) 
    take both parameters being passed, and return 
    1 if there is a straight triple of a number at 
    any place in num1 and also a straight double of 
    the same number in num2. 
    
    For example: if num1 equals 451999277 and 
    num2 equals 41177722899, then return 1 because 
    in the first parameter you have the straight 
    triple 999 and you have a straight double, 99, 
    of the same number in the second parameter. 
    If this isn't the case, return 0.
    '''
    
    digit_list_num1 = list(str(num1))
    digit_list_num2 = list(str(num2))

    if len(digit_list_num1) >=3 and len(digit_list_num2) >= 2:
        for index in range(2, len(digit_list_num1)):
            if digit_list_num1[index-2] == digit_list_num1[index-1] and\
                digit_list_num1[index-1] == digit_list_num1[index]:
                for index2 in range(1, len(digit_list_num2)):
                    if digit_list_num2[index2-1] == digit_list_num2[index2] and\
                        digit_list_num2[index2] == digit_list_num1[index]:
                        return 1

    return 0                