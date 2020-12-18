'''
Binary Search Tree LCA from Coderbyte
December 2020 Jakub Kazimierski
'''

# region Binary Search Tree
class Node: 
    def __init__(self, key): 
        self.left = None
        self.right = None
        self.val = key 
  
def insert(root, key): 
    if root is None: 
        return Node(key) 
    else: 
        if root.val == key: 
            return root 
        elif root.val < key: 
            root.right = insert(root.right, key) 
        else: 
            root.left = insert(root.left, key) 
    return root 

def search_ancestors(root, key_one, key_two): 

    # if node is greater/eq than one of keys, and less/eq than other one  
    if root.val <= key_one and root.val >= key_two \
        or root.val >= key_one and root.val <= key_two : 
            return root.val
    
    # go recursively down
    if root.val < key_one and root.val < key_two:
        return search_ancestors(root.right, key_one, key_two) 
    
    # go recursively down
    if root.val > key_one and root.val > key_two:
        return search_ancestors(root.left, key_one, key_two) 

# endregion

def BinarySearchTreeLCA(strArr):
    '''
    Have the function BinarySearchTreeLCA(strArr) 
    take the array of strings stored in strArr, 
    which will contain 3 elements: the first element 
    will be a binary search tree with all unique values in a 
    preorder traversal array, the second and third elements 
    will be two different values, and your goal is to find the 
    lowest common ancestor of these two values. 
    
    For example: if strArr is ["[10, 5, 1, 7, 40, 50]", "1", "7"] 
    then this tree looks like the following:
    
            10
           /  \
         5    40
        / \     \
       1   7     50
    
    For the input above, your program should return 5 because 
    that is the value of the node that is the LCA of the two nodes 
    with values 1 and 7. You can assume the two nodes you are searching 
    for in the tree will exist somewhere in the tree.
    '''
    

    tree_arr = eval(strArr[0])
    first_elem, sec_elem = int(strArr[1]), int(strArr[2])

    root = Node(tree_arr.pop(0)) 

    for element in tree_arr:
        insert(root, element)

    return search_ancestors(root, first_elem, sec_elem)
