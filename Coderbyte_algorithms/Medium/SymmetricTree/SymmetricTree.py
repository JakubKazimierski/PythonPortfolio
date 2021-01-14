'''
Symmetric Tree from Coderbyte
December 2020 Jakub Kazimierski
'''

def Recurency_check_left(node_id, strArr, arrRemember):
    '''
    Remember all values of tree
    With left-down priority:
        # First check left node with reccurency
        # Next check right node with reccurency
    '''
    left_child_id = 2*node_id + 1
    right_child_id = 2*node_id + 2

    if right_child_id <= len(strArr):
        # priority has left side
        arrRemember.append(strArr[left_child_id])
        Recurency_check_left(left_child_id, strArr, arrRemember)
     
        arrRemember.append(strArr[right_child_id])
        Recurency_check_left(right_child_id, strArr, arrRemember)    

    return arrRemember

def Recurency_check_right(node_id, strArr, arrRemember):
    '''
    Remember all values of tree
    With right-down priority:
        # First check right node with reccurency
        # Next check left node with reccurency
    '''
    
    left_child_id = 2*node_id + 1
    right_child_id = 2*node_id + 2

    if right_child_id <= len(strArr):
        # priority has right side
        arrRemember.append(strArr[right_child_id])
        Recurency_check_right(right_child_id, strArr, arrRemember)
     
        arrRemember.append(strArr[left_child_id])
        Recurency_check_right(left_child_id, strArr, arrRemember)    

    return arrRemember


def SymmetricTree(strArr):
    '''
    Have the function SymmetricTree(strArr) 
    take the array of strings stored in strArr, 
    which will represent a binary tree, and determine 
    if the tree is symmetric (a mirror image of itself). 
    The array will be implemented similar to how a binary 
    heap is implemented, except the tree may not be complete 
    and NULL nodes on any level of the tree will be represented 
    with a #. 
    
    For example: if strArr is ["1", "2", "2", "3", "#", "#", "3"] 
    then this tree looks like the following:
    
         1
       /  \
      2    2
     / \   / \
    3   # #   3

    For the input above, your program should return the string true 
    because the binary tree is symmetric.
    '''

    tree_from_left = []
    tree_from_right = []
    if Recurency_check_left(0, strArr, tree_from_left) ==\
         Recurency_check_right(0, strArr, tree_from_right):
        return "true"
    
    return "false"   
