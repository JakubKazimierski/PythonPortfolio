'''
Palindrome Creator from Coderbyte
December 2020 Jakub Kazimierski
I'm not quite glad about this code, but it 
covers all cases, which are wrongly interpreted at Coderbyte.
'''

def PalindromeCreator(strParam):
    '''
    Have the function PalindromeCreator(str) 
    take the str parameter being passed and 
    determine if it is possible to create a 
    palindromic string of minimum length 3 
    characters by removing 1 or 2 characters. 
    
    For example: if str is "abjchba" then 
    you can remove the characters jc to produce 
    "abhba" which is a palindrome. 
    For this example your program should return the 
    two characters that were removed with no delimiter 
    and in the order they appear in the string, so "jc". 
    If 1 or 2 characters cannot be removed to produce a 
    palindrome, then return the string "not possible".

    If the input string is already a palindrome, 
    your program should return the string palindrome. 
    Your program should always remove the characters that 
    appear earlier in the string. 
    
    In the example above, you can also remove ch to form a 
    palindrome but jc appears first, so the correct answer is jc.

    The input will only contain lowercase alphabetic characters. 
    Your program should always attempt to create the longest palindromic 
    substring by removing 1 or 2 characters 
    The 2 characters you remove do not have to be adjacent in the string.
    '''
    try:
        # if it is already palindrome
        if strParam[::-1] == strParam:
            return "palindrome"
        else:
            # counter for first match remeber
            counter = 0
            output = []

            # make lenght of param longer, in order to chek all indexes
            strParam_longer = strParam + " "
            # below checks if lack of one letter inside string is enough to create palindrome
            for i in range (1, len(strParam_longer)):
                temp_String = strParam_longer[0:i-1] + strParam_longer[i:len(strParam_longer)-1]
                
                # if it is, return this letter
                if temp_String[::-1] == temp_String:
                    return strParam[i-1]
                
                temp_String_longer = temp_String + " "
                # if it is not, try next letter
                for j in range (1, len(temp_String_longer)):
                    temp_String_second = temp_String_longer[0:j-1] + temp_String[j:len(temp_String_longer)-1]
                    # if lack of two letters is enough return those letters
                    if temp_String_second[::-1] == temp_String_second:
                        # return first output
                        if counter == 0:
                            output = [letter for letter in strParam if letter not in temp_String_second]
                            counter += 1

            if len(output) != 0:
                return "".join(letter for letter in output)
            else:        
                # if 2 letters was not enough return not possible
                return "not possible"

    except(AttributeError, TypeError):
        return -1

def _input():

    sampleList = "abjchba"

    return sampleList

def _output():

    sampleString = "jc"

    return sampleString
