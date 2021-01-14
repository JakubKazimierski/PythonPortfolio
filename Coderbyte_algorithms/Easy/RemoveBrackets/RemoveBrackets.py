'''
Remove Brackets from Coderbyte
December 2020 Jakub Kazimierski
'''

def RemoveBrackets(strParam):
    '''
    Have the function RemoveBrackets(strParam) 
    take the str parameter being passed, 
    which will contain only the characters "(" and ")", 
    and determine the minimum number of brackets that 
    need to be removed to create a string of correctly 
    matched brackets. For example: if str is "(()))" 
    then your program should return the number 1. 
    The answer could potentially be 0, and there will 
    always be at least one set of matching brackets in the string.
    '''
    try:
  
        counter = 0
        steps = 0
        # if counter stays 0 brackets matches 
        for elem in strParam:
            if elem == "(":
                counter += 1
                steps += 1

            # ")" fits only if counter > 0
            if counter > 0:
                if elem == ")":
                    counter -= 1
                    steps += 1

        
        # if counter > 0 there is some steps to remove 
        return len(strParam) - steps + counter
    
    except(TypeError):
        return -1