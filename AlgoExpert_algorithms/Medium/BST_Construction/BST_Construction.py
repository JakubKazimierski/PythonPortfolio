'''
BST Construction from AlgoExpert.io
January 2021 Jakub Kazimierski
'''

class BST:
    '''
    Write a BST class for a Binary Search Tree. The class
    should support:
    
    -Inserting values with the insert method.
    -Removing values with the remove method; this
    method should only remove the first instance of
    a given value.
    -Searching for values with the contains method.

    Note that you can't remove values from a single-node tree.
    In other words, calling the remove method on a singe-node
    tree should simply not do anything.

    Each BST node has an integer value, a left child node, and
    a right child ode. A node is said to be a valid BST node if
    and only if it satisfies the BST property:
    its value is strictly greater than the values of every node
    to its left; its value is less than or equal to the values of 
    every node to its right; and its children nodes are either valid 
    BST nodes themselves or None/null.
    '''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        '''
        avg Time O(log(n))| avg space O(1)
        worst Time O(n) | worst space O(1)
        '''
        current_node = self
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    # traverse down
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:    
                    current_node = current_node.right
                
        return self

    def contains(self, value):
        '''
        avg Time O(log(n))| avg space O(1)
        worst Time O(n) | worst space O(1)
        '''
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True
        return False

    def remove(self, value, parent_node = None):
        '''
        avg Time O(log(n))| avg space O(1)
        worst Time O(n) | worst space O(1)
        Parent node helps reasign child node of it
        after removal.
        '''
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            else:
                # value is found
                # both child nodes are not none
                if current_node .left is not None and current_node.right is not None:
                    # replace with minimum value from right branch of tree
                    current_node.value = current_node.right.getMinValue()
                    current_node.right.remove(current_node.value, current_node)
                # root node case if root does not have two chhild nodes
                elif parent_node is None:
                    if current_node.left is not None:
                        # left child becomes root
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        # right child becomes root
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                    else:
                        # root becomes None if it has no children
                        current_node = None
                        
                # we're at the node which does not have two child (or none child)
                elif parent_node.left == current_node:
                    # if min left value is not none reasign it at place removed node else right value even if right is none
                    parent_node.left = current_node.left if current_node.left is not None else current_node.right
                # we're at the node which does not have two child (or none child)
                elif parent_node.right == current_node:
                    parent_node.right = current_node.left if current_node.left is not None else current_node.right 
                
                # after deleting nodes leave loop
                break
        
        return self

    
    def getMinValue(self):
        '''
        avg Time O(log(n))| avg space O(1)
        worst Time O(n) | worst space O(1)
        Parent node helps reasign child node of it
        after removal.
        '''
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value    