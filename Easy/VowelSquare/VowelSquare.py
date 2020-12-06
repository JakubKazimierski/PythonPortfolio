'''
Vowel Square from Coderbyte
December 2020 Jakub Kazimierski
'''

def VowelSquare(strArr):
    '''
    Have the function VowelSquare(strArr) take the strArr 
    parameter being passed which will be a 2D matrix of some 
    arbitrary size filled with letters from the alphabet, 
    and determine if a 2x2 square composed entirely of vowels 
    exists in the matrix. 

    For example: strArr is ["abcd", "eikr", "oufj"] then this 
    matrix looks like the following:

    a b c d
    e i k r
    o u f j

    Within this matrix there is a 2x2 square of vowels starting 
    in the second row and first column, namely, ei, ou. 
    
    If a 2x2 square of vowels is found your program should return
    the top-left position (row-column) of the square, so for this 
    example your program should return 1-0. If no 2x2 square of 
    vowels exists, then return the string not found. 
    If there are multiple squares of vowels, return the one 
    that is at the most top-left position in the whole matrix. 
    The input matrix will at least be of size 2x2.
    '''

    try:

        possible_outputs = {}
        vowels = ["a","e","i","o","u"]

        # below looks for 2x2 matrix built from vowels
        for y_index in range(0, len(strArr) - 1):
            for x_index in range (0, len(strArr[y_index]) - 1):
                # if in row are 2 adjacent vowels
                if strArr[y_index][x_index] in  vowels and strArr[y_index][x_index + 1] in vowels:
                    # if in row under are 2 adjacent vowels with same indexes as above
                    if strArr[y_index + 1][x_index] in  vowels and strArr[y_index + 1][x_index + 1] in vowels:
                        # below adds top-left index as key into dict, with sum of indexes as value
                        possible_outputs[str(y_index)+"-"+str(x_index)] = y_index + x_index     
        
        # below finds min value in dict, and assigns to variable it's key
        min_output =  min(possible_outputs.keys(), key=(lambda k: possible_outputs[k]))

        return min_output

    except(AttributeError, TypeError):
        return -1

def _input():

    sampleInp = ["aqrst", "ukaei", "ffooo"]

    return sampleInp 

def _output():

    sampleOut = "1-2"

    return sampleOut