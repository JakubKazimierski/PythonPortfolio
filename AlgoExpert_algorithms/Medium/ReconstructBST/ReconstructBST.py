'''
Reconstruct BST from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

# This is an input class. Do not edit.
class BST:
    '''
    The pre-order traversal of a Binary Tree is a traversal
    technique that starts at the tree's root node and visits
    nodes in the following order:

        1. Current node
        2. Left subtree
        3. Right subtree
    
    Given a non-empty array of integers representing the pre-order
    traversal of a Binary Search Tree (BST), write a function that 
    creates the relevant BST and returns its root node.

    The input array will contain the values of BST nodes in the order
    in which these nodes would be visited with a pre-order traversal.

    Each BST node has an integer value, a left child node, and a right
    child node. A node is said to be a valid BST node if and only if it satisfies
    the BST property: its value is strictly greater than the values of every
    node to its left. its value is less than or equal to the values of every
    node to its right; and its children nodes are either valid BST nodes
    themselves or None/null.    
    '''

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBST(preOrderTraversalValues):
    '''
    Reconstructs BST from given input array
    Takes O(n*h) time | O(n) space where
    n is num of nodes in tree and h is height of tree.
    '''

    def insert(node, val):
        '''
        Takes O(h) Time | O(1) space
        where h is height of tree
        Insert value in proper place
        in BST.
        '''
        if val < node.value:
            if node.left is None:
                node.left = BST(val)
            else:    
                insert(node.left, val)
        else:
            if node.right is None:
                node.right = BST(val)
            else:
                insert(node.right, val)    


    root_val = preOrderTraversalValues.pop(0)
    root = BST(root_val)

    # below takes O(n*h) time | O(n) space where
    # n is num of nodes in tree and h is height of tree
    while len(preOrderTraversalValues) > 0:
        node = root
        val = preOrderTraversalValues.pop(0)
        insert(node, val)

    return root

def traversePreOrder(tree_node, arr):
    '''
    Takes O(n) time | O(n) space
    where n is num of nodes in tree
    Returns preorder array of values.
    '''
    
    if tree_node is None:
        return 
    arr.append(tree_node.value)
    traversePreOrder(tree_node.left, arr)
    traversePreOrder(tree_node.right, arr)

    