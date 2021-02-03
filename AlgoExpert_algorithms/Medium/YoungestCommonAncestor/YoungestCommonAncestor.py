'''
Youngest Common Ancestor from AlgoExpert.io
February 2021 Jakub Kazimierski
'''


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    '''
    You're given three inputs, all of which are instances of an 
    AncestralTree class that have an ancestor property pointing to their
    youngest ancestor. The first input is the top ancestor in an ancestral
    tree (i.e. the only instance that has no ancestor--its ancestor property
    points to None/null), and the other two inputs are descendants in the
    ancestral tree.

    Write a function that returns the youngest common ancestor to the two
    descendants.

    Note that a descendant is considered its own ancestor. So in the simple 
    ancestral tree below, the youngest common ancestor to nodes A and B is
    node A.
    '''

    # time O(d) where d is height of the tree | space O(1)

    def findCommonAcestor(nodeOne, nodeTwo, levelOne, levelTwo):
        '''
        time O(d) where d is height of the tree | space O(1)
        Returns common lowest ancestor of two nodes, nodeOne
        has to be lower in the tree than nodeTwo.
        '''

        for _ in range(abs(levelOne-levelTwo)):
            ancestorOne = nodeOne.ancestor
            nodeOne = ancestorOne

        # if nodeTwo was ancestor of nodeOne
        if nodeOne == nodeTwo:
            return nodeOne
        else:
            # look for common ancestor and begin from the same level from both nodes
            while nodeOne.ancestor != nodeTwo.ancestor:
                ancestorOne = nodeOne.ancestor
                nodeOne = ancestorOne
                ancestorTwo = nodeTwo.ancestor
                nodeTwo = ancestorTwo

            return nodeOne.ancestor


    def find_level(node):
        '''
        time O(d) where d is height of the tree | space O(1)
        '''
        count = 0
        while node != topAncestor:
            node = node.ancestor
            count += 1
        return count    


    copyOne = descendantOne
    levelOfOne = find_level(copyOne)

    copyTwo = descendantTwo
    levelOfTwo = find_level(copyTwo)

    if levelOfOne >= levelOfTwo:
        output = findCommonAcestor(descendantOne, descendantTwo, levelOfOne, levelOfTwo)
    else:
        output = findCommonAcestor(descendantTwo, descendantOne, levelOfOne, levelOfTwo)    

    return output



