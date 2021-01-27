'''
BST Traverslal from AlgoExoert.io
January 2021 Jakub Kazimierski
'''

class BST:
    '''
    Class of binary search tree.

    Task description:

    
    Write three functions that take in 
    a Binary Search Tree (BST) and an empty
    array, traverse the BST, add its nodes' 
    values to the input array, and return
    that array. The three functions should 
    traverse the BST using the in-order,
    pre-order, and post-order tree-traversal 
    techniques, respectively.

    Each BST node has an integer value, a left
    child node, and a right child node. A node is said
    to be a valid BST node if and only if it satisfies 
    the BST property: 

    Its value is strictly greater than the values of every
    node to its left; its value is less than or equal to 
    the values of every node to its right; and its children
    nodes are either valid BST nodes themselves or None/null.
    '''
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
                                             
def inOrderTraverse(tree, array):
    '''
    Time O(n) | space O(n)
    '''
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)

    return array

def preOrderTraverse(tree, array):
    '''
    Time O(n) | space O(n)
    '''
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)

    return array


def postOrderTraverse(tree, array):
    '''
    Time O(n) | space O(n)
    '''
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)

    return array

def setUp():
    '''
    Returns BST tree for tests
    '''
    root = BST(5)
    root.insert(10)
    root.insert(2)
    root.insert(3)

    return root    