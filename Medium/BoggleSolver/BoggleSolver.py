'''
Boggle Solver from Coderbyte
December 2020 Jakub Kazimierski
'''

# global variables
found = set()
moves = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]


def search(word, index, y, x, matrix):  
    '''
    Uses recurency to find all connected letters
    from given word in given matrix.
    '''
    # index of letter in word
    index += 1

    # if recurency reached end
    if index > len(word) - 1:
        found.add(word)
        return

    # below tries all possible moves
    for move in moves:
        y1 = move[0] + y
        x1 = move[1] + x
        if 0 <= y1 < len(matrix) and 0 <= x1 < len(matrix[0]):
            # if letter is at moved place in matrix, call recurency search
            if matrix[y1][x1] == word[index]:
                search(word, index, y1, x1, matrix)


def BoggleSolver(strArr):
    '''
    Have the function BoggleSolver(strArr) 
    read the array of strings stored in strArr, 
    which will contain 2 elements: the first element 
    will represent a 4x4 matrix of letters, and the 
    second element will be a long string of comma-separated 
    words each at least 3 letters long, in alphabetical order, 
    that represents a dictionary of some arbitrary length. 
    
    For example: strArr can be: ["rbfg, ukop, fgub, mnry", "bog,bop,gup,fur,ruk"]. 
    Your goal is to determine if all the comma separated words as the second parameter 
    exist in the 4x4 matrix of letters. For this example, the matrix looks like the following:

    r b f g
    u k o p
    f g u b
    m n r y

    The rules to make a word are as follows:

    1. A word can be constructed from sequentially adjacent spots in the matrix, 
    where adjacent means moving horizontally, vertically, or diagonally in any direction.

    2. A word cannot use the same location twice to construct itself.

    The rules are similar to the game of Boggle. So for the example above, 
    all the words exist in that matrix so your program should return the string true. 
    If all the words cannot be found, then return a comma separated string of the words 
    that cannot be found, in the order they appear in the dictionary.
    '''
        
    words = strArr[1].split(',')

    for word in words:
        # for each word create matrix
        matrix = [list(x) for x in strArr[0].split(', ')]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # start recurency method search from first letter in word
                if matrix[i][j] == word[0]:
                    # visited became empty due to avoid repeatition of letters
                    matrix[i][j] = ''
                    search(word, 0, i, j, matrix)

    missing = [word for word in words if word not in found]

    if missing == []:
        return 'true'

    return ','.join(missing)

        
