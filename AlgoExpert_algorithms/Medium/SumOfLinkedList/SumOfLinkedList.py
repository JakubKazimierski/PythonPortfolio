'''
Sum of LinkedList from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

# This is an input class. Do not edit.
class LinkedList:
    '''
    You're given two Linked Lists of potentially unequal length. 
    Each Linked List represents a non-negative integer, where 
    each node in the Linked List is a digit of that integer, 
    and the first node in each Linked List always represents 
    the least significant digit of the integer. Write a function that
    returns the head of a new Linked List that represents the sum of 
    the integers represented by the two input Linked Lists.

    Each LinkedList node has an integer value as well as a next
    node pointing to the next node in the list or to None/null
    if it's the tail of the list. The value of each LinkedList
    node is always in the range of 0-9.

    Note your function must create and return a new LinkedList, and you're
    not allowed to modify either of the input LinkedLists.
    '''
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    '''
    Returns new Linked List which is representation
    of sum of two input lists.
    
    Time O(max(n, m)) | Space O(max(n, m))
    Where n, m are lengths of Linked Lists.
    '''

    nodeOne = linkedListOne
    nodeTwo = linkedListTwo

    numOneReversed = ""
    numTwoReversed = ""

    nodeOneContinue = True
    nodeTwoContinue = True
    
    # takes O(max(n,m) time and space
    while nodeOneContinue or nodeTwoContinue:
        
        if nodeOneContinue:
            numOneReversed += str(nodeOne.value)
            nodeOne = nodeOne.next

            if nodeOne is None:
                nodeOneContinue = False

        if nodeTwoContinue:    
            numTwoReversed += str(nodeTwo.value)    
            nodeTwo = nodeTwo.next

            if nodeTwo is None:
                nodeTwoContinue = False



    # below assigns correct string repr of int value
    numOne = numOneReversed[::-1]
    numTwo = numTwoReversed[::-1]

    summedStr = str(int(numOne) + int(numTwo))
    outputNum = summedStr[::-1]

    outList = LinkedList(int(outputNum[0]))

    node = outList
    for strDigit in outputNum[1:]:
        node.next = LinkedList(int(strDigit))
        node = node.next        

    return outList


def checkValues(list_I, list_II):
    '''
    Time O(max(n, m)) | space O(1)
    where n, m are lengths of input lists.
    Check if two lists, has the same values.
    If so returns True else False
    '''

    while list_I is not None or list_II is not None:
        if list_I.value != list_II.value:
            return False

        list_I = list_I.next
        list_II = list_II.next

    return True        