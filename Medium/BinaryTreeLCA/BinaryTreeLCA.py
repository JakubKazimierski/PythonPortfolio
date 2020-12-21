'''
Binary Tree LCA from Coderbyte
December 2020 Jakub Kazimierski
'''

def BinaryTreeLCA(strArr):
    '''
    Have the function BinaryTreeLCA(strArr) 
    take the array of strings stored in strArr, 
    which will contain 3 elements: the first 
    element will be a binary tree with all unique 
    values in a format similar to how a binary heap 
    is implemented with NULL nodes at any level represented 
    with a #, the second and third elements will be two different 
    values, and your goal is to find the lowest common ancestor of 
    these two values.

    For example: 
    if strArr is ["[12, 5, 9, 6, 2, 0, 8, #, #, 7, 4, #, #, #, #]", "6", "4"] 
    then this tree looks like the following:

              12
            /    \  
           /      \
          5        9 
         / \      /  \
        6   2    0    8
           /  \
          7     4

    For the input above, your program 
    should return 5 because that is the 
    value of the node that is the LCA of the 
    two nodes with values 6 and 4. You can assume 
    the two nodes you are searching for in the tree will 
    exist somewhere in the tree.      
    '''
    
    treeArr = strArr[0].replace("[","").replace("]", "").replace(" ","").split(",")
    val_1, val_2 = strArr[1], strArr[2]

    # values are unique
    id_val_1 = treeArr.index(val_1)
    id_val_2 = treeArr.index(val_2)

    # if one of nodes is root
    if id_val_1 == 0 or id_val_2 == 0:
        return treeArr[0]

    # indexes like in binary cheap    
    parent_id_val_1 = int((id_val_1 - 1)/2)
    parent_id_val_2 = int((id_val_2 - 1)/2)
    
    # if one of nodes is parent second one
    if id_val_1 == parent_id_val_2:
        return val_1

    if id_val_2 == parent_id_val_1:
        return val_2

    # if nodes are child of common node
    if parent_id_val_1 == parent_id_val_2:
        return treeArr[parent_id_val_1]

    parent_id_val_1_ancestor = parent_id_val_1
    #assume val_1 is lower in tree than val_2
    while parent_id_val_1_ancestor > 0:
        # traverse up
        parent_id_val_1_ancestor = int((parent_id_val_1_ancestor - 1)/2)
        if parent_id_val_1_ancestor == parent_id_val_2:
            return treeArr[parent_id_val_1_ancestor]

    parent_id_val_2_ancestor = parent_id_val_2
    #assume val_2 is lower in tree than val_1
    while parent_id_val_2_ancestor > 0:
        # traverse up
        parent_id_val_2_ancestor = int((parent_id_val_2_ancestor - 1)/2)
        if parent_id_val_2_ancestor == parent_id_val_1:
            return treeArr[parent_id_val_2_ancestor]


    # if none of lower nodes was common ancestor return root
    return treeArr[0]