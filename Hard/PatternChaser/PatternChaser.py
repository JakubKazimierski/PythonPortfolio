'''
Pattern Chaser from Coderbyte
January 2021 Jakub Kazimierski
'''

import re

def PatternChaser(strParam):
    '''
    Have the function PatternChaser(str) 
    take str which will be a string and return 
    the longest pattern within the string. A pattern 
    for this challenge will be defined as: if at least 2 
    or more adjacent characters within the string repeat 
    at least twice. So for example "aabecaa" contains the 
    pattern aa, on the other hand "abbbaac" doesn't contain 
    any pattern. Your program should return yes/no pattern/null.
    
    So if str were "aabejiabkfabed" the output should be yes abe. 
    If str were "123224" the output should return no null. The string 
    may either contain all characters (a through z only), integers, 
    or both. But the parameter will always be a string type. The maximum 
    length for the string being passed in will be 20 characters. If a 
    string for example is "aa2bbbaacbbb" the pattern is "bbb" and not "aa". 
    You must always return the longest pattern possible.
    '''
    
    possible_patterns = set()
    temp_seq = ""
    for char_id in range(len(strParam)-1):
        for char_id_II in range(char_id + 2, len(strParam)):
            temp_seq += strParam[char_id:char_id_II] 

            if len(re.findall(temp_seq, strParam)) >= 2:
                possible_patterns.add(temp_seq)
            temp_seq = "" 

    if len(possible_patterns) == 0:
        return "no null"

    return "yes " + max(possible_patterns, key=len)    