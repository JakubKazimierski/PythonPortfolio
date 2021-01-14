'''
TernaryConverter from Coderbyte
December 2020 Jakub Kazimierski
'''

def TernaryConverter(num):
    '''
    Have the function TernaryConverter(num) 
    take the num parameter being passed, which 
    will always be a positive integer, and convert 
    it into a ternary representation. 
    
    For example: if num is 12 then your 
    program should return 110.
    '''
    
    rest = []

    while int(num/3) != 0:
        rest.append(num%3)
        num = int(num/3)
    # append rest after division last elem which is equal 0
    rest.append(num%3)

    return int("".join(str(digit) for digit in rest[::-1]))