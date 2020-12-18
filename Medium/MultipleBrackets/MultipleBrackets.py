'''
Multiple Brackets from Coderbyte
December 2020 Jakub Kazimierski
'''

def MultipleBrackets(strParam):
    '''
    Have the function MultipleBrackets(str) 
    take the str parameter being passed and 
    return 1 #ofBrackets if the brackets are 
    correctly matched and each one is accounted for. 
    Otherwise return 0. 
    
    For example: if str is "(hello [world])(!)", 
    then the output should be 1 3 because all the 
    brackets are matched and there are 3 pairs of 
    brackets, but if str is "((hello [world])" 
    the the output should be 0 because the brackets 
    do not correctly match up. Only "(", ")", "[", and "]"
    will be used as brackets. If str contains no brackets 
    return 1.
    '''
    
    pairs = 0
    bracket = 0
    square_bracket = 0

    for elem in strParam:
        # possible brackets and pairs increment
        if elem == "(" and bracket >= 0:
            bracket += 1
            pairs += 1
        if elem == ")":
            bracket -= 1
        # possible brackets and pairs increment            
        if elem == "[" and bracket >= 0:
            square_bracket += 1
            pairs += 1
        if elem == "]":
            square_bracket -= 1            

    # only if brackets matches, return number of pairs
    if square_bracket == 0 and bracket == 0:
        return '{} {}'.format(1, pairs)

    return 0