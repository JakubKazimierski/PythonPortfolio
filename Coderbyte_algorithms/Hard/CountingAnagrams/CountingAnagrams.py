'''
Counting Anagrams from Coderbyte
January 2021 Jakub Kazimierski
'''

from itertools import permutations

def CountingAnagrams(strParam):
    '''
    Have the function CountingAnagrams(str) 
    take the str parameter and determine how 
    many anagrams exist in the string. An anagram 
    is a new word that is produced from rearranging 
    the characters in a different word.
    
    For example: cars and arcs are anagrams. 
    Your program should determine how many anagrams exist 
    in a given string and return the total number. 
    
    For example: if str is "cars are very cool so are arcs and my os" 
    then your program should return 2 because "cars" and "arcs" form 1 
    anagram and "so" and "os" form a 2nd anagram. The word "are" occurs 
    twice in the string but it isn't an anagram because it is the same word 
    just repeated. The string will contain only spaces and lowercase letters, 
    no punctuation, numbers, or uppercase letters.
    '''

    words_list = list(strParam.split(" "))
    anagram_list = []

    for word in words_list:
        perm = list(permutations(list(word), len(word)))

        for anagram in perm:
            possible_one = "".join(char for char in anagram)
            # if anagram is not the same as word, and it is not anagram formed by already appended one
            # and it is not repeated
            if possible_one in words_list and possible_one != word and\
                 word not in anagram_list and possible_one not in anagram_list:
                anagram_list.append(possible_one)

    return len(anagram_list)            