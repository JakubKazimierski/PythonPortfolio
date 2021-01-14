'''
GCF from Coderbyte
December 2020 Jakub Kazimierski
'''

def gcf(a, b):
    '''
    Calculate the Greatest Common Divisor of a and b.
    '''
    while b:
        a, b = b, a%b
    return a

def GCF(arr):
    '''
    Have the function GCF(arr) 
    take the array of numbers 
    stored in arr which will always 
    contain only two positive integers, 
    and return the greatest common 
    factor of them. 
    
    For example: if arr is [45, 12] then your 
    program should return 3. 
    There will always be two elements in 
    the array and they will be positive integers.
    '''

    try:

        output = gcf(arr[0],arr[1])

        return output
        
    except(AttributeError, TypeError):
        return -1    