'''
TreeConstructor from Coderbyte
October 2020 Jakub Kazimierski
'''

from collections import Counter

def TreeConstructor(strArr):
    '''
    Have the function TreeConstructor(strArr) 
    take the array of strings stored in strArr, 
    which will contain pairs of integers in the 
    following format: (i1,i2), where i1 represents 
    a child node in a tree and the second integer 
    i2 signifies that it is the parent of i1. 
    
    For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"], 
    then this forms the following tree:

          (4)
        /  
      (2)
      / \
    (1) (7)

    which you can see forms a proper binary tree. 
    Your program should, in this case, return the 
    string true because a valid binary tree can be formed. 
    
    If a proper binary tree cannot be formed with the integer pairs, 
    then return the string false. All of the integers within the tree 
    will be unique, which means there can only be one node in the tree 
    with the given integer value.  
    '''
    try:
      
        # extraction of children and parents nodes to lists
        parents = list(map(lambda x:x.replace('(','').replace(')','').split(',')[1],strArr))
        children = list(map(lambda x:x.replace('(','').replace(')','').split(',')[0],strArr))
        
        # {"node":"appearence"}
        count_parents = Counter(parents)
        count_children = Counter(children)
        
        # number of parents cannot be more than 2 (each parent has at most 2 children)
        if count_parents.most_common(1)[0][1] > 2:
            return 'false'
        
        #number of children canot be more than 1
        if count_children.most_common(1)[0][1] > 1:
            return 'false'

        roots = 0
        root_list = []

        # below finds root if tree    
        for element in count_parents.elements():
          
            if element not in count_children.elements():

              if element not in root_list:
                  root_list.append(element)
                  roots +=1
          
        if roots != 1:
            return 'false'

        # Counter.keys() method helps to see the unique elements in the list
        leafs = [node for node in count_children.keys() if node not in count_parents.keys()]
      
        nodes = []

        # below creates list of children from given input
        for leaf in leafs:
            actual = leaf
            while actual != root_list[0]:
                index = children.index(actual)
                # leaves and parents have same indexes in lists, due to extraction process
                actual = parents[index]
                if index not in nodes:
                    nodes.append(index)

        # if amount of nodes from our iteration is different than amount of input children
        # tree is not a proper binary tree
        if len(nodes) != len(children):
            return 'false'

        return 'true'
    
    except IndexError:
        return 'false'

def _input():

    exampleInput = ["(1,2)","(3,2)","(2,5)","(6,5)"]

    return exampleInput

def _output():

    exampleOutput = "true"

    return exampleOutput  