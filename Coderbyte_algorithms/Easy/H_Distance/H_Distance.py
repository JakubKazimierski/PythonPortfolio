'''
H Distance from Coderbyte
December 2020 Jakub Kazimierski
'''

def HDistance(strArr):
    '''
    Have the function HDistance(strArr) 
    take the array of strings stored in strArr, 
    which will only contain two strings of equal 
    length and return the number of characters at 
    each position that are different between them. 
    
    For example: if strArr is ["house", "hours"] 
    then your program should return 2. The string 
    will always be of equal length and will only 
    contain lowercase characters from the alphabet and numbers.
    '''
    try:
        
        diff_counter = 0

        for charI, charII in zip(list(strArr[0]), list(strArr[1])):
            if charI != charII:
                diff_counter+=1

        
        return diff_counter

    except(TypeError):
        return -1    