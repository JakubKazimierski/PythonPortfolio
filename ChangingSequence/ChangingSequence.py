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
    

    #Sequences can be increasing or decreasing
    if arr[0] < arr[1]:
        #Increasing

        #Till line below i has value of last elemnt in array
        #Because assertion loop above (it is worth to remember)
        i = 0

        #While sequence is increasing and i is in indexes of arr range
        #i < len(arr)-1 must be first condition to asser index error
        while i < len(arr)-1 and arr[i] < arr[i+1]:
            #increase index
            i += 1

        #region Commentary
        #LAST INDEX IN ARR IS len(arr)-1 not len(arr)!!!
        #if numbers was not increasing in whole arr retun index i
        #above mean if loop ends and i is different than last index
        #it will be index when sequence stop
        #endregion

        if i != len(arr)-1:
            return i
        else:
            #else sequence was still increasing
            return -1    
        
    else:
        #Decreasing        
        i = 0

        #While sequence is decreasing and i is in indexes of arr range
        #i < len(arr)-1 must be first condition to asser index error
        while i < len(arr)-1 and arr[i] > arr[i+1]:
            #Increase index
            i += 1

      if i != len(arr)-1:
            return i
        else:
            #Else sequence was still decreasing
            return -1    
        

