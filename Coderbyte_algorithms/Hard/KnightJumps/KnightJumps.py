'''
Knight Jumps from Coderbyte
January 2021 Jakub Kazimierski
'''

def KnightJumps(strParam):
    '''
    Have the function KnightJumps(str) 
    read str which will be a string consisting 
    of the location of a knight on a standard 8x8 
    chess board with no other pieces on the board. 
    The structure of str will be the following: "(x y)" 
    which represents the position of the knight with x and 
    y ranging from 1 to 8. Your program should determine 
    the number of spaces the knight can move to from a given 
    location. 
    
    For example: if str is "(4 5)" then your program should 
    output 8 because the knight can move to 8 different spaces from 
    position x=4 and y=5.
    '''
    
    def move_knight(x, y, endpoints):
        '''
        Returns array with possible endpoints
        for knight, from given at input (x, y)
        '''

        # all possible moves
        moves = [(x - 2, y + 1), (x - 2, y - 1), (x + 2, y + 1), (x + 2, y - 1),\
            (x - 1, y + 2), (x - 1, y - 2), (x + 1, y + 2), (x + 1, y - 2)]

        for move in moves:
            if  8 >= move[0] >= 1 and 8 >= move[1] >= 1:
                endpoints.append(move)
        return endpoints        

    x, y = int(strParam[1]), int(strParam[-2])

    moves = move_knight(x, y, [])

    return len(moves)
