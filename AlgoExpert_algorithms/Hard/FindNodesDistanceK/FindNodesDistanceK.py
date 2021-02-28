'''
Find Node Distance K from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

class BinaryTree:
    '''
    You're given the root node
    of a Binary Tree, a target value
    of a node that's contained in the tree,
    and a positive integer k. Write a function
    that returns the values of all the nodes that 
    are exactly distance k from the node with target
    value.

    The distance between two nodes is defined as the number
    of edges that must be traversed to go from one node to
    the other. For example, the distance between a node and its
    immediate left or right child is 1. The same holds in reverse:
    the distance between a node and its parents is 1. In a tree
    of three nodes where the root node has a left and right child, the
    left and right children are distance 2 from each other.

    Each BinaryTree node has an integer value, a left child node, and a right
    child node. Children nodes can either be Binary Tree nodes themselves
    or None/ null. Note that all BinaryTree node values will be unique
    and your function can return the output values in any order.
    '''

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    '''
    Total time O(n) | space O(n)
    '''

    def dfs(node, parent, parents):
        '''
        Depth first search algorithm
        for searching prents of nodes.
        Time O(n) | space O(n)
        '''

        if node is not None:
            parents[node] = parent
            dfs(node.left, node, parents)
            dfs(node.right, node, parents)

        return parents


    parents_dict = dfs(tree, None, {})

    visited = set()

    def return_target(node, target_node):
        '''
        Returns target.
        Time O(n) | space O(n) worst stack call.
        '''
        if len(target_node) == 0 and node is not None:
            
            if node.value == target:
                target_node.append(node)

            return_target(node.left, target_node)
            return_target(node.right, target_node)

        return target_node        

    def return_distanced(node, distance, to_return):
        '''
        Returns nodes with distance k from target.
        Time O(n) | space O(n) worst stack call.
        '''
        if distance > k or node is None or node in visited:
            return to_return
    
        visited.add(node)
    
        if distance == k:
            to_return.append(node.value)

        parent = parents_dict[node]
        child_l = node.left
        child_r = node.right

        return_distanced(parent, distance+1, to_return)
        return_distanced(child_l, distance+1, to_return)
        return_distanced(child_r, distance+1, to_return)

        return to_return

    target_node = return_target(tree, [])

    nodes_distanced = return_distanced(target_node[0], 0, [])

    return nodes_distanced

    


