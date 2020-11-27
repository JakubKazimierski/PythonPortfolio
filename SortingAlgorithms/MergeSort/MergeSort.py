def MergeSort(array):
    '''
    MergeSort algorithm.
    
    If array contains n elements, in each divison  we get two subarrays of lenghts: (n/2), (n/4), (n/8) ... (n/2^i)
    
    Till we reach subarrays of lenght 1 so:

    0 <= i < k
    
    where k = log_2(n)

    Because: n = 2^k


    At each division level we have at most (n/2^i - 1) comparitions to do.
    For 0 <= i < k

    So whole numbers of comparitions, we have to take at most will be:

    Sum in range from 0 to k-1, because if array is length of 1, we don't do any comparitions
    
    So total number of operations is Sum:  2^i*(n/2^i - 1) for i in range 0 <= i < k: which is in O(nlogn)

    '''
    try:
        # if array has length 1, there is nothing to sort
        if len(array)>1:
            
            middleIndex = round(len(array)/2)

            leftArray = array[:middleIndex]
            rightArray = array[middleIndex:]
            
            # Below returns sorted subarrays
            MergeSort(leftArray)
            MergeSort(rightArray)

            # below merge sorted subarrays into array in order
            indexLeftArr = indexRightArr = indexArray = 0
        
            while indexLeftArr < len(leftArray) and indexRightArr < len(rightArray):

                # assign elements to main array in order, from both subarrays
                if leftArray[indexLeftArr] < rightArray[indexRightArr]:
                    
                    array[indexArray] = leftArray[indexLeftArr]
                    indexLeftArr += 1
                
                else:
                    array[indexArray] = rightArray[indexRightArr]
                    indexRightArr += 1
                
                indexArray += 1
            # when loop ends half of array is already sorted

            # below cheks which element from subarrays was not yet inserted into main array
            # and puts those elements at remaining indexes
            # one of subarrays has all elements inserted at this moment, so there won't be mistake
            while indexLeftArr < len(leftArray):
                array[indexArray] = leftArray[indexLeftArr]
                indexLeftArr += 1
                indexArray += 1
    
            while indexRightArr < len(rightArray):
                array[indexArray] = rightArray[indexRightArr]
                indexRightArr += 1
                indexArray += 1
                    
            return array
        else:
            return array    

    except (AttributeError, TypeError, ValueError):
        return -1    

def _input():
    
    exampleInput = [3,4,2,5,1]

    return exampleInput

def _input():
    
    exampleOutput = [1,2,3,4,5]

    return exampleOutput

