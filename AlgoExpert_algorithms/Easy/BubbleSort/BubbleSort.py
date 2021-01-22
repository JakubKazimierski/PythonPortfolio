'''
Bubble Sort from AlgoExpert.com
January 2021 Jakub Kazimierski
'''

def bubbleSort(array):
    '''
    Write a function that takes in an array
    of integers and returns a sorted version
    of that array. Use Bubble Sort algorithm
    to sort the array.
    '''

    # Avg time O(n^2), Best O(n) -> sorted array, space o(1)

    if all(array[index] <= array[index+1] for index in range(len(array)-1)):
        return array

    for elem_id in range(len(array)):
        # at each iteration algorithm finds current minimum
        for elem_id_II in range(elem_id + 1, len(array)):
            if array[elem_id_II] < array[elem_id]:
                array[elem_id], array[elem_id_II] = array[elem_id_II], array[elem_id]

    return array