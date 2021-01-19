'''
Wildcard Characters from Coderbyte
January 2021 Jakub Kazimierski
'''

def WildcardCharacters(strParam):
    '''
    Have the function WildcardCharacters(str) 
    read str which will contain two strings 
    separated by a space. The first string will 
    consist of the following sets of characters: 
    +, *, and {N} which is optional. The plus (+) 
    character represents a single alphabetic character, 
    the asterisk (*) represents a sequence of the same character 
    of length 3 unless it is followed by {N} which represents 
    how many characters should appear in the sequence where N will 
    be at least 1. Your goal is to determine if the second string 
    exactly matches the pattern of the first string in the input.

    For example: if str is "++*{5} gheeeee" then the second string in 
    this case does match the pattern, so your program should return the 
    string true. If the second string does not match the pattern your 
    program should return the string false.
    '''
    
    pattern , word = strParam.split(" ")
    for i in range(len(pattern)):
        '''
        in each iteration word is cutted at
        the beginning
        '''
        # normal case
        if  pattern[i]  == "+":
            word = word[1:]
        elif pattern[i] == "*" :
            if i != len(pattern)  - 1 :
                # below converts occurences num for int
                if pattern[i+1]  == "{" :
                    x = i+1
                    while pattern[x]!= '}':
                        x+=1
                    n = int(pattern[i+2:x])
                    if len(word) < n or len(set(word[:n])) != 1 :
                        return "false"
                    word = word[n:]
                else:
                    # if  substring is not length of 3 or those are diff characters
                    if len(word)<3 or len(set(word[:3])) != 1: return "false"          
                    word = word[3:]
            else:
                # if last substring is not length of 3 or those are diff characters
                if len(word)<3 or len(set(word[:3]))!= 1:return "false"
                word = word[3:]
    
    return "true" if len(word) == 0 else "false"