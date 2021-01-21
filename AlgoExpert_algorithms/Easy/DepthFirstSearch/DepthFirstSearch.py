'''
Depth First Search from AlgoExpert.com
January 2021 Jakub Kazimierski
'''

class Node:
    '''
    You're given a Node class that has
    a name and an array of optional children
    nodes. When put together, nodes form an acyclic
    tree-like structure.

    Implement the depthFirstSearch method on the Node class
    , which takes in an empty array, traverses the tree using
    the Depth-first-Search approach (specifically navigating the tree
    from left to right), stores all of the nodes' names in the 
    input array, and returns it. 
    '''
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # time O(V + E) (vertices, edges), space O(V)
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)

        return array    