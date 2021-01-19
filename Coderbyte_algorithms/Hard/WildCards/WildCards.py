'''
Wild Cards from Coderbyte
January 2021 Jakub Kazimierski
'''

def WildCards(strParam):
    '''
    Have the function Wildcards(str) read 
    str which will contain two strings separated 
    by a space. The first string will consist of the 
    following sets of characters: +, *, $, and {N} which 
    is optional. The plus (+) character represents a single 
    alphabetic character, the ($) character represents a number 
    between 1-9, and the asterisk (*) represents a sequence of 
    the same character of length 3 unless it is followed by {N} 
    which represents how many characters should appear in the 
    sequence where N will be at least 1. Your goal is to determine 
    if the second string exactly matches the pattern of the first 
    string in the input.

    For example: if str is "++*{5} jtggggg" then the second string 
    in this case does match the pattern, so your program should return 
    the string true. If the second string does not match the pattern 
    your program should return the string false.
    '''
    decrypted, word = strParam.split(" ")

    for char_id in range(len(decrypted)):
        '''
        At each iteration word is cutted, in case no match
        character, iteration just continue till next match
        '''
        
        if decrypted[char_id] == "+":
            if word[0].isalpha() == False:
                return "false"
            word = word[1:]
        
        elif decrypted[char_id] == "$":
            if word[0].isdigit() == False:
                return "false"
            word = word[1:]
        
        elif decrypted[char_id] == "*":
        
            if char_id < len(decrypted) - 1: 
                if decrypted[char_id + 1] == "{":
        
                    x = char_id + 1
                    while decrypted[x] != "}":
                        x += 1
                    num_occurence = int(decrypted[char_id+2 : x])
        
                    # if sequence does not contain the same elements or is shorter
                    if len(word[:num_occurence]) < num_occurence or len(set(word[:num_occurence])) != 1:
                        return "false"
                    word = word[num_occurence:]
                    
                else:
                    if len(word[:3]) < 3 or len(set(word[:3])) != 1:
                        return "false"
                    word = word[3:]
            else:
                if len(word) < 3 or len(set(word[:3])) != 1:
                    return "false"
                word = word[3:]

    if len(word) == 0:
        return "true"

    return "false"                
                    