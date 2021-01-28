'''
Find Sucessor from AlgoExpert.io
January 2021 Jakub Kazimierski
'''

class BinaryTree:
    '''
    Write a function that takes in a Binary Tree
    (where nodes have an additional pointer to their
    parent node) as well as a node contained in that tree
    and returns the given node's successor.

    A node's successor is the next node to be visited 
    (immediately after the given node) when traversing 
    it's tree using the in-order tree-traversal technique. 
    A node has no successor if it's the last node to be visited
    in the in-order traversal.

    If a node has no successor, your function should return None/null.

    Each BinaryTree node has an integer value, a parent node,
    a left child node, and a right chid node. Children nodes can either
    be BinaryTree nodes themselves or None/null.
    '''
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    '''
    Use inorderTraverse logic

    traverse(left)
    vist
    traverse(right)

    Time O(h) where h is level of the tree | space O(1)
    '''

    if node.right is not None:
        return getLeftmostChild(node.right)

    elif node.parent is not None and node.parent.left == node:
        return node.parent

    elif node.parent is not None and node.parent.right == node:
        return findMostRightParent(node)

    else:
        return None


def getLeftmostChild(node):
    '''
    Time O(h) | space O(1)
    Returns leftmost child of subtree.
    '''
    while node.left is not None:
        node = node.left
    return node    


def findMostRightParent(node):
    '''
    Find first right parent.
    O(h) time | O(1) space
    ''' 
    while node.parent is not None and node == node.parent.right:
        node = node.parent
    return node.parent
