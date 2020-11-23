'''
MinWindow substring from codersbyte
October 2020 Jakub Kazimierski
'''

from collections import Counter

EMPTY_COUNTER = Counter()

def MinWindowSubstring(strArr):
    '''
    Have the function MinWindowSubstring(strArr) 
    take the array of strings stored in strArr, 
    which will contain only two strings, 
    the first parameter being the string N 
    and the second parameter being a string K 
    of some characters, and your goal is to determine 
    the smallest substring of N that contains all the 
    characters in K. For example: if strArr is ["aaabaaddae", "aed"] 
    then the smallest substring of N that contains the characters a, e, and d is "dae" 
    located at the end of the string. 
    So for this example your program should return the string dae.

    Another example: if strArr is ["aabdccdbcacd", "aad"] 
    then the smallest substring of N that contains all of 
    the characters in K is "aabd" which is located at the 
    beginning of the string. Both parameters will be strings 
    ranging in length from 1 to 50 characters and all of K's 
    characters will exist somewhere in the string N. 
    Both strings will only contains lowercase alphabetic characters.
    '''
    

    firstString, secondString = strArr

    #count appearence of letters in SecondString
    secondStringLettersCounter = Counter(secondString)  
    substringsList = []

    # O(n)
    for i in range(0, len(firstString)):
      
        firstStringLettersCounter = Counter()

      # O(n)
        for j in range(i, len(firstString)):
            firstStringLettersCounter[firstString[j]] += 1

            # if firstStringLettersCounter contains at least the same elements as secondStringLettersCounter
            if secondStringLettersCounter - firstStringLettersCounter == EMPTY_COUNTER and secondStringLettersCounter != EMPTY_COUNTER:

                  # strings indexing to j element
                  substringsList.append(firstString[i:j + 1])
                  
                  # go to i = i+1 and repeat process
                  break

    # return min of valid windows, key is length 
    if substringsList != []:
        return min(substringsList, key=len)
    else:
        return False    
    
def _input():

    exampleInput =  ["aaabaaddae", "aed"] 

    return exampleInput

def _output():

    exampleOutput = "dae" 

    return exampleOutput

