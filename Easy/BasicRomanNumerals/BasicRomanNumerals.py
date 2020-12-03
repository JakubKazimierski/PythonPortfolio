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
        decimal_param = []
        indexes_list = []
        decimal_output = 0

        # create list of digitals from given input
        for value in strParam:
            decimal_param.append(Roman_Decimal_dict[value]) 

        # below add to output values get by substraction in Roman notation (e.g. CD = 400 = (500 - 100))
        for param_id in range(1, len(decimal_param)):
            # if number before next is less, add abs(substraction) of those numbers to output
            if decimal_param[param_id-1] < decimal_param[param_id]:
                decimal_output += (decimal_param[param_id] - decimal_param[param_id-1])
                # below remembers indexes of used values
                indexes_list.append(param_id-1)
                indexes_list.append(param_id)

        # assign value of 0 to previously counted elements
        for param_id in indexes_list:
            decimal_param[param_id] = 0

        # sum up rest of values
        decimal_output += sum(decimal_param)

        return decimal_output

    except(AttributeError, TypeError):
        return -1

def _input():

    sampleList = "XLVI"

    return sampleList

def _output():

    sampleString = 46

    return sampleString
