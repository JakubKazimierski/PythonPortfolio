'''
String Merge from Coderbyte
December 2020 Jakub Kazimierski
'''

import re

def StringMerge(strParam):
    '''
    Have the function StringMerge(strParam) 
    read the str parameter being passed which 
    will contain a large string of alphanumeric 
    characters with a single asterisk character 
    splitting the string evenly into two separate 
    strings. Your goal is to return a new string 
    by pairing up the characters in the corresponding 
    locations in both strings. 
    
    For example: if str is "abc1*kyoo" then your program 
    should return the string "akbyco1o" because a pairs with k, 
    b pairs with y, etc. 
    The string will always split evenly with the 
    asterisk in the center.
    '''
    try:
        output = ""
        string_I , string_II = re.split(r'\*', strParam)


        for char_I, char_II in zip(string_I, string_II):
            output += char_I + char_II

        return output

    except(TypeError):
        return -1    