'''
Breadth-first Search from AlgoExpert.io
January 2021 Jakub Kazimierski
'''

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def returnChild(self, name):
        '''
        Method created for tests (not best one)
        '''
        for child in self.children:
            if child.name == name:
                return child


    def breadthFirstSearch(self, array):
        '''
        You're given a Node class that has a name
        and an array of optional children nodes.
        When put together, nodes form an acyclic tree-like
        structure.

        Implement the breadthFirstSearch method on the Node class,
        which takes in an empty array, traverses the tree using
        the breadth-first Search approach (specifically navigating
        the tree from left to right), stores all of the nodes' names
        in the input array, and returns it.
        '''
        
        # implementation based on queue (fifo)
        # time O(v+e) v-vertices e-edges| space O(n)
        queue = []

        array.append(self.name)

        queue.extend(self.children)

        while len(queue) != 0:
            node = queue.pop(0)
            array.append(node.name)
            queue.extend(node.children)

        return array

def setUp():
    '''
    Returns graph for tests
    '''
    graph = Node('A')
    graph.addChild('B')
    graph.addChild('C')
    graph.addChild('D')
  
    node_B = graph.returnChild('B')
    node_B.addChild('E')
    node_B.addChild('F')
    
    node_F = node_B.returnChild('F')
    node_F.addChild('I')
    node_F.addChild('J')

    node_D = graph.returnChild('D')
    node_D.addChild('G')
    node_D.addChild('H')

    node_G = node_D.returnChild('G')
    node_G.addChild('K')


    return graph    