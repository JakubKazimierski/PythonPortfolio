'''
Validate BST from AlgoExpert.io
January 2021 Jakub Kazimierski
'''

class BST:
    '''
    Class of binary search tree.
    '''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        '''
        Avg O(log(n)) time | O(1) space
        Worst O(n) time | O(1) space
        '''
        current_node = self

        while True:
            if current_node.value > value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                current_node = current_node.right

        return self

def setUp():
    '''
    Returns BST tree for tests
    '''
    root = BST(5)
    root.insert(10)
    root.insert(2)
    root.insert(3)

    return root    

def validateBst(tree):
    '''
    Write a function that takes in
    a potentially invalid Biary Search Tree(BST)
    and returns a boolean representing whether 
    the BST is valid.

    Each BST node has an integer value, a left child
    node, and a right child node. A node is said 
    to be valid BST node if and only if it satisfies 
    the BST property: its value is strictly greater than 
    the values of every node to its right; and its children
    nodes are either valid BST nodes themselves or None/null.

    A BST is valid if and only if all of its nodes are valid BST
    nodes.
    '''

    def validate_helper(tree, min_val, max_val):

        # O(n) time | O(d) space where d is depth of BST
        if tree is None:
            return True

        if tree.value < min_val or tree.value >= max_val:
            return False
        # left has to be strictly less than current value    
        left_valid = validate_helper(tree.left, min_val, tree.value) 
        # right has to be greater or equal to cuurent value   
        right_valid = validate_helper(tree.right, tree.value, max_val)
        # min and max values are updated at each level of depth!
        # min_val < curr_node <= max_val
        return left_valid and right_valid

    return validate_helper(tree, float("-inf"), float("inf"))    