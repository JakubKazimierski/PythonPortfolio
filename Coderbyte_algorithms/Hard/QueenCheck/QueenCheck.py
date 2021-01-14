'''
Queen Check from Coderbyte
January 2021 Jakub Kazimierski
'''

def QueenCheck(strArr):
    '''
    Have the function QueenCheck(strArr) 
    read strArr which will be an array 
    consisting of the locations of a Queen 
    and King on a standard 8x8 chess board 
    with no other pieces on the board. 
    The structure of strArr will be the following: 
    ["(x1,y1)","(x2,y2)"] with (x1,y1) representing 
    the position of the queen and (x2,y2) representing 
    the location of the king with x and y ranging from 1 to 8. 
    Your program should determine if the king is in check based 
    on the current positions of the pieces, and if so, return 
    the number of spaces it can move to in order to get out of 
    check. If the king is not in check, return -1. 
    
    For example: if strArr is ["(4,4)","(6,6)"] then your program 
    should output 6. Remember, because only the queen and king are 
    on the board, if the queen is checking the king by being directly 
    adjacent to it, technically the king can capture the queen.
    '''
    
    queen_pos, king_pos = eval(strArr[0]), eval(strArr[1])
    
    # if king is checked vertical or horizontal
    if  king_pos[0] == queen_pos[0] or king_pos[1] == queen_pos[1] or\
        abs(king_pos[1] - queen_pos[1]) == abs(king_pos[0] - queen_pos[0]):# if is checked oblique
        pass
    else:
        return -1

    # places where king can move
    # https://stackoverflow.com/questions/2373306/pythonic-and-efficient-way-of-finding-adjacent-cells-in-grid
    adjacency = [(x+king_pos[0],y+king_pos[1]) for x in (-1,0,1) for y in (-1,0,1) if not (x == y == 0)]

    movements = 0
    for x,y in adjacency:
        if x < 1 or x > 8 or y < 1 or y > 8:
            continue
        else: # horizontal or vertical or oblique, and not in place of queen
            if (x == queen_pos[0] or y == queen_pos[1] or abs(y - queen_pos[1]) == abs(x - queen_pos[0])) and\
                 (x != queen_pos[0] or y != queen_pos[1]):
                continue
            else:
                movements += 1
      
    # code goes here
    return movements


