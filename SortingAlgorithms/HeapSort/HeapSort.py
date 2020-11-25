def HeapSort(array):
    '''
    HeapSort algorithm.
    
    Complexity of building a cheap is O(n)
    (at each level, for each element we do at most 2 comparitions
    if we sum it up it is in O(n)) 
    
    Complexity of heapsort is sum for 2<= i <= n  2*log(i) (when last element remaining 
    there is no comparitions so i starts from 2)
    (2 comparitions at each level to heapify array after extraction)
    This sum is in O(nlogn)
    '''

    try:
                
        numberOfElements = len(array)
        
        # map indexes of array into binary complete tree
        # leftChild = 2*p + 1
        # rightChild = 2*p + 2
        # If we have n indexes in array last right child has index n
        # so 2*p + 2 = n -> p = n/2 - 1 as it's parent, so we can start mapping parents indexes
        # from this value, it is not necessery to starts from n-1, child indexes are mapped in Heapify method 
        for index in range((numberOfElements-1)//2 - 1, -1, -1):
            Heapify(array, numberOfElements, index)
        
        # One by one extract max elements which are at the end of array
        for numOfElements_In_Heap in range(numberOfElements-1, 0, -1):
            # in each iteration heap is smaller and the smallest element becomes root
            array[numOfElements_In_Heap], array[0] = array[0], array[numOfElements_In_Heap]
            # heap has to be repaired after extraction
            Heapify(array, numOfElements_In_Heap, 0)

        return array

    except(AttributeError, TypeError, ValueError):
        return -1


# heapify creates proper complete binary tree with sorted elements
# parent is greater than both children nodes
def Heapify(array, numberOfElements, root_Index):
    
    largestElem_Index = root_Index  # Initialize largest as root
    leftChild_Index = 2 * root_Index + 1     
    rightChild_Index = 2 * root_Index + 2    
    
    # See if left child of root exists and is greater than root
    if leftChild_Index < numberOfElements and array[largestElem_Index] < array[leftChild_Index]:
        largestElem_Index = leftChild_Index
    
    # See if right child of root exists and is greater than root
    if rightChild_Index < numberOfElements and array[largestElem_Index] < array[rightChild_Index]:
        largestElem_Index = rightChild_Index
    
    # Change root, if it is not largestElem
    if largestElem_Index != root_Index:
        array[root_Index], array[largestElem_Index] = array[largestElem_Index], array[root_Index]  # swap
    
        # recurency call to create Maxheap
        Heapify(array, numberOfElements, largestElem_Index)
    
def _input():
    
    exampleInput = [3,4,2,5,1]

    return exampleInput

def _input():
    
    exampleOutput = [1,2,3,4,5]

    return exampleOutput

