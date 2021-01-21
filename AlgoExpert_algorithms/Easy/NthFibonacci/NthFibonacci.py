'''
Nth Fibonacci from AlgoExpert.com
January 2021 Jakub Kazimierski
'''

def nthFibonacci(n):
    '''
    The Fibonacci sequence is defined as follows:
    the first number of the sequence is 0, the second
    number is 1, and the nth number is the sum of 
    the (n-1)th and (n-2)th numbers. Write a function
    that takes in an integer n and returns nth Fibonacci number/

    Important note: the Fibonacci sequence is often defined
    with its first two numbers as F_0 = 0
    and F_1 - 1. For purpose of this question, the first
    Fibonacci number is F_0; therefore, nthFibonacci(1) = F_0
    , nthFibonacci(2) = F_1, etc.
    '''

    def count_nth(n):
        '''
        O(n^2) time | O(n) space
        '''
        if n == 1:
            return 0
        if n == 2:
            return 1
        return count_nth(n-1) + count_nth(n-2) 

    return count_nth(n)           
