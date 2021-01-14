'''
Nim Winner from Coderbyte
January 2021 Jakub Kazimierski
'''

def NimWinner(arr):
    '''
    Have the function NimWinner(arr) 
    take the array of integers stored 
    in arr which will represent the amount 
    of coins in each pile. 
    
    For example: [2, 4, 1, 3] means there are 
    4 piles of coins and there are 2 coins in the 
    first pile, 4 in the second pile, etc. Nim is played 
    by each player removing any number of coins from only 
    one pile, and the winner is the player who picks up the 
    last coin. 
    
    For example: if arr is [1, 2, 3] then for example player 1 can 
    remove 2 coins from the last pile which results in [1, 2, 1]. 
    Then player 2 can remove 1 coin from the first pile which results 
    in [0, 2, 1], etc. The player that has the last possible move taking 
    the last coin(s) from a pile wins the game. Your program should output 
    either 1 or 2 which represents which player has a guaranteed win with 
    perfect play for the Nim game.
    '''
    
    # “If both A and B play optimally (i.e- they don’t make any mistakes), 
    # then the player starting first is guaranteed to win if the XOR Nim-Sum at 
    # the beginning of the game is non-zero. Otherwise, if the XOR Nim-Sum evaluates 
    # to zero, then player A will lose definitely.”

    # in other words if piles can sum up to the same values, then player A, want it
    # to be different, but at two last moves, player 2 remove coin from pile, and there
    # is at least one coin on the other pile (only way to keeps difference), so player B wins
    # 
    # if piles sum up to different values then player A wants to have different values of piles
    # so when it comes to last moves he has to leave one pile, which will be picked up by player B
    # who wants the same values, and player B wins

    xor = eval('^'.join([str(val) for val in arr]))

    if xor == 0:
        return 2
        
    return 1    