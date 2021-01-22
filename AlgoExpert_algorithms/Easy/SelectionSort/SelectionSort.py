'''
Selection Sort from AlgoExpert.com
January 2021 Jakub Kazimierski
'''

def selectionSort(array):
    '''
    Write a function that takes in an array
    of integers and returns a sorted version
    of that array. Use the Selection Sort algorithm
    to sort the array.
    '''
    
    if all(array[index] <= array[index+1] for index in range(len(array)-1)):
        return array

    # Avg time O(n^2), best time O(n) | space O(1)
    for elem_id in range(len(array)-1):
        # at each iteration current lowest elem is choosen
        for elem_id_II in range(elem_id + 1, len(array)):
            if array[elem_id_II] < array[elem_id]:
                array[elem_id], array[elem_id_II] = array[elem_id_II], array[elem_id]

    return array