'''
Missing Digit II from Coderbyte
December 2020 Jakub Kazimierski
'''

def MissingDigitII(strParam):
    '''
    Have the function MissingDigitII(str) 
    take the str parameter, which will be 
    a simple mathematical formula with three 
    numbers, a single operator (+, -, *, or /) 
    and an equal sign (=) and return the two digits 
    that complete the equation. In two of the numbers 
    in the equation, there will be a single ? character, 
    and your program should determine what digits are missing 
    and return them separated by a space. 
    
    For example, if str is "38?5 * 3 = 1?595" then your program should output 6 1.

    The ? character will always appear in both the first number and the last number 
    in the mathematical expression. There will always be a unique solution.
    '''
    
    # brute force solution

    digits = '0123456789'

    for digit_I in digits:
        for digit_II in digits:
            left_side = strParam.split("=")[0]
            right_side = strParam.split("=")[1]

            left_side = left_side.replace("?", digit_I)
            right_side = right_side.replace("?", digit_II)

            if eval(left_side) == eval(right_side):
                return '{} {}'.format(digit_I, digit_II)

    return -1            