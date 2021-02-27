'''
Max Path Sum In Binary Tree from ALgoExpert.io
February 2021 Jakub Kazimierski
'''


class BinaryTree:
    '''
    Class for building tree.
    
    Write a function that takes in a BinaryTree
    and returns its max path sum.

    A path is a collection of connected nodes in a tree,
    where no node is connected to more than two other
    nodes; a path sum is the sum of the values of the nodes
    in a particular path.

    Each BinaryTree node has an integer value, a left child node
    and a right child node. Children nodes can either be BinaryTree
    nodes themselves or None/null.
    '''    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None




def maxPathSum(tree):
    _, maxSum = findMaxSum(tree)

    return maxSum

def findMaxSum(tree):
    if tree is None:
        return (0, 0)

    leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
    rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)

    # can be negative
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

    value = tree.value
    maxSumAsBranch = max(maxChildSumAsBranch + value, value)
    # subtree as triangle, or branch (if values are negative, subtree can be greater than branch with negative value)
    maxSumAsRootNode = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxChildSumAsBranch)

    maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)
    
    return (maxSumAsBranch, maxPathSum)