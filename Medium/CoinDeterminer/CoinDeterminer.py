'''
Coin Determiner from Coderbyte
December 2020 Jakub Kazimierski
'''

import sys

# Top Down solution
def coin_change(coins, to_change, cache):
    '''
    Finds minimum amount of coins for change
    Time complexity is O(A*c)
    Where A is value to change, and c is amount of coins' values.
    Worst case is call stack at depth lenght of A,
    next for each stack level we try each of c coins' value, to get best result
    best solutions are storing in chache, and next are based on this cache.
    This solution finds shortest way from Val_to_change to 1, and each time improve solution
    based on values stored in cache.
    '''

    # region Conditions for recursive call
    if to_change < 0:
        return -1

    if to_change == 0:
        return 0

    if cache[to_change] != 0:
        return cache[to_change]

    system_max = sys.maxsize
    minimum = system_max
    # endregion

    # belows loop finds recursively best solution, checking each coin
    for coin in coins:
        change_result = coin_change(coins, to_change - coin, cache)

        # below finds new minimum solution for subproblem
        if (change_result >= 0 and change_result < minimum):
            minimum = 1 + change_result
    
    # assign new minimum to cache
    cache[to_change] = -1 if (minimum == system_max) else minimum

    return cache[to_change]

def CoinDeterminer(num):
    '''
    Have the function CoinDeterminer(num) 
    take the input, which will be an integer 
    ranging from 1 to 250, and return an integer 
    output that will specify the least number of coins, 
    that when added, equal the input integer. Coins are 
    based on a system as follows: there are coins representing 
    the integers 1, 5, 7, 9, and 11. 
    
    So for example: if num is 16, then the output should be 2 
    because you can achieve the number 16 with the coins 9 and 7. 
    If num is 25, then the output should be 3 because you can 
    achieve 25 with either 11, 9, and 5 coins or with 9, 9, and 7 coins.
    '''

    coins = [1, 5, 7, 9, 11]
    if num < 1:
        return 0

    return coin_change(coins, num, [0] * (num + 1))


# Down Top approach
def CoinDeterminer_DT(to_change):
    '''
    Down Top approach of Minimum Coin Change Problem
    Complexity is O(A*c) where A is value to change
    and c are amount of values of coins. For each value from
    1 to Val_to_change we do c comparitions for each value
    to get best result, and choose the best way, next iteration
    is based on this best way, so this solution does not need to 
    remember all steps, just chooses the best one.
    '''

    coins = [1, 5, 7, 9, 11]

    # array of steps to make changes
    depth = [to_change + 1] * (to_change + 1)
    depth[0] = 0

    # for ach value from down to top 
    for i in range(1, to_change + 1):
        # for each coin value
        for j in range(0, len(coins)):
            if coins[j] <= i:
                # assign new minimum amount of steps to get change
                depth[i] = min(depth[i], depth[i - coins[j]] + 1)

    return -1 if depth[to_change] > to_change else depth[to_change]