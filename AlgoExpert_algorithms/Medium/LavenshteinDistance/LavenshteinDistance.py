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

    '''
    # time O(n*m) where n is lenght of str1 and m of str2
    # space O(n*m)
    # dynamic programming approach

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
    '''

    # time O(n*m) where n is lenght of str1 and m of str2
    # space O(min(n,m))
    # dynamic programming approach
    small_str = str1 if len(str1) < len(str2) else str2
    big_str = str1 if len(str1) >= len(str2) else str2

    even_edits = [col_id for col_id in range(len(small_str)+1)]
    odd_edits = [None for col_id in range(len(small_str)+1)]

    for row_id in range(1, len(big_str)+1):
        if row_id % 2 == 1:
            current_edits = odd_edits
            previous_edits = even_edits
        else:
            previous_edits = odd_edits
            current_edits = even_edits

        # below line is evaluation of row in full matrix
        # 0 <- current_edits[0] in curr iteration
        # 1 <- current_edits[0] in curr iteration
        # 2 <- current_edits[0] in curr iteration
        # 3 <- current_edits[0] in curr iteration
        # ...
        current_edits[0] = row_id

        for col_id in range(1, len(small_str)+1):
            if small_str[col_id-1] == big_str[row_id-1]:
                current_edits[col_id] = previous_edits[col_id-1]
            else:
                current_edits[col_id] = 1 + min(previous_edits[col_id-1],previous_edits[col_id], current_edits[col_id-1])

    return even_edits[-1] if len(big_str) % 2 == 0 else odd_edits[-1]
