'''
Changing Sequence from Coderbyte
November 2020 Jakub Kazimierski
'''


def ChangingSequence(arr):
    '''
    Have the function ChangingSequence(arr) 
    take the array of numbers stored in arr 
    and return the index at which the numbers stop increasing 
    and begin decreasing or stop decreasing 
    and begin increasing. For example: if arr is [1, 2, 4, 6, 4, 3, 1] 
    then your program should return 3 because 6 is the last point 
    in the array where the numbers were increasing and the next number 
    begins a decreasing sequence. The array will contain at least 3 numbers 
    and it may contains only a single sequence, increasing or decreasing. 
    If there is only a single sequence in the array, 
    then your program should return -1. 
    Indexing should begin with 0.
    '''

    #Below asserts type of input and asserts that input is not empty
    if len(arr) > 0:
        for i in arr:
            if type(i) != int:
                return "Wrong Input Type"
    else:
        return "Input is empty"             
    
    #Below assigns difference between vallues at first and second index in array
    difference = arr[0]-arr[1]

    for j in range(0,len(arr)-1):
        #region Commentary
        #Below works for both increasing and decreasing sequence at once
        #If sequence is increasing difference is negative integer
        #while sequence is increasing value of (arr[j]-arr[j+1]) is also negative integer
        #So difference*(arr[j]-arr[j+1]) is positive integer
        #When sequence changes for decreasing value of (arr[j]-arr[j+1]) becames positive integer 
        #so difference*(arr[j]-arr[j+1]) becames less than 0
        #endregion
        if difference*(arr[j]-arr[j+1])<0:
            return j

    #If sequence does not change
    return -1         
