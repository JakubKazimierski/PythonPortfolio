'''
Linked List Construction from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    '''
    Write a DoublyLinkedList class that has a head
    and a tail, both of which point to either a linked list
    Node or None/null. the class should support:
    
        -Setting the head and tail of the linked list.
        -Inserting nodes before and after other nodes
            as well as at given position (the position 
            of te head node is 1)
        -Removing given nodes and removing nodes with given
            values.
        -Searching for nodes with given values.

    Note that the stHead, setTail, insertBefore, insertAfter,
    insertAtPosition, and remove methods all takes in actual Nodes
    as input parameters-not integers (except for insertAtPosition),
    which also takes in an integer representing the position); this
    means that you don't need to create any new Nodes in these methods.
    The input nodes can be either stand-alone nodes or nodes that are already
    in the linked list. If they're nodes that are already in the linked list
    the methods will effectively be moving the nodes within the linked list.
    You won't be told if the input nodes are already in the linked list, so 
    your code will have to defensively handle this scenario.

    Each Node has an integer value as well as a prev node and a next node, both
    of which can point to either another node or None/null.
    '''
    
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        pass

    def setTail(self, node):
        # Write your code here.
        pass

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        pass

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        pass

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        pass

    def removeNodesWithValue(self, value):
        # Write your code here.
        pass

    def remove(self, node):
        # Write your code here.
        pass

    def containsNodeWithValue(self, value):
        # Write your code here.
        pass
