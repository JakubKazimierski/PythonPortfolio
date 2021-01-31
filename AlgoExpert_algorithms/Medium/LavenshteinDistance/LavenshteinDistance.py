'''
Lavenshtein Distance from AlgoExpert.io
January 2021 Jakub Kazimierski
'''

def lavenshteinDistance(str1, str2):
    '''
    Write a function that takes in
    two strings and returns the minimum
    number of edit operations that need
    to be performed on the first string
    to obtain the second string.

    There are three edit operations:
    insertion of a character, deletion
    of a character, and substitution
    of a character for another.
    '''

    #time O(n*m) where n is lenght of str1 and m of str2
    # space O(n*m)

    # below contains counting of empty strigns  
    # and makes n*m matrix comparing letters from strings 
    edits = [[idx for idx in range(len(str1)+1)] for idx_2 in range(len(str2)+1)]

    # for empty string increments each operations num
    # for each letter in each row
    for row_id in range(1, len(str2)+1):
        edits[row_id][0] = edits[row_id-1][0] + 1

    for row_id in range(1, len(str2)+1):
        for col_id in range(1, len(str1)+1):
            # assign same values of operations per letter if letters are the same
            if str1[col_id-1] == str2[row_id-1]:
                edits[row_id][col_id] = edits[row_id-1][col_id-1]
            else:
                # choose minimum from adjacent previous operations
                edits[row_id][col_id] = 1 + min(edits[row_id][col_id-1], edits[row_id-1][col_id-1], edits[row_id-1][col_id])

    return edits[-1][-1]





