'''
Find Closest Value in BST from AlgoExpert.com
January 2021 Jakub Kazimierski
'''

import sys

def findClosestValueInBst(tree, target):
    '''
    Write a function that takes in a 
    Binary Search Tree (BST) and a target integer
    value and returns the closest value to that 
    target value contained in the BST.
    
    You can assume that there will only be
    one closest value.
    
    Each BST node has an integer value, a left 
    child node, and a right child node.
    A node is said to be a valid BST node if
    and only if it satisfies the BST property:
    Its value is strictly greater than the values of 
    every node to its left; it's value is less
    than or equal to the values of every node to 
    its right; and it's children nodes are either
    valid BST nodes themselves or None/null. 
    '''

    def traverse_tree(tree, target, closest):
        '''
        Avg case complexity is O(log(n)) | Space O(log(n))
        Worst case complexity is O(n) | Space O(n)
        '''
        if tree is None:
            return closest

        if abs(tree.value - target) < abs(closest - target):
            closest = tree.value

        if tree.value < target:
            return traverse_tree(tree.right, target, closest)
        elif tree.value > target:
            return traverse_tree(tree.left, target, closest)
        else:
            return closest        

    return traverse_tree(tree, target, float('inf'))
        


# region Binary tree region
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        '''
        Avg Time O(log(n)) | space O(1)
        worst time O(n) | space O(1)
        '''

        current_node = self

        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current_node = current_node.left    
            if value >= current_node.value:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    current_node = current_node.right 
# endregion    

def setUp():
    '''
    Returns BST tree for tests
    '''
    root = BST(10)
    root.insert(5)
    root.insert(15)
    root.insert(2)
    root.insert(5)
    root.insert(1)
    root.insert(22)
    root.insert(13)
    root.insert(14)

    return root    