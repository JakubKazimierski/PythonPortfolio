'''
Changing Sequence from Coderbyte
November 2020 Jakub Kazimierski
'''


def ChangingSequence(arr):
    '''
    take the array of numbers stored in arr 
    and return the index at which the numbers 
    stop increasing and begin decreasing or 
    stop decreasing and begin increasing

    If there is only a single sequence in the array 
    then your program should return -1

    The array will contain at least 3 numbers and it 
    may contains only a single sequence, increasing or decreasing
    '''

    #assert type of input and condition that input is not empty

    if len(arr) > 0:
        for i in arr:
            if type(i) != int:
                return "Wrong Input Type"
    else:
        return "Input is empty"             
    

    #sequences can be increasing or decreasing
    if arr[0] < arr[1]:
        #increasing
        i = 0

        #while sequence is increasing and i is in indexes of arr range
        #i+1 < len(arr) must be first condition to asser index error
        while i+1 < len(arr) and arr[i] < arr[i+1]:
            #increase index
            i += 1

        #LAST INDEX IN ARR IS len(arr)-1 not len(arr)!!!
        #if numbers was not increasing in whole arr retun index i
        #above mean if after loop ends i is different than last index
        #it will be index when sequence stop
        if i != len(arr)-1:
            return i
        else:
            #else sequence was still increasing
            return -1    
        
    else:
        #decreasing
        
        i = 0

        #while sequence is decreasing and i is in indexes of arr range
        #i+1 < len(arr) must be first condition to asser index error
        while i+1 < len(arr) and arr[i] > arr[i+1]:
            #increase index
            i += 1

        #LAST INDEX IN ARR IS len(arr)-1 not len(arr)!!!
        #if numbers was not decreasing in whole arr retun index i
        #above mean if after loop ends i is different than last index
        #it will be index when sequence stop
        if i != len(arr)-1:
            return i
        else:
            #else sequence was still decreasing
            return -1    
        

