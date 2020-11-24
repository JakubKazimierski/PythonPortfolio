def BubbleSort(array):
    '''
    BubbleSort algorithm.
    '''
    try:
        # if array is not already sorted change to False
        isSorted = True

        #O(n^2)
        for i in range(0, len(array)):
            # biggest element in each iteration get to highest possible place
            # so each time we can iterate one place less
            for j in range(0, len(array)-i-1): 
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    isSorted = False

            if isSorted == True:
                return "Array is already sorted"

        return array

            
    except (AttributeError, TypeError):
        return -1

def _input():

    exampleInput = [3,4,5,1,2]

    return exampleInput

def _output():

    exampleOutput = [1,2,3,4,5]

    return exampleOutput    