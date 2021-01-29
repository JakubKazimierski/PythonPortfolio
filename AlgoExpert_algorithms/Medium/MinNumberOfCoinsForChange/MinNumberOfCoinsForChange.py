'''
MinNumberOfCoinsForChange from AlgoExpert.io
January 2021 Jakub Kazimierski
'''

def minNumberOfCoinsForChange(n, denoms):
    '''
    Given an array of positive integers
    representing coin denominations and
    a single non-negative
    integer n, representing a target amount
    of money, write a function that returns
    the smallest number of coins needed to make
    change for (to sum up to) that target amount
    using the given coin denominations.

    Note that you have access to an unlimited amount
    of coins. In other words, if the denominations
    are [1, 5, 10], you have access to an unlimited
    amount of 1s, 5s, and 10s.

    If it's impossible to make change for the target
    amount, return -1.
    '''

    # dynamic programming approach
    # time O(n*d) where d is num of denominals
    # space O(n)
    num_coins = [float("inf")]*(n+1)
    num_coins[0] = 0

    for denom in denoms:
        for idx in range(len(num_coins)):
            if idx >= denom:
                num_coins[idx] = min(1 + num_coins[idx - denom], num_coins[idx])
    
    if num_coins[n] != float("inf"):
        return num_coins[n]
    
    return -1    



