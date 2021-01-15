'''
Array Couples from Coderbyte
January 2021 Jakub Kazimierski
'''

def ArrayCouples(arr):
    '''
    Have the function ArrayCouples(arr) 
    take the arr parameter being passed which 
    will be an array of an even number of positive 
    integers, and determine if each pair of integers,
    [k, k+1], [k+2, k+3], etc. in the array has a corresponding 
    reversed pair somewhere else in the array. 
    
    For example: if arr is [4, 5, 1, 4, 5, 4, 4, 1] then your program 
    should output the string yes because the first pair 4, 5 has the 
    reversed pair 5, 4 in the array, and the next pair, 1, 4 has the 
    reversed pair 4, 1 in the array as well. But if the array doesn't 
    contain all pairs with their reversed pairs, then your program 
    should output a string of the integer pairs that are incorrect, 
    in the order that they appear in the array.
    
    For example: if arr is [6, 2, 2, 6, 5, 14, 14, 1] then your program 
    should output the string 5,14,14,1 with only a comma separating the 
    integers.
    '''

    pairs_with_id = []
    pairs = []
    all_pairs_with_id = []
    correct_pairs = []

    for elem_id in range(0, len(arr)-1, 2):
        pairs_with_id.append(([arr[elem_id], arr[elem_id+1]], elem_id))
        pairs.extend([arr[elem_id], arr[elem_id+1]])
    for elem_id in range(0, len(arr)-1):
        all_pairs_with_id.append(([arr[elem_id], arr[elem_id+1]], elem_id))    

    
    for pair in pairs_with_id:
        for pair_rev in all_pairs_with_id:
            if pair[1] != pair_rev[1]:
                # if pairs starts at different indexes and 
                # reversed pair is equal one of possible pairs
                if pair[0][::-1] == pair_rev[0]:
                    correct_pairs.extend(pair[0])
                    break

    output = []
    for elem in pairs:
        if elem not in correct_pairs:
            output.append(elem)

    if len(output) != 0:
        return ",".join(str(elem) for elem in output)

    return "yes"            
