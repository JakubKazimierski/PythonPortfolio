'''
Basic Roman Numerals from Coderbyte
December 2020 Jakub Kazimierski
'''

def BasicRomanNumerals(strParam):
    '''
    Have the function BasicRomanNumerals(str) 
    read str which will be a string of Roman numerals. 
    The numerals being used are:
     I for 1, 
     V for 5, 
     X for 10, 
     L for 50, 
     C for 100, 
     D for 500,
     M for 1000. 
     
    In Roman numerals, to create a number 
    like 11 you simply add a 1 after the 10, so you get XI. 
    But to create a number like 19, you use the subtraction 
    notation which is to add an I before an X or V 
    (or add an X before an L or C). 
    So 19 in Roman numerals is XIX.

    The goal of your program is to return the decimal 
    equivalent of the Roman numeral given. 
    For example: if str is "XXIV" your program should return 24
    '''
    try:
        Roman_Decimal_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        decimal_output = 0

        # create list of decimal values from param
        decimal_param = [Roman_Decimal_dict[value] for value in strParam]

        decimal_output += decimal_param[-1]

        # below traverses given param from right to left, first from right is already summed
        for param_id in range(len(decimal_param)-1, 0, -1):
            # if number at the left is less, substract it from sum
            if decimal_param[param_id-1] < decimal_param[param_id]:
                decimal_output -= decimal_param[param_id-1]
            else:
                # else add it to sum
                decimal_output += decimal_param[param_id-1]    

        return decimal_output

    except(AttributeError, TypeError):
        return -1

