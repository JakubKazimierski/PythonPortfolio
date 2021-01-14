'''
Linear Congurence from Coderbyte
December 2020 Jakub Kazimierski
''' 

def LinearCongruence(strParam):
    '''
    Have the function LinearCongruence(str) 
    read the str parameter being passed which 
    will be a linear congruence equation in the 
    form: "ax = b (mod m)" Your goal is to solve 
    for x and return the number of solutions to x. 
    
    For example: if str is "32x = 8 (mod 4)" then 
    your program should return 4 because the answers 
    to this equation can be either 0, 1, 2, or 3.
    '''
    
    left_side, right_side = strParam.split(" = ")[0].replace("x", ""), \
        strParam.split(" = ")[1].replace("(","").replace(")","").split(" mod ")

    right_side_equal = int(right_side[0]) % int(right_side[1])

    possible_solutions = set()
    for number in range(int(right_side[1])):
        
        if (int(left_side)*number) % int(right_side[1]) == right_side_equal:
            possible_solutions.add(number%int(right_side[1])) 

    return len(possible_solutions)        