'''
Node Depths from AlgoExpert.com
January 2021 Jakub Kazimierski
'''

def nodeDepths(root):
    '''
    The distance between a node in a Binary Tree
    and the tree's root is called the node's depth/

    Write a function that takes in a Binary Tree and
    returns the sum of its nodes' depth.

    Each BinaryTree node has an integer value, a left
    child node, and a right child node. Children nodes
    can either be BinaryTree nodes themselves or None/null.
    '''

    def traverse_tree(root, curr_depth, depths_list):
        '''
        Count each node's level and returns list of those levels,
        Worst and avg case time O(n) | space O(h) where h is depth of tree
        '''
        curr_depth += 1
        left_depth = right_depth = curr_depth

        # due to counting from root, append decremented value
        depths_list.append(curr_depth-1)
        if root.left is not None:
            traverse_tree(root.left, left_depth, depths_list)
        if root.right is not None:
            traverse_tree(root.right, right_depth, depths_list)    

        return depths_list

    depths = traverse_tree(root, 0, [])

    return sum(depths)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None