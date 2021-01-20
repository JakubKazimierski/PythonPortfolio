'''
Branch Sums from AlgoExpert.com
January 2021 Jakub Kazimierski
'''

def branchSums(root):
    '''
    Write a function that takes in a Binary Tree
    and returns a list of its branch sums ordered
    from leftmost branch sum to rightmost branch sum.

    A branch sums is the sum of all values in a Binary Tree
    branch. A Binary Tree branch is a path of nodes in a tree
    that starts at the root node and ends at any lleaf node.

    Each Binary Tree node has an integer value, a left child
    node, and a right child node. Children nodes can
    either be BinaryTree nodes themselves or None/null.
    '''

    def traverse_tree(root, current_sum, sums):
        '''
        Appends sum of each branch into returned at the end list.
        O(n) time | O(n) space
        '''
        current_sum += root.value
        sum_right = current_sum
        sum_left = current_sum

        if root.left is not None:
            traverse_tree(root.left, sum_left, sums)
        if root.right is not None:
            traverse_tree(root.right, sum_right, sums)
        if root.left is None and root.right is None:
            sums.append(current_sum)              

        return sums

    sums = traverse_tree(root, 0, [])

    return sums


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
