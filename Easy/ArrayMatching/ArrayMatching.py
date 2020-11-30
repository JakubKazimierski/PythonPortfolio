'''
Array Matching from Coderbyte
November 2020 Jakub Kazimierski
'''
import itertools

def ArrayMatching(strArr):
    '''
    Have the function ArrayMatching(strArr) 
    read the array of strings stored in strArr 
    which will contain only two elements, 
    both of which will represent an array of positive integers. 
    
    For example: if strArr is ["[1, 2, 5, 6]", "[5, 2, 8, 11]"], 
    then both elements in the input represent two integer arrays, 
    and your goal for this challenge is to add the elements in 
    corresponding locations from both arrays. 
    For the example input, your program should do the following additions: 
    [(1 + 5), (2 + 2), (5 + 8), (6 + 11)] 
    which then equals [6, 4, 13, 17]. 
    
    Your program should finally return this resulting array 
    in a string format with each element separated by a hyphen: 6-4-13-17.

    If the two arrays do not have the same amount of elements, 
    then simply append the remaining elements onto the new array 
    Both arrays will be in the format: [e1, e2, e3, ...] 
    where at least one element will exist in each array.
    '''
    try:

        # evaluate string expression
        lists = list(map(eval, strArr))
        # map sum for two elements of zipped list (to the longest one, shorter is filled with zeros) 
        output = map(sum, itertools.zip_longest(lists[0], lists[1], fillvalue=0))
        return "-".join(map(str, output))

    except (AttributeError, TypeError):
        return -1
    

def _input():

    exampleInput = ["[1, 2, 5, 6]", "[5, 2, 8, 11]"]

    return exampleInput

def _output():

    exampleOutput = "6-4-13-17"
    return exampleOutput
    