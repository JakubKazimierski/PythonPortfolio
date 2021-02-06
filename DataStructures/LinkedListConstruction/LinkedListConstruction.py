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
        '''
        Time O(1) | space O(1)
        Sets new head of list.
        '''
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head, node)    


    def setTail(self, node):
        '''
        Time O(1) | space O(1)
        Sets new head of list.
        '''
        if self.tail is None:
            self.setHead(node)
        else:
            self.insertAfter(self.tail, node)    

    def insertBefore(self, node, nodeToInsert):
        '''
        O(1) Time | O(1) space
        Insert given node to insert before node in list.
        '''
        # of there is just one node in list
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        # in case if node to insert exist somewhere in list
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert        


    def insertAfter(self, node, nodeToInsert):
        '''
        O(1) Time | O(1) space
        Insert given node to insert after node in list.
        '''
        # of there is just one node in list
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        # in case if node to insert exist somewhere in list
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert        

    def insertAtPosition(self, position, nodeToInsert):
        '''
        Time O(position) | space O(1)
        Inserts given node at given position.
        '''
        if position == 1:
            self.setHead(nodeToInsert)
        else:
            node = self.head
            currentPosition = 1
            while node is not None and currentPosition != position:
                currentPosition += 1
                node = node.next
            if node is  None:
                self.setTail(nodeToInsert)
            else:
                self.insertBefore(node, nodeToInsert)            

    def removeNodesWithValue(self, value):
        '''
        Time O(n) | space O(1)
        Finds if node with given
        value exist, and if it is, 
        then removes it.
        '''
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def remove(self, node):
        '''
        Time O(1) | space O(1)
        Removes given node.
        '''
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.remove_bindings(node)         

    def containsNodeWithValue(self, value):
        '''
        Time O(n) | space O(1)
        Returns node if it is in list, else None.
        '''
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return True if node is not None else False    

    def remove_bindings(self, node):
        '''
        Time O(1) | space O(1)
        Removes bindings of adjacent nodes,
        of node to be removed.
        '''
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None    
