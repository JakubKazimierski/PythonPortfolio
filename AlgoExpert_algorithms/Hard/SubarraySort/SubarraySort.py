'''
Subarray Sort from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def subarraySort(array):
    '''
    Write a function that takes in an array
    of at least two integers and that returns an
    array of the starting and ending indicies
    of the smallest subarray in the input array
    that needs to be sorted in place in order
    for the entire input array to be sorted 
    (in ascending order).

    If the input array is already sorted, the 
    function should return [-1, 1].
    '''

    def isOutOfRange(idx, num, array):
        '''
        Time O(1) | space O(1)
        Defines if number in array 
        is out of ascending order.
        '''
        if idx == 0:
            return array[idx] > array[idx+1]
        if idx == len(array)-1:
            return array[idx] < array[idx-1]
        return array[idx] > array[idx+1] or array[idx] < array[idx-1]

    minOutOfOrder = float('inf')
    maxOutOfOrder = float('-inf')

    # O(n) time | O(1) space
    for idx in range(len(array)):
        num = array[idx]
        if isOutOfRange(idx, num, array):
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)

    leftMinIdx = 0
    rightMaxIdx = len(array)-1

    if minOutOfOrder == float('inf') and maxOutOfOrder == float('-inf'):
        return [-1, -1]

    # worst time O(n) | space O(1)
    while array[leftMinIdx] <= minOutOfOrder:
        leftMinIdx += 1
    while array[rightMaxIdx] >= maxOutOfOrder:
        rightMaxIdx -= 1

    return [leftMinIdx, rightMaxIdx]       


