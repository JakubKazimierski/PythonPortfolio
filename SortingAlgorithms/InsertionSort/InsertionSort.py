def InsertionSort(array):
    '''
    InsertionSort algorithm.
    '''
    try:
        # O(n^2)
        for i in range(0, len(array)-1):
            # compare array[i] and array[i+1]
            if array[i]>array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                # if array[i+1] was less, compare it tother elements 
                # which was before array[i]
                for j in range(i, 0, -1):
                    if array[j-1] > array[j]:    
                        array[j], array[j-1] = array[j-1], array[j]

        return array    
    except (AttributeError, TypeError):
        return -1    

def _input():
    
    exampleInput = [3,4,2,5,1]

    return exampleInput

def _input():
    
    exampleOutput = [1,2,3,4,5]

    return exampleOutput

