'''
Palindrome Swapper from Coderbyte
December 2020 Jakub Kazimierski
'''

def PalindromeSwapper(strParam):
    '''
    Have the function PalindromeSwapper(strParam) 
    take the str parameter being passed and determine 
    if a palindrome can be created by swapping two 
    adjacent characters in the string. 
    If it is possible to create a palindrome, 
    then your program should return the palindrome, 
    if not then return the string -1. 
    The input string will only contain alphabetic 
    characters. 
    
    For example: if str is "rcaecar" then you can create 
    a palindrome by swapping the second and third characters, 
    so your program should return the string "racecar" which 
    is the final palindromic string.
    '''
    
    try:
        # if input already is palindrome
        if strParam[::-1] == strParam:
            return strParam

        # below cheks each possible swap in string
        tempString = list(strParam)
        for index in range(0, len(tempString)-1):
            
            tempString[index], tempString[index+1] = tempString[index+1], tempString[index]
            
            if "".join(tempString)[::-1] == "".join(tempString):
                return "".join(tempString)

            tempString = list(strParam)

        return "-1"    

    except(TypeError):
        return -1    