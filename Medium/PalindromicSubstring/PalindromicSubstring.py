'''
Palindromic Substring from Coderbyte
December 2020 Jakub Kazimierski
'''

def PalindromicSubstring(strParam):
    '''
    Have the function PalindromicSubstring(str) 
    take the str parameter being passed and find 
    the longest palindromic substring, which means 
    the longest substring which is read the same forwards 
    as it is backwards. 
    
    For example: if str is "abracecars" 
    then your program should return the string racecar because 
    it is the longest palindrome within the input string.

    The input will only contain lowercase alphabetic characters. 
    The longest palindromic substring will always be unique, 
    but if there is none that is longer than 2 characters, 
    return the string none.
    '''
    
    palindromes = []
    for index in range(len(strParam)):

        possible_palindrome = ""        
        for traverse_id in range(index, len(strParam)):
            possible_palindrome += strParam[traverse_id]

            if len(possible_palindrome) > 2 and\
                 possible_palindrome == possible_palindrome[::-1]:
                 palindromes.append(possible_palindrome)

    if len(palindromes) > 0:
        return max(palindromes, key=len)

    return "none"                 