'''
Insertion Sort from AlgoExpert.com
January 2021 Jakub Kazimierski
'''

def insertionSort(array):
    '''
    Write a function that takes in an array
    of integers and returns a sorted version
    of that array. Use the insertion Sort algorithm
    to sort the array.
    '''

    if all(array[index] <= array[index+1] for index in range(len(array)-1)):
        return array

    # Avg time O(n^2), best case O(n) | space O(1)
    for elem_id in range(1, len(array)):
        # at each iteration subarray till elem_id is sorted        
        for elem_id_II in range(elem_id, 0, -1):
            if array[elem_id_II] < array[elem_id_II - 1]:
                array[elem_id_II], array[elem_id_II - 1] = array[elem_id_II - 1], array[elem_id_II]
            else:
                break
    return array
