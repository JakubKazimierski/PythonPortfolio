'''
Chessboard Traveling from Coderbyte
January 2021 Jakub Kazimierski
'''

def ChessboardTraveling(strParam):
    '''
    Have the function ChessboardTraveling(str) 
    read str which will be a string consisting 
    of the location of a space on a standard 8x8 
    chess board with no pieces on the board along 
    with another space on the chess board. The 
    structure of str will be the following: "(x y)(a b)" 
    where (x y) represents the position you are currently 
    on with x and y ranging from 1 to 8 and (a b) represents 
    some other space on the chess board with a and b also 
    ranging from 1 to 8 where a > x and b > y. Your program 
    should determine how many ways there are of traveling 
    from (x y) on the board to (a b) moving only up and to 
    the right. 
    
    For example: if str is (1 1)(2 2) then your program should 
    output 2 because there are only two possible ways to travel 
    from space (1 1) on a chessboard to space (2 2) while making 
    only moves up and to the right.
    '''
    
    strParam = strParam.replace("(", "").replace(")", "").replace(" ", "")

    x, y = int(strParam[0]), int(strParam[1])
    a, b = int(strParam[2]), int(strParam[3])

    ways = []

    def traverse(x, y):
        '''
        Cheks all possible ways
        by recurency.
        '''
        if x == a and y == b:
            ways.append(1)
            return

        moves = [(1, 0), (0, 1)]
        for move in moves:
            next_x = x + move[0]
            next_y = y + move[1]
            if next_x <= a and next_y <= b:
                traverse(next_x, next_y)

    traverse(x, y)
    return len(ways)        
