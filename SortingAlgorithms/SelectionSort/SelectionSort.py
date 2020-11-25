def SelectionSort(array):
    '''
    SelectionSort algorithm.

    Takes default min as first element of main loop, and compare it with others.
    If any element is smaller, swap them. When inner loop ends
    First element is minimum of array.

    Repeat process for next index in array, this will be second min value,
    and later third, fourth, ...

    Repeat whole process till array ends.
    '''
    try:
        
        # Worst Case complexity is O(n^2) for reverse sorted array
        # best case is O(n^2) for sorted array
        
        # last element is compared in second loop
        for i in range(0, len(array)-1):

            for j in range(i+1, len(array)):
            
                # swap amount is less than with bubblesort
                if array[j] < array[i]:
                
                    array[i], array[j] = array[j], array[i]
        


        return array

    except (AttributeError, TypeError, ValueError):
        return -1

def _input():

    exampleInput = [3,4,2,5,1]

    return exampleInput
def _output():

    exampleOutput = [1,2,3,4,5]

    return exampleOutput    