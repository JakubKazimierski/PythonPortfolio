'''
Same BSTs from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def sameBSTs(arrayOne, arrayTwo):
    '''
    An array of integers is said to represent
    the BinarySearch Tree (BST) obtained by inserting
    each integer in the array, from left to right,
    into the BST.

    Write a function that takes in two arrays of integers
    and determines whether these arrays represent the same 
    BST. Note that you're not allowed to construct any BSTs 
    in your code.

    A BST is a Biinary Tree that consist only of BST nodes.
    A node is said to be a valid BST node if and only if
    it satisfies the BST property: its value is strictly
    greater than the values of every node to its left; its value
    is less than or equal to the values of every node to its right;
    and its children nodes are either valid BST nodes themselves 
    or None/null.
    '''


    '''
    Time O(n) | space O(n) (stack calls)
    returns true if input arrays represents
    the same BSTs.
    '''
    if len(arrayOne) != len(arrayTwo):
        return  False

    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    # check root value
    if arrayOne[0] != arrayTwo[0]:
        return False  

    # recurency call for smaller than root and 
    # greater than root values, checks occurence
    # step by step in each array

    leftOne = getSmaller(arrayOne)
    leftTwo = getSmaller(arrayTwo)
    rightOne = getBiggerOrEqual(arrayOne)
    rightTwo = getBiggerOrEqual(arrayTwo)

    return sameBSTs(leftOne, leftTwo) and sameBSTs(rightOne, rightTwo)

def getSmaller(arr):
    '''
    Time O(n) | space O(n)
    returns smaller values
    than first elem in array.
    '''
    smaller = []
    for idx in range(1, len(arr)):
        if arr[idx] < arr[0]:
            smaller.append(arr[idx])
    return smaller        

def getBiggerOrEqual(arr):
    '''
    Time O(n) | space O(n)
    returns bigger or equal values
    than first elem in array.
    '''
    biggerOrEqual = []
    for idx in range(1, len(arr)):
        if arr[idx] >= arr[0]:
            biggerOrEqual.append(arr[idx])
    return biggerOrEqual        


