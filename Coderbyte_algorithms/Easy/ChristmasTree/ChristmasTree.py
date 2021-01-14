'''
ChristmasTree with explanation
December 2020 Jakub Kazimierski
'''

def ChristmasTree(num):
    '''
    Prints christmas tree of defined legth.

        # at each missing space in each row iteration
        # goes 2x more of '*' char (one half for each side of tree to keep balance) and plus one '*' in the middle
        # 
        # it's like:
        #      0 missing spaces, 2*0 of '*' at each side of tree plus one '*' at top of the tree
        #      1 missig space, 2*1 of '*' at each side of tree plus one '*' in the middle
        #      2 missing spaces, 2*2 of '*' at each side of tree plus one '*' in the middle
        #      ...
        #      num missing spaces, 2*num od '*' at each side of tree plus one '*' in the middle   
    '''

    for row in range(0, num):
        print((num-row)*" " + (2*row+1)*"*")
        
    return 0