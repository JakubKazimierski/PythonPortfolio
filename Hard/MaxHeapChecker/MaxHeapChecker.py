'''
Max Heap Checker from Coderbyte
January 2021 Jakub Kazimierski
'''

def MaxHeapChecker(arr):
    '''
    Have the function MaxHeapChecker(arr) 
    take arr which represents a heap data 
    structure and determine whether or not it 
    is a max heap. A max heap has the property 
    that all nodes in the heap are either greater 
    than or equal to each of its children. 
    
    For example: if arr is [100,19,36,17] then this is 
    a max heap and your program should return the string max. 
    If the input is not a max heap then your program should return 
    a list of nodes in string format, in the order that they appear 
    in the tree, that currently do not satisfy the max heap property 
    because the child nodes are larger than their parent. 
    
    For example: if arr is [10,19,52,13,16] then your program should return 19,52.

    Another example: if arr is [10,19,52,104,14] then your program should return 19,52,104
    '''
    
    wrong_nodes = []
    def check_heap(index):
        left_node_id = 2 * index + 1
        right_node_id = 2 * index + 2

        if left_node_id < len(arr) and arr[left_node_id] >= arr[index]:
            wrong_nodes.append(arr[left_node_id])
        if right_node_id < len(arr) and arr[right_node_id] >= arr[index]:
            wrong_nodes.append(arr[right_node_id])
        
    for index in range(len(arr)):
        check_heap(index)

    if len(wrong_nodes) == 0:
        return "max"

    return ",".join(str(node) for node in wrong_nodes)           