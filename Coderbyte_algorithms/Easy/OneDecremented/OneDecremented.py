'''
One Decremented from Coderbyte
December 2020 Jakub Kazimierski
'''

def OneDecremented(strParam):
    '''
    Have the function OneDecremented(strParam) 
    count how many times a digit appears 
    that is exactly one less than the previous digit. 
    
    For example: if str is "5655984" then your 
    program should return 2 because 5 appears 
    directly after 6 and 8 appears directly after 9. 
    The input will always contain at least 1 digit.
    '''
    try:
        counter = 0

        for index in range(0, len(strParam)-1):
            if int(strParam[index+1]) == int(strParam[index])-1 :
                counter += 1
        
        return counter
    except(TypeError):
        return -1    