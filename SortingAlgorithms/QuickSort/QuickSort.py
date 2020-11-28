def QuickSort(arr):
    '''
    Quick Sort Algorithm implementation.

    Worst case complexity is if pivot is the biggest
    or the smallest element in array, then tree of partition
    is not balanced. Then number of operations will be
    sum in range 1<= i < n of i this is equal (((n-1)+1)/2)*(n-1)
    so complexity is O(n^2).

    Best case scenario is alike to merge sort when array is halved
    while partiotion process has place so then complexity is O(nlogn) 
    
    '''
    
    try:
        
        # for array of lenght 1, there is nothing to sort
        if len(arr) < 2:
            return arr
        
        pivot_position = 0 

        for i in range(1, len(arr)): 
    
            # for elements less than pivot value
            if arr[i] <= arr[0]:
                # pivot position increase 
                pivot_position += 1
                # elements less than pivot go at left site 
                arr[i], arr[pivot_position] = arr[pivot_position], arr[i]

            # pivot position does not increase if element is greater than pivot value        
            # so elements greater than pivot stay at right site of it by swaping 
            # with element less than it, it is important to remeber that pivot
            # is not actually put between elements, it is compared with them

        # when process ends assign to pivot position pivot value, 
        # element at pivot position is less or equal than it so swap them
        arr[0], arr[pivot_position] = arr[pivot_position], arr[0]
        
        left = QuickSort(arr[:pivot_position]) #Sorts the elements to the left of pivot
        right = QuickSort(arr[pivot_position+1:]) #sorts the elements to the right of pivot

        arr = left + [arr[pivot_position]] + right #Merging everything together
        
        return arr

    except (AttributeError, TypeError, ValueError):
        return -1    

def _input():
    
    exampleInput = [3,4,2,5,1]

    return exampleInput

def _input():
    
    exampleOutput = [1,2,3,4,5]

    return exampleOutput

