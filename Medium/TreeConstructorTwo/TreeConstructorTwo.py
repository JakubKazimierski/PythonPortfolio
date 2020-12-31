'''
Tree Constructor Two
December 2020 Jakub Kazimierski
'''


def TreeConstructorTwo(strArr):
    '''
    Have the function TreeConstructor(strArr) 
    take the array of strings stored in strArr, 
    which will contain pairs of integers in the following 
    format: (i1,i2), where i1 represents a child node in a 
    tree and the second integer i2 signifies that it is the parent 
    of i1. 
    
    For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"], 
    then this forms the following tree:

             4
           /   
          2     
         / \
        1   7

    which you can see forms a proper binary tree. 
    Your program should, in this case, return the 
    string true because a valid binary tree can be formed. 
    If a proper binary tree cannot be formed with the integer pairs, 
    then return the string false. All of the integers within the 
    tree will be unique, which means there can only be one node in 
    the tree with the given integer value.      
    '''

    parents = []
    children = []
    root = []
    leafs = []
    nodes = []

    for elem in strArr:
        elem = elem.replace("(","").replace(")","").replace(",","")
        parents.append(elem[1])
        children.append(elem[0])
    
    # for empty tree    
    if len(parents) == len(children) == 0:
        return "true"        

    for elem in children:
        if children.count(elem) > 1:
            return "false"
        if elem not in parents:
            leafs.append(elem)
 
    for elem in parents:
        if parents.count(elem) > 2:
            return "false"
        if elem not in children:
            root.append(elem)

    if len(set(root)) != 1:
        return "false"

    # traverse from left down to up
    for leaf in leafs:
        actual = leaf
        while actual != root[0]:
            index = children.index(actual)
            # leaves and parents have same indexes in lists, due to extraction process
            actual = parents[index]
            if index not in nodes:
                nodes.append(index)

    # if amount of nodes from our iteration is different than amount of input children
    # tree is not a proper binary tree
    if len(nodes) != len(children):
        return 'false'

    return "true"


