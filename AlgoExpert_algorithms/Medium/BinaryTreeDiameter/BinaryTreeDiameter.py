'''
Binary Tree Diameter from AlgoExpert.io
January 2021 Jakub Kazimierski
'''

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    '''
    Write a function that takes in a Binary Tree
    and returns its diameter. The diameter of a
    binary tree is defined as the length of its
    longest path, even if that path doesn't
    pass through the root of the tree.

    A path is a collection of connected nodes in a tree,
    where no node is connected to more than two other
    nodes. The length of a path is the number of edges
    between the path's first node and it's last node.

    Each BinaryTree node has an integer value, a left child node,
    and a right child node. Children nodes can either be BinaryTree
    nodes themselves or None.
    '''

    return getTreeParams(tree).diameter


def getTreeParams(tree):
    '''
    Time O(n) | space O(n)
    Returns max diameter
    '''
    if tree is None:
        return TreeParams(0,0)

    # Traverse left and right subtree
    leftTreeParams = getTreeParams(tree.left)
    rightTreeParams = getTreeParams(tree.right)

    # at end of recurson returns summed left and right height throught the root
    longestPathThroughRoot = leftTreeParams.height + rightTreeParams.height
    maxDiameter = max(leftTreeParams.diameter, rightTreeParams.diameter)

    # if diameter is greater in next step assign it as new val
    currentDiameter = max(longestPathThroughRoot, maxDiameter)
    # assign new height in each step
    currentHeight = 1 + max(leftTreeParams.height, rightTreeParams.height)

    # return current parameters
    return TreeParams(currentDiameter, currentHeight)


class TreeParams:
    '''
    Contains parameters of node at
    some level of the tree.
    '''
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height
                 

