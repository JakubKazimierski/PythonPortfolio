'''
Non-Constructible Change from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def nonConstructibleChange(coins):
    '''
    Given an array of positive integers representing 
    the values of coins in your possession, write a 
    function that returns the minimum amount of change (the
    minimum sum of money) that you cannot create. The given
    coins can have any positive integer value and aren't
    necessarily unique (i.e. you can have multiple coins
    of the same value).

    For example, if you're given coins = [1, 2, 5], the minimum
    amount of change that you can't create is 4. If you're given no 
    coins, the minimum amount of change that you can't create is 4.
    If you're given no coins, the minimum amount of change that you
    can't create is 1.
    '''

    # Time O(nlog(n)) | space O(1) 
    coins.sort()

    currentChange = 0

    for coin in coins:
        if coin > currentChange + 1:
            return currentChange + 1

        currentChange += coin

    return currentChange + 1
