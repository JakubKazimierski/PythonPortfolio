'''
Invert Binary Tree from AlgoExpert.io
January 2021 Jakub Kazimierski
'''

'''
Write a function that takes in a Binary Tree 
and inverts it. In other words, the function should swap
every left node in the tree for its corresponding
right node.

Each Binary Tree node has an integer value,
a left child node, and a right child node.
Children nodes can either be BinaryTree
nodes themselves or None/null.
'''

def invertBinaryTree(tree):
    '''
    Time O(n) | space O(d) where d is depth of Btree
    Starts swapping nodes from lowest left level to the right side. 
    '''
    # first traverse max at left
    if tree.left is not None:
        invertBinaryTree(tree.left)
    # next to the right    
    if tree.right is not None:
        invertBinaryTree(tree.right)
    # if node has no children return, else swap them    
    if tree.right is not None or  tree.left is not None:
        tree.left, tree.right = tree.right, tree.left
    return tree

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preOrderTraverse(tree, array):
    '''
    Time O(n) | space O(n)
    returns preorder array 
    for tests.
    '''
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)

    return array