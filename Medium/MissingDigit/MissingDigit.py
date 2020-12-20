'''
Missing Digit from Coderbyte
December 2020 Jakub Kazimierski
'''

def MissingDigit(strParam):
    '''
    Have the function MissingDigit(str) 
    take the str parameter, which will be 
    a simple mathematical formula with three 
    numbers, a single operator (+, -, *, or /) 
    and an equal sign (=) and return the digit 
    that completes the equation. In one of the 
    numbers in the equation, there will be an x character, 
    and your program should determine what digit is missing. 
    
    For example, if str is "3x + 12 = 46" then 
    your program should output 4. The x character can 
    appear in any of the three numbers and all three 
    numbers will be greater than or equal to 0 and less 
    than or equal to 1000000.
    '''
    
    # althought it is a brute force it is still O(1) complexity
    for num in range(0, 10):
        possible_x = strParam.replace("x", str(num))

        left_side, right_side = possible_x.split("=")[0], possible_x.split("=")[1]        
        
        # eval left side formula creates output of equation
        if eval(left_side) == eval(right_side):
            return num

    return -1