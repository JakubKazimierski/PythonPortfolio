'''
Remove Kth Node From End from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def returnValues(head):
    '''
    Method for tests, returns
    values of linked list, starts fro head.
    Time O(n) | space O(n)
    '''
    array = []
    while head is not None:
        array.append(head.value)
        head = head.next
    return array    

def removeKthNodeFromEnd(head, k):
    '''
    Write a function that takes in the head
    of a Singly Linked List and an integer k
    and removes the kth node from the end of 
    the list.

    The removal should be done in place, meaning
    that the original data structure should be mutated
    (no new structure should be created).

    Furthermore, the input head of the linked list
    should remain the head of the linked list after 
    the removal is done, even if the head is the node
    that's supposed to be removed. In other words, if the
    head is the node that's supposed to be removed, your
    function should simply mutate its value and next pointer.

    Note that your function doesn't need to return anything.

    You can assume that the input Linked List will always have
    at least two nodes and, more specifically, at least k nodes.

    Each LinkedList node has an integer value as well as a next node
    pointing to the next node in the list or to None/null if it's 
    the tail of the list.
    '''

    # whole algorithm time O(n) | O(1) space

    temp_node_len = temp_node_remove = head
    length = 0

    # O(n) time | O(1) space
    while temp_node_len is not None:
        length += 1
        temp_node_len = temp_node_len.next

    position = length - k

    # if head has to be removed
    if position == 0:
        new_head = head.next
        head.next = head.next.next
        head.value = new_head.value
    else:
        count_pos = 0
        # time O(n) worst case | space O(1)
        # stops at node before node at given position
        while count_pos < position-1:
            count_pos += 1
            head = head.next
        # remove bindings of node at given position    
        head.next = head.next.next




