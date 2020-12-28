'''
Eight Queens from Coderbyte
December 2020 Jakub Kazimierski
'''

def EightQueens(strArr):
    '''
    Have the function EightQueens(strArr) 
    read strArr which will be an array 
    consisting of the locations of eight 
    Queens on a standard 8x8 chess board 
    with no other pieces on the board. 
    The structure of strArr will be the 
    following: ["(x,y)", "(x,y)", ...] where 
    (x,y) represents the position of the current 
    queen on the chessboard (x and y will both range 
    from 1 to 8 where 1,1 is the bottom-left of the chessboard
    and 8,8 is the top-right). Your program should determine if 
    all of the queens are placed in such a way where none of 
    them are attacking each other. If this is true for the given 
    input, return the string true otherwise return the first queen 
    in the list that is attacking another piece in the same format 
    it was provided.

    For example: if strArr is ["(2,1)", "(4,2)", "(6,3)", "(8,4)", 
    "(3,5)", "(1,6)", "(7,7)", "(5,8)"] then your program should return 
    the string true. The corresponding chessboard of queens for this input 
    is below (taken from Wikipedia).
    '''
    
    oblique_right = []
    oblique_right_elems = []

    oblique_left = []
    oblique_left_elems = []

    vertical = []
    vertical_elems = []

    horizontal = []
    horizontal_elems = []

    # due to task first digit is for y axis, secon for x
    for elem in strArr:
        elem = elem.replace("(","").replace(")","").replace(",","")

        # count b from y = x + b 
        oblique_right.append( (int(elem[0])) - (int(elem[1])))
        oblique_right_elems.append("(" + elem[0] + "," + elem[1] + ")")

        # count b from y = -x + b 
        oblique_left.append( (int(elem[0])) + (int(elem[1])))
        oblique_left_elems.append("(" + elem[0] + "," + elem[1] + ")")


        horizontal.append(int(elem[0]))
        horizontal_elems.append("(" + elem[0] + "," + elem[1] + ")")

        vertical.append(int(elem[1]))
        vertical_elems.append("(" + elem[0] + "," + elem[1] + ")")

    possible_outputs = set()
    if len(set(oblique_right)) != 8:
        for index in range(0, len(oblique_right)-1):
            for index_II in range(index + 1, len(oblique_right)):
                if oblique_right[index] == oblique_right[index_II]:
                    possible_outputs.add(oblique_right_elems[index])

    if len(set(oblique_left)) != 8:
        for index in range(0, len(oblique_left)-1):
            for index_II in range(index + 1, len(oblique_left)):
                if oblique_left[index] == oblique_left[index_II]:
                    possible_outputs.add(oblique_left_elems[index])


    if len(set(vertical)) != 8:
        for index in range(0, len(vertical)-1):
            for index_II in range(index + 1, len(vertical)):
                if vertical[index] == vertical[index_II]:
                    possible_outputs.add(vertical_elems[index])

    if len(set(horizontal)) != 8:
        for index in range(0, len(horizontal)-1):
            for index_II in range(index + 1, len(horizontal)):
                if horizontal[index] == horizontal[index_II]:
                    possible_outputs.add(horizontal_elems[index])

    if len(possible_outputs) != 0:
        first_mistake = min(strArr.index(elem) for elem in possible_outputs)

        return strArr[first_mistake]

    return "true"
