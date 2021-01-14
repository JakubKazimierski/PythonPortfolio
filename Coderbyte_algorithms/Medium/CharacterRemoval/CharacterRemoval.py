'''
Character Removal from Coderbyte
December 2020 Jakub Kazimierski
'''

from itertools import combinations

def CharacterRemoval(strArr):
    '''
    Have the function CharacterRemoval(strArr) 
    read the array of strings stored in strArr, 
    which will contain 2 elements: the first element 
    will be a sequence of characters representing a word, 
    and the second element will be a long string of comma-separated 
    words, in alphabetical order, that represents a dictionary of 
    some arbitrary length. 
    
    For example: strArr can be: 
    ["worlcde", "apple,bat,cat,goodbye,hello,yellow,why,world"]. Your 
    goal is to determine the minimum number of characters, if any, 
    can be removed from the word so that it matches one of the words from 
    the dictionary. In this case, your program should return 2 because once 
    you remove the characters "c" and "e" you are left with "world" and 
    that exists within the dictionary. If the word cannot be found no matter 
    what characters are removed, return -1.
    '''
    
    list_of_chars = list(strArr[0])

    possible_words = [combinations(list_of_chars, lenght) for lenght in range(1, len(list_of_chars)+1)]
    
    lenght_max = 0
    for words in possible_words:
        for word in words:
            possible_out_word = "".join(word)
            if possible_out_word in strArr[1].split(","):
                if len(possible_out_word) > lenght_max:
                    lenght_max = len(possible_out_word)

    if lenght_max > 0:
        return len(strArr[0]) - lenght_max
        
    return -1
