'''
Remove Duplicates From Linked List from AlgoExpert.io
February 2021 Jakub Kazimierski
'''
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    '''
    You're given the head of a SinglyLinkedList whose
    nodes are in sorted order with respect to their
    values. Write a function that returns a modified
    version of the LinkedList that doesn't contain
    any nodes with duplicate values. The LinkedList
    should be modified in place (i.e, you shouldn't 
    create a brand new list), and the modified LinkedList
    should still have its nodes sorted with respect to their
    values.

    Each LinkedList node has an integer value as well as a
    next node pointing to the next node in the list or
    to None/null if it's the tail of the list.
    '''

    # time O(n) where n-nodes in l list | space O(1)
    if linkedList.next != None:
        # as long as values repeat, loop disconnects them
        while linkedList.next.value == linkedList.value:
            if linkedList.next.next != None:
                linkedList.next = linkedList.next.next
            else:
                linkedList.next = None
                return linkedList    
        removeDuplicatesFromLinkedList(linkedList.next)

    return linkedList

def compare_values(list_1, list_2):
    '''
    Method for tests.
    Time O(n) | space O(1)
    '''
    while list_1.next != None and list_2.next != None:
        val_1, val_2 = list_1.value, list_2.value
        if val_1 != val_2:
            return False
        list_1, list_2 = list_1.next, list_2.next 

    return True    