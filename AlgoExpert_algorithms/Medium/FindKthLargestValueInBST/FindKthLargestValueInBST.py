'''
Find Kth Largest Value in BST from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

# This is an input class. Do not edit.
class BST:
    '''
    Write a function that takes in a Binary Search Tree
    (BST) and a positive integer k, and returns the kth
    largest integer contained in the BST.

    You can assume that there will only be integer values
    in the BST and that k is less than or equal to the number
    of nodes in the tree.

    Also, for the purpose of this question, duplicate integers
    will be treated as distinct values. In other words, the second
    largest value in a BST containing values {5, 7, 7} will be 7 not 5.

    Each BST node has an inteher value, aleft child node, and a right
    child node. A node is said to be a valid BST node if and only if
    it satisfies the BST property: its value is strictly greater than 
    the values of every node to its left; its value is less than or equal
    to the values of every node to its right; and its children nodes are either
    valid BST nodes themselves or None/null.
    '''

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBST(tree, k):
    '''
    Returns K-th largest value in BST
    Time O(n) | Space O(n)
    '''
    
    def traverse(node, values):
        if node is None:
            return
        traverse(node.left, values)
        values.append(node.value)
        traverse(node.right, values)

    # O(n) space where n is num of nodes
    sorted_values = []

    # O(n) time
    traverse(tree, sorted_values)
    nodes_num = len(sorted_values)

    return sorted_values[nodes_num - k]






