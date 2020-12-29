'''
Preorder Traversal from Coderbyte
December 2020 Jakub Kazimierski
'''


def traverse_tree(arr, output, index):
    '''
    Traverse tree from left to right.
    '''

    left_child = 2*index + 1
    right_child = 2*index + 2

    output.append(arr[index])
    
    if arr[index] != "#":
        if left_child < len(arr):
            traverse_tree(arr, output, left_child)
        if right_child < len(arr):
            traverse_tree(arr, output, right_child)

    return output

def PreorderTraversal(strArr):
    '''
    Have the function PreorderTraversal(strArr) 
    take the array of strings stored in strArr, 
    which will represent a binary tree with integer 
    values in a format similar to how a binary heap is 
    implemented with NULL nodes at any level represented 
    with a #. Your goal is to return the pre-order traversal 
    of the tree with the elements separated by a space. 
    
    For example: if strArr is 
    ["5", "2", "6", "1", "9", "#", "8", "#", "#", "#", "#", "#", "#", "4", "#"] 
    then this tree looks like the following tree:
     
             5
           /   \
          2     6  
         / \     \
        1   9     8
                 /
                4   
    For the input above, your program should return the string 5 2 1 9 6 8 4 
    because that is the pre-order traversal of the tree.            
    '''

    output = traverse_tree(strArr, [], 0)

    return " ".join(elem for elem in output if elem != "#")    

