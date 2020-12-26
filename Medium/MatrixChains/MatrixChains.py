'''
Matrix Chains from Coderbyte
December 2020 Jakub Kazimierski
'''

# Matrix A[i] has dimension p[i-1] x p[i] 
# for i = 1..n 
import sys

def MatrixChainOrder(arr, start_id, end_id): 
  
    if start_id == end_id: 
        return 0
  
    _min = sys.maxsize 
  
    # place parenthesis at different places 
    # between first and last matrix, 
    # recursively calculate count of 
    # multiplications for each parenthesis 
    # placement and return the minimum count 
    for bracket_id in range(start_id, end_id): 
  
        count = (MatrixChainOrder(arr, start_id, bracket_id) 
                 + MatrixChainOrder(arr, bracket_id + 1, end_id) 
                 + arr[start_id-1] * arr[bracket_id] * arr[end_id]) 
  
        if count < _min: 
            _min = count 
  
    # Return minimum count 
    return _min 
  
  
  

def MatrixChains(arr):
    '''
    Have the function MatrixChains(arr) 
    read the array of positive integers 
    stored in arr where every pair will 
    represent an NxM matrix. 
    
    For example: if arr is [1, 2, 3, 4] 
    this means you have a 1x2, 2x3, and a 3x4 matrix. 
    So there are N-1 total matrices where N is the 
    length of the array. Your goal is to determine the 
    least number of multiplications possible after 
    multiplying all the matrices. Matrix multiplication 
    is associative so (A*B)*C is equal to A*(B*C).

    For the above example, let us assume the following 
    letters represent the different matrices: 
    A = 1x2, B = 2x3, and C = 3x4. 
    Then we can multiply the matrices in the following orders: 
    (AB)C or A(BC). The first ordering requires (1*2*3) = 6 then 
    we multiply this new 1x3 matrix by the 3x4 matrix and we get (1*3*4) = 12. 
    So in total, this ordering required 6 + 12 = 18 multiplications. 
    Your program should therefore return 18 because the second ordering 
    produces more multiplications. The input array will contain between 3 
    and 30 elements.
    '''
    
    return MatrixChainOrder(arr, 1, len(arr)-1)