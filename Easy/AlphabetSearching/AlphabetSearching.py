'''
AlphabetSearching from Coderbyte
Decmber 2020 Jakub Kazimierski
'''
import string
import re

def AlphabetSearching(strParam):
    '''
    Have the function AlphabetSearching(str) 
    take the str parameter being passed and 
    return the string true if every single 
    letter of the English alphabet exists in 
    the string, otherwise return the string false. 
    
    For example: if str is "zacxyjbbkfgtbhdaielqrm45pnsowtuv" 
    then your program should return the string true because every 
    character in the alphabet exists in this string even though 
    some characters appear more than once.
    '''

    all_letters = string.ascii_lowercase

    # below gets all alpha chars from strParam.lower()
    only_alpha = set(re.findall(r'[a-zA-z]', strParam.lower()))

    # if all letters from ascii letters lowercase, are in strParam return "true"
    return "true" if all(char in only_alpha for char in all_letters) else  "false"



def _input():

    sampleList = "zacxyjbbkfgtbhdaielqrm45pnsowtuv" 

    return sampleList

def _output():

    sampleString = "true"

    return sampleString
