'''
K Unique Characters from Coderbyte
December 2020 Jakub Kazimierski
'''

def K_Unique_Characters(strParam):
    '''
    Have the function KUniqueCharacters(str) 
    take the str parameter being passed and 
    find the longest substring that contains k 
    unique characters, where k will be the first 
    character from the string. The substring will 
    start from the second position in the string 
    because the first character will be the integer k. 
    
    For example: if str is "2aabbacbaa" there are several 
    substrings that all contain 2 unique characters, namely: 
    ["aabba", "ac", "cb", "ba"], but your program should return 
    "aabba" because it is the longest substring. 
    If there are multiple longest substrings, then return the first 
    substring encountered with the longest length. k will range from 1 to 6.
    '''

    k_unique = int(strParam[0])
    
    possible_outputs = []
    temp_substring = ""
    
    # for this task i assume that in strParam are at least k_uniqe characters
    for index in range(1, (len(strParam)-k_unique) + 1):
        # below appends all possible substrings with k unique chars to possible outputs
        temp_substring = ""
        for char in strParam[index:]:
            temp_substring += char
            if len(set(temp_substring)) == k_unique:
                possible_outputs.append(temp_substring)
            if len(set(temp_substring)) > k_unique:
                break

    return max(possible_outputs, key=len)