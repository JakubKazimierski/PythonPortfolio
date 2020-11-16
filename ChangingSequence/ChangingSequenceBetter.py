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
    
    #Default iteration has came to end of array
    index = -1

    #Below makes range from 1 to len(arr)-1 in order to check 3 values at once
    for j in range(1, len(arr) - 1, 1):
        #First condition is for increasing sequence and second is for decreasing
        #Backslash below is treated as extension of line
        if arr[j-1] < arr[j] and arr[j] > arr[j+1] or \
            arr[j-1] > arr[j] and arr[j] < arr[j+1]:
            #Below assigns index where sequence stopped increasing or decreasing  
            index = j
    
    #If none of cases had place, index is -1 because it means whole array was traversed
    return index
