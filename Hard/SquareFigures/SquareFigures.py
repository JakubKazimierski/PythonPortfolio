'''
Square Figures from Coderbyte
January 2021 Jakub Kazimierski
'''

from itertools import count, islice
import sys

def SquareFigures(num):
    '''
    Have the function SquareFigures(num) 
    read num which will be an integer. 
    Your program should return the smallest 
    integer that when squared has a length equal to num. 
    For example: if num is 6 then your program should output 
    317 because 317^2 = 100489 while 316^2 = 99856 which does 
    not have a length of six.
    '''
    
    # isslice only needs to memorize the initial arguments you provide
    # and generates every number on-the-fly
    for i in islice(count(0), sys.maxsize):
        if len(str(i**2)) == num:
            return i