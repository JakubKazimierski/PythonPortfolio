'''
Quick Knight from Coderbyte
January 2021 Jakub Kazimierski
'''

import copy

def QuickKnight(strParam):
    '''
    Have the function QuickKnight(str) 
    read str which will be a string consisting 
    of the location of a knight on a standard 8x8 
    chess board with no other pieces on the board 
    and another space on the chess board. The structure 
    of str will be the following: "(x y)(a b)" where (x y) 
    represents the position of the knight with x and y ranging 
    from 1 to 8 and (a b) represents some other space on the chess 
    board with a and b also ranging from 1 to 8. Your program 
    should determine the least amount of moves it would take the 
    knight to go from its position to position (a b). For example 
    if str is "(2 3)(7 5)" then your program should output 3 because 
    that is the least amount of moves it would take for the knight 
    to get from (2 3) to (7 5) on the chess board.
    '''

    strParam = strParam.replace("(","").replace(")","").replace(" ", "")
    k_x, k_y = int(strParam[0]), int(strParam[1])
    end_x, end_y = int(strParam[2]), int(strParam[3])

    moves = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]

    oldPos = [(k_x, k_y)]

    count = 1
    # complexity is enormous
    while True:
        newPos = []
        # all possibilities from point are counted as 1
        for pos in oldPos:
            for move in moves:
                move_x = pos[0] + move[0]
                move_y = pos[1] + move[1]
                if move_x == end_x and move_y == end_y: return count
                if move_x < 1 or move_y < 1 or move_x > 8 or move_y > 8: continue
                newPos.append((move_x,move_y))
        oldPos = copy.copy(newPos)
        count += 1


    return count 
