'''
Bracket Combinations from Coderbyte
January 2021 Jakub Kazimierski
'''
import scipy.special

def BracketCombinations(num):
    '''
    Have the function BracketCombinations(num) 
    read num which will be an integer greater 
    than or equal to zero, and return the number 
    of valid combinations that can be formed with 
    num pairs of parentheses. 
    
    For example, if the input is 3, then the possible 
    combinations of 3 pairs of parenthesis, namely: ()()(), 
    are ()()(), ()(()), (())(), ((())), and (()()). 
    There are 5 total combinations when the input is 3, 
    so your program should return 5.
    '''

    # output is Calatan numbers based on n given at input

    calatan_num = int((1/(num + 1)) * scipy.special.binom(2*num, num))

    return calatan_num