'''
Array Addition I from Codersbyte
November 2020 Jakub Kazimierski
'''

from itertools import chain, combinations

def all_subsets(arr):
    '''
    Returns chain of all possible combinations
    of elements in given at input array
    ''' 
  
    # chain() -It is a function that takes a series of iterables and returns one iterable.
        
    # map() -function returns a map object(which is an iterator) of the results after applying
    # the given function to each item of a given iterable
        
    # combinations()-Given an array of size n, generate and print all possible combinations of r elements in array.
    # where r is length of combination
    

    return chain(*map(lambda x: combinations(arr, x), range(1, len(arr)+1)))


def ArrayAdditionI(arr):
    '''
    Have the function ArrayAdditionI(arr) 
    take the array of numbers stored in arr 
    and return the string true if any combination 
    of numbers in the array (excluding the largest number) 
    can be added up to equal the largest number in the array, 
    otherwise return the string false. 
    For example: if arr contains [4, 6, 23, 10, 1, 3] 
    the output should return true because 4 + 6 + 10 + 3 = 23. 
    The array will not be empty, will not contain all the same elements, 
    and may contain negative numbers.
    '''
    try:
        maxElement = max(arr)

        arr.remove(max(arr))

        for subset in all_subsets(arr):
            if sum(subset) == maxElement:
                return "true"

        # If sum of any combination was not equal
        # to max element return false         
        return 'false'

        #region Commentary
        #Algorithm is good because it checks
        #all possible combinations
        #but complexity in this case is O(2^n)
        #where n is number of all elements in given arrBuf
        #so it is not fast
        #endregion
        
    except TypeError:
        return -1

def _input():

    sampleList = [4, 6, 23, 10, 1, 3]

    return sampleList

def _output():

    sampleString = "true"

    return sampleString
