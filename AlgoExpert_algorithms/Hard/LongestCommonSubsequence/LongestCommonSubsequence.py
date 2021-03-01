'''
Longest Common Subsequence from AlgoExpert.io
March 2021 Jakub Kazimierski
'''

def longestCommonSubsequence(str1, str2):
    '''
    Write a function that takes in two strings
    and returns their longest common subsequence.

    A subsequence of a string is a set of characters
    that aren't necessarily adjacent in the string but
    that are in the same order as they appear in the string.
    For instance, the characters ["a", "c", "d"] form a subsequence
    of the string "abcd", and so do the charaters ["b", "d"]. Note
    that a single character in a string and the string itself are
    both valid subsequences of the string. 

    You can assume that there will only be one longest common
    subsequence.
    '''
    
    # empty matrix NxM where n and m are lengths of strings
    lcs = [[[] for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

    for row_id in range(1, len(str2) + 1):
        for col_id in range(1, len(str1) + 1):
            if str2[row_id-1] == str1[col_id-1]:
                lcs[row_id][col_id] = lcs[row_id-1][col_id-1] + [str2[row_id-1]]
            else:
                lcs[row_id][col_id] = max(lcs[row_id-1][col_id], lcs[row_id][col_id-1], key=len) 

    return lcs[-1][-1]

    # Time O(n*m*min(m,n)) due to comparision each row and column 
    # and also concatenating string at each comparition in worst case
    # Space O(n*m*min(n,m))              