'''
Optimal Assignments from Coderbyte
December 2020 Jakub Kazimierski
'''

import sys
import itertools

def OptimalAssignments(strArr):
    '''
    Have the function OptimalAssignments(strArr) 
    read strArr which will represent an NxN matrix 
    and it will be in the following format: 
    ["(n,n,n...)","(...)",...] where the n's represent 
    integers. This matrix represents a machine at row i 
    performing task at column j. The cost for this is matrix[i][j]. 
    Your program should determine what machine should perform what 
    task so as to minimize the whole cost and it should return the 
    pairings of machines to tasks in the following format: (i-j)(...)... 
    Only one machine can perform one task. 
    
    For example: if strArr is ["(5,4,2)","(12,4,3)","(3,4,13)"] then
    your program should return (1-3)(2-2)(3-1) because assigning the 
    machines to these tasks gives the least cost. The matrix will range 
    from 2x2 to 6x6, there will be no negative costs in the matrix, and there 
    will always be a unique answer.
    '''
    
    matrix = [elem[1:-1].split(",") for elem in strArr]

    # belows represet all possible orders of assigning tasks to machines
    permutations = itertools.permutations(list(range(len(matrix[0]))))

    total_min_cost = []
    min_val = sys.maxsize
    for permutation in permutations:
        
        min_coords = []
        temp_sum = 0
        for index in range(len(permutation)):
            temp_sum += int(matrix[index][permutation[index]])
            # increment index and permutation[index] due to indexing from 0
            min_coords.append("(" + "-".join([str(index+1), str(permutation[index]+1)]) + ")")

        if temp_sum < min_val:
            min_val = temp_sum
            total_min_cost = min_coords.copy()        
                        

    return "".join(total_min_cost)
