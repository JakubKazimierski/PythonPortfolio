'''
Min Height BST from AlgoExpert.io
January 2021 Jakub Kazimierski
'''

def minHeightBst(array):
    '''
    Write a function that takes in
    a non-empty sorted array of distinct
    integers, and returns the root of the BST.

    The function should minimize the height
    of the BST.

    You've been provided with a BST class that
    you'll have to use to construct the BST.

    Each BST node has an integer value, a left chid
    node, and a right child node. A node is said to be
    valid BST node  if and only if it satisfies the BST
    property: its value is strictly greater than the values
    of every node to its left; its valur is less than or equal
    to the values of every node to it's right; and it's children
    nodes are either valid BST nodes themselves or None/null.


    A BST is valid if and only if all of it's nodes are valid
    BST nodes.

    Note that the BST class already has an insert method which you
    can use if you want.
    '''

    '''
    # we does not have to find median because numbers are distinct
    # just middle index at each insertion
    def min_height_helper(array, root, from_idx, to_idx):
        # time O(Nlog(N))| space O(N)
        # returns minimum BST

        if to_idx < from_idx:
            return

        idx_middle = (to_idx + from_idx)//2
        if root is None:
            root = BST(array[idx_middle])        
        else:
            # insertion is O(log(N))
            root.insert(array[idx_middle])

        min_height_helper(array, root, from_idx, idx_middle-1)
        min_height_helper(array, root, idx_middle+1, to_idx)

        return root

    return min_height_helper(array, None, 0, len(array)-1)
    '''

    def min_height_faster_helper(array, from_idx, to_idx):
        '''
        time O(N)| space O(N)
        returns minimum BST
        '''
        if to_idx < from_idx:
            return

        idx_middle = (to_idx + from_idx)//2
        
        bst = BST(array[idx_middle])        
        # connect left and right children to parent (in each call BST is gaining new children)
        bst.left = min_height_faster_helper(array, from_idx, idx_middle-1)
        bst.right = min_height_faster_helper(array, idx_middle+1, to_idx)

        return bst

    return min_height_faster_helper(array, 0, len(array)-1)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


def preOrderTraverse(tree, array):
    '''
    Time O(n) | space O(n)
    method for tests
    '''
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)

    return array                