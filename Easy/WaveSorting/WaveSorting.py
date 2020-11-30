'''
WaveSorting from Coderbyte
November 2020 Jakub Kazimierski
'''

def WaveSorting(arr):
    '''
    Have the function WaveSorting(arr) 
    take the array of positive integers 
    stored in arr and return the string 
    true if the numbers can be arranged 
    in a wave pattern: a1 > a2 < a3 > a4 < a5 > ..., 
    otherwise return the string false. 
    
    For example, if arr is: [0, 1, 2, 4, 1, 4], 
    then a possible wave ordering of the numbers is: 
    [2, 0, 4, 1, 4, 1]. 
    
    So for this input your program should return the 
    string true. 
    The input array will always contain at least 2 elements.
    '''


    
    frequecy = {}

    # if any element occurs more times than half lenght of array
    # it will be not possible to surround it with other various elements (Dirrichlet pigeonhole principle)
    for element in arr:
        frequecy[element] = frequecy.get(element, 0) + 1

    mostCommon = max(value for key, value in frequecy.items())

    if mostCommon > len(arr)//2:
        return "false"
    else:
        return "true"    



def _input():

    exampleInput = [0, 4, 22, 4, 14, 4, 2]

    return exampleInput

def _output():

    exampleOutput = "true"

    return exampleOutput