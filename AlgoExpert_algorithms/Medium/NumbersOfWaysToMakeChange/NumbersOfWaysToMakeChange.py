'''
NumbersOfWaysToMakeChange from AlgoExpert.io
January 2021 Jakub Kazimierski
'''

def numberOfWaysToMakeChange(n, denoms):
    '''
    Given an array of distinct positive integers
    representing coin denominations and a single 
    non-negative integer n, representing a target
    amount of money, write a function that returns
    the number of ways to make change for that target
    amount using the given coin denominations.

    Note that an unlimited amount of coins is at your
    disposal.
    '''

    # Time O(n*d) where d is amount of denoms
    # space O(n)
    # dynamic programming approach
    ways = [0]*(n+1)
    ways[0] = 1

    for denom in denoms:
        for idx in range(len(ways)):    
            if idx >= denom:
                ways[idx] += ways[idx-denom]

    return ways[n]
