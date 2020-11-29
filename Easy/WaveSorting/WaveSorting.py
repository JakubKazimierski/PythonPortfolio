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

    try:

        
        sortedArray = sorted(arr)

        oddIndexesMetcher = 0
        # first half of sorted array, assign at odd indexes of primal array
        for index in range(0, int(len(sortedArray)/2)):
            arr[int((2*oddIndexesMetcher+1)%len(arr))] = sortedArray[index]
            oddIndexesMetcher += 1
        
        evenIndexesMatcher = 0
        # second half of sorted array, assign at even indexes of primal array
        for index in range(int(len(sortedArray)/2), len(sortedArray)):
            arr[int((2*evenIndexesMatcher)%len(arr))] = sortedArray[index]
            evenIndexesMatcher += 1
        # in that case lower numbers will be surrounded by greater

        # below checks odd indexes
        for index in range(1, len(arr)-1, 2):
            if arr[index-1] <= arr[index] or arr[index] >= arr[index+1]:
                return "false"

        return "true"        

    except(AttributeError, TypeError):
        return -1    


def _input():

    exampleInput = [0, 4, 22, 4, 14, 4, 2]

    return exampleInput

def _output():

    exampleOutput = "true"

    return exampleOutput