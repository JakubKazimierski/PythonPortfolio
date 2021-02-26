'''
Codility 2 task February 2021
Jakub Kazimierski
'''

def solution(A):

    # sumation takes O(n)
    array_sum = sum(A)

    # checks all possible partitions 
    # (3 partition at each iter)
    
    # loop takes O(n)
    for idx in range(1, len(A) - 3):
        
        # idx before last one
        rightmost_idx = len(A) - 2
        
        # loop takes O(n)
        while idx + 1 < rightmost_idx:

            temp_sum = array_sum

            temp_sum -= A[idx]
            temp_sum -= A[rightmost_idx]

            if temp_sum % 3 == 0:
                return True

            rightmost_idx -= 1

    return False

    # Total time O(n^2) 