'''
Fibonnaci Checker form Coderbyte
December 2020 Jakub Kazimierski
'''

def FibonacciChecker(num):
    '''
    Have the function FibonacciChecker(num) 
    return the string yes if the number given 
    is part of the Fibonacci sequence. This 
    sequence is defined by: Fn = Fn-1 + Fn-2, 
    which means to find Fn you add the previous two numbers up. 
    The first two numbers are 0 and 1, then comes 1, 2, 3, 5 etc. 
    If num is not in the Fibonacci sequence, return the string no.
    '''
    

    num_n = num_n_1 = 0
    num_n_2 = 1

    while num_n <= num:

        if num_n == num:
            return "yes"

        num_n = num_n_1 + num_n_2
        
        num_n_2 = num_n_1
        num_n_1 = num_n


    return "no"