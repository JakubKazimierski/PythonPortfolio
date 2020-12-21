'''
Binary Tree LCA from Coderbyte
December 2020 Jakub Kazimierski
'''

def Find_Node_val(node_id, strArr, val, arr_parent):
    '''
    Returns arr_parent with parent node element.
    Due to problem that recurrency work at stack, i could not
    get the same result by simple return, list was
    necessary to remember found element, while recursion
    still works. That's why I'm not 100% glad from this
    solution.
    '''
    if val == strArr[node_id]:
        arr_parent.append(strArr[node_id])

    left_child_id = 2*node_id + 1
    right_child_id = 2*node_id + 2

    # return parent node of value
    if right_child_id <= len(strArr):
        if strArr[left_child_id] != val and strArr[right_child_id] != val:
            Find_Node_val(left_child_id, strArr, val, arr_parent)
            Find_Node_val(right_child_id, strArr, val, arr_parent) 
        else:
            arr_parent.append(strArr[node_id])

    return arr_parent


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
    
    tree_string_values = strArr[0].replace("[","").replace("]", "").replace(" ","") 
    tree_Arr = tree_string_values.split(",")
    val_1, val_2 = strArr[1], strArr[2]

    # list with one elem is returned
    parent_val_1 = Find_Node_val(0, tree_Arr, val_1, [])[0]
    parent_val_2 = Find_Node_val(0, tree_Arr, val_2, [])[0]

    # simplest case, one of values is parent of second one
    if val_1 == parent_val_2:
        return val_1
    if val_2 == parent_val_1:
        return val_2    

    if parent_val_1 != parent_val_2:
        # assume parent_val_2 is lower in tree than parent_val_1
        ancestors_val_2 = parent_val_2
        while ancestors_val_2 != tree_Arr[0] and ancestors_val_2 != parent_val_1:
            # while ancestor is not common, go up
            ancestors_val_2 = Find_Node_val(0, tree_Arr, ancestors_val_2, [])[0]
        
        if  parent_val_1 == ancestors_val_2:
            return parent_val_1
     
        # assume parent_val_1 is lower in tree than parent_val_2
        ancestors_val_1 = parent_val_1               
        while ancestors_val_1 != tree_Arr[0] and ancestors_val_1 != parent_val_2:
            # while ancestor is not common, go up
            ancestors_val_1 = Find_Node_val(0, tree_Arr, ancestors_val_1, [])[0]
        
        if  parent_val_2 == ancestors_val_1:
            return parent_val_2
        
        # if root is LCA
        if ancestors_val_2 == ancestors_val_1:
            return ancestors_val_1

    return parent_val_1