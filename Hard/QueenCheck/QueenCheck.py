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
    
    # obliqe move as f(x) = x + b (+1) due to indexing from 1
    b_factor = abs(queen_pos[1] - queen_pos[0])

    def is_queen_in_range(queen_pos, king_pos):
        '''
        Returns True if King can capture the Queen.
        '''
        if abs(king_pos[0] - queen_pos[0]) == 1 and \
            abs(king_pos[1] - queen_pos[1]) == 1:
            return True

    def is_king_checked(queen_pos, king_pos):
        '''
        Returns True if King is checked.
        '''
        if king_pos[1] == queen_pos[1]:
            return True
        elif king_pos[0] == queen_pos[0]:
            return True
        # if y = (x_q + delta) + b -> y is in line   
        elif king_pos[1] == queen_pos[0] + abs(king_pos[0] - queen_pos[0]) + b_factor or\
                king_pos[1] == (-1)*(queen_pos[0] + abs(king_pos[0] - queen_pos[0])) + (b_factor+2):
                # for case -x + b (b is greater by 2 because of difference of 2 between -1 and 1)
            return True    

    if is_king_checked(queen_pos, king_pos):
        # at corners
        if king_pos in [(1,1),(1,8),(8,8),(8,1)]:
            if is_queen_in_range(queen_pos, king_pos):
                return 3
            else:
                return 2    
        # at left and right border
        elif king_pos[0] == 1 or king_pos[0] == 8:
            if is_queen_in_range(queen_pos, king_pos):
                return 5
            else:
                if king_pos[0] == queen_pos[0]:
                    return 3
                else:
                    return 4         
        # at top and bottom border
        elif king_pos[1] == 1 or king_pos[1] == 8:
            if is_queen_in_range(queen_pos, king_pos):
                return 5
            else:
                if king_pos[1] == queen_pos[1]:
                    return 3
                else:
                    return 4         
        # in the middle
        else:
            if is_queen_in_range(queen_pos, king_pos):
                return 7
            else:
                return 6
    else:
        return -1


