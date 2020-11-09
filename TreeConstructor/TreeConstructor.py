'''
TreeConstructor from codersbyte
October 2020 Jakub Kazimierski
'''

from collections import Counter

def TreeConstructor(strArr):
  '''
  Function return true if input array form proper binary tree
  input format: array of (i1,i2), where i1 represents a child node
  in a tree and the second integer i2 signifies that it is the parent of i1.
  '''
  try:
    
    #create list of parents and children
    #map gives to function (here it is lambda) elements from iteration from object
    #(here it is strArr ), last thing is what lambda does
    #lambda changes brackets at empty char, and splits numbers 
    #then for parents go second element of splited string
    #for children goes first element of splited list
    parents = list(map(lambda x:x.replace('(','').replace(')','').split(',')[1],strArr))
    children = list(map(lambda x:x.replace('(','').replace(')','').split(',')[0],strArr))
    

    #A Counter is a dict subclass for counting hashable objects
    #here it will be used to count how many times each parent node was in input string
    #hash value does not change during program, and can be compared to other objects
    count_parents = Counter(parents)

    #most_common returns most common objects in counter [elem][counter]
    #number of parents cannot be more than 2 (each parent has at most 2 children)
    if count_parents.most_common(1)[0][1] > 2:
      return 'false'
    count_children = Counter(children)
    #number of children canot be more than 1
    if count_children.most_common(1)[0][1] > 1:
      return 'false'

    roots = 0
    root_list = []

    #return elements each time it occurs 
    for element in count_parents.elements():
      #if parent is no one child
      if element not in count_children.elements():
        if element not in root_list:
          #add as root (there can be only one root)
          #and there must be at least one root
          root_list.append(element)
          roots +=1
    if roots != 1:
      return 'false'

    #list of nodes which are not parents (key() returns values of counter not their count)
    leafs = [node for node in count_children.keys() if node not in count_parents.keys()]
    #return root from parents who are not children
    root = [node for node in count_parents.keys() if node not in count_children.keys()]
    nodes = []

    for leaf in leafs:
      actual = leaf
      #while leaf is not a root of tree
      while actual != root[0]:
        index = children.index(actual)
        #go up to the root
        actual = parents[index]
        if index not in nodes:
          #make list of all nodes (iterate over all children and go up to the root)
          nodes.append(index)

    #if amount of nodes from our iteration is different than amount of input children
    #our tree is not a proper binary tree
    if len(nodes) != len(children):
      return 'false'

    return 'true'
  except IndexError:
    return 'false'
