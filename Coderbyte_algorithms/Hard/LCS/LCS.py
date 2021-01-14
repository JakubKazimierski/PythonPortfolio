'''
LCS from Coderbyte 
January 2021 Jakub Kazimierski
'''

from itertools import combinations

def LCS(strArr):
    '''
    Have the function LCS(strArr) 
    take the strArr parameter being passed 
    which will be an array of two strings 
    containing only the characters {a,b,c} 
    and have your program return the length 
    of the longest common subsequence common 
    to both strings. A common subsequence for 
    two strings does not require each character 
    to occupy consecutive positions within the 
    original strings. 
    
    For example: if strArr is ["abcabb","bacb"] 
    then your program should return 3 because one 
    longest common subsequence for these two strings 
    is "bab" and there are also other 3-length 
    subsequences such as "acb" and "bcb" but 3 is 
    the longest common subsequence for these two strings.
    '''
    
    list_I = list(strArr[0])
    list_II = list(strArr[1])
 
    # iterate from longest combinations
    for length in range(len(list_I), 0, -1):
        if length <= len(list_II):
            combination_list_I = []
            combination_list_II = []
            combination_list_I.extend(list(combinations(list_I, length)))
            combination_list_II.extend(list(combinations(list_II, length)))

            for comb in combination_list_I:
                for comb_II in combination_list_II:
                    if comb == comb_II:
                        return len(comb)
    # if no subsequences of at least legth 1 match
    return 0
