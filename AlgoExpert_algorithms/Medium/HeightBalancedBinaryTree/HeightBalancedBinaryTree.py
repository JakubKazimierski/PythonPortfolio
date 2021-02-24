'''
Height Balanced Binary Tree from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

# This is an input class. Do not edit.
class BinaryTree:
    '''
    You're given the root node
    of a BinaryTree. Write a function 
    that returns true if this Binary Tree
    is height balanced and false if it isn't.

    A binary Tree is height balanced if for 
    each node in the tree, the difference between the height
    of its left subtree and the height of its right
    subtree is at most 1.

    Each BinaryTree node has an integer value, a left child
    node, and a right child node. Children nodes can either
    be BinaryTree nodes themselves or None/null.
    '''
    
    
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced


class TreeInfo:
    '''
    Class contains info about
    tree height and balance.
    '''
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height


# Time O(n) where n is num of nodes
# Space O(h) where h is height of tree
def getTreeInfo(node):
    if node == None:
        return TreeInfo(True, -1)

    leftSubtreeInfo = getTreeInfo(node.left)
    rightSubtreeInfo = getTreeInfo(node.right)

    isBalanced = leftSubtreeInfo.isBalanced and rightSubtreeInfo.isBalanced\
        and abs(leftSubtreeInfo.height - rightSubtreeInfo.height) <= 1
    
    # if node is None height will be 0
    height = max(leftSubtreeInfo.height, rightSubtreeInfo.height) + 1
    return TreeInfo(isBalanced, height)   