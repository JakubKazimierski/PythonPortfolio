'''
Simple Evens from Coderbyte
December 2020 Jakub Kazimierski
'''

def SimpleEvens(num):
    '''
    Have the function SimpleEvens(num) 
    check whether every single number 
    in the passed parameter is even. 
    If so, return the string true, 
    otherwise return the string false.

    For example: if num is 4602225 
    your program should return the string 
    false because 5 is not an even number.
    '''
    try:
        
        string_num = str(num)

        return "true" if all(int(char)%2 == 0 for char in string_num) else "false"
    except(ValueError):
        return -1

