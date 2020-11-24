def InsertionSort(array):
    '''
    InsertionSort algorithm.
    '''
    try:
        for i in range(0, len(array)-1):
            
            if array[i]>array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]

                for j in range(i, 0, -1):
                    if array[j-1] > array[j]:    
                        array[j], array[j-1] = array[j-1], array[j]

        return array    
    except (AttributeError, TypeError):
        return -1    