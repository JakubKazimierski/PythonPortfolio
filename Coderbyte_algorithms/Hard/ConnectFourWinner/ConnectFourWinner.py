'''
Connect Four Winner from Coderbyte
January 2021 Jakub Kazimierski
'''

def ConnectFourWinner(strArr):
    '''
    Have the function ConnectFourWinner(strArr) 
    read the strArr parameter being passed which will 
    represent a 6x7 Connect Four board. The rules of 
    the game are: two players alternate turns and place 
    a colored disc down into the grid from the top and 
    the disc falls down the column until it hits the 
    bottom or until it hits a piece beneath it. 
    The object of the game is to connect four of one's 
    own discs of the same color next to each other vertically, 
    horizontally, or diagonally before your opponent. 
    The input strArr will represent a Connect Four board 
    and it will be structured in the following format: 
    ["R/Y","(R,Y,x,x,x,x,x)","(...)","(...)",...)] where R 
    represents the player using red discs, Y represents the player 
    using yellow discs and x represents an empty space on the board. 
    The first element of strArr will be either R or Y and it represents 
    whose turn it is. Your program should determine, based on whose turn 
    it is, whether a space exists that can give that player a win. If a 
    space does exist your program should return the space in the following format:
    (RxC) where R=row and C=column. If no space exists, return the string none. 
    The board will always be in a legal setup.

    For example, if strArr is:
    ["R","(x,x,x,x,x,x,x)","(x,x,x,x,x,x,x)","(x,x,x,x,x,x,x)","(x,x,x,R,x,x,x)","(x,x,x,R,x,x,x)","(x,x,x,R,Y,Y,Y)"] 
    then your program should return (3x4).

    Another example, if strArr is: 
    ["Y","(x,x,x,x,x,x,x)","(x,x,x,x,x,x,x)","(x,x,x,x,x,x,x)","(x,x,Y,Y,x,x,x)","(x,R,R,Y,Y,x,R)","(x,Y,R,R,R,Y,R)"] 
    then your program should return (3x3).
    '''
    
    turn = strArr[0]
    matrix = []
    for row in strArr[1:]:
        matrix.append(row.replace("(", "").replace(")", "").split(","))


    def check_line(x, y):
        
        diagonal_I = [(3,3), (2,2), (1,1), (-1,-1), (-2,-2), (-3,-3)]
        diagonal_II = [(-3,3), (-2,2), (-1,1), (1,-1), (2,-2), (3,-3)]
        row = [(0,-3),(0,-2), (0,-1), (0,1), (0,2), (0,3)]
        column = [(-3,0),(-2,0), (-1, 0), (1,0), (2,0), (3,0)]

        moves_list = [diagonal_I, diagonal_II, row, column]

        for line in moves_list:
            count = 0

            # below checks adjacent 3 points with givemn point at input
            # if each of them is equal to R or Y, return point as output with incremented indexes
            for index in range(0, 4):
                count = 0
                for move in line[index : index+3]:
                    new_x = x + move[0]       
                    new_y = y + move[1]

                    if 0 <= new_x < 6 and 0 <= new_y < 7:
                        if matrix[new_x][new_y] == turn:
                            count += 1
                        else:
                            break
                    else:
                        break            
                if count == 3:
                    # as indexing from 1
                    return "(" + str(x+1) + "x" + str(y+1) + ")"

    for row_id in range(len(matrix)):
        for col_id in range(len(matrix[0])):
            if matrix[row_id][col_id] == "x":
                output = check_line(row_id, col_id)

            if output != None:
                return output

    return "none"


