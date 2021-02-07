'''
Permutations from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def getPermutations(array):
    '''
    Write a function that takes in
    an array of unique integers and
    returns an array of all permutations
    of those integers in no particular
    order.

    If the input array is empty, the function
    should return an empty array.
    '''

    # Time o(n*n!) | space O(n*n!)

    def swap(idx_1, idx_2, arr):
        '''
        Time O(1) | space O(1)
        Swaps elements in array.
        '''
        arr[idx_1], arr[idx_2] = arr[idx_2], arr[idx_1]


    def count_perm(arr, perms, idx):
        '''
        Reurency method, returns array
        of permutations.
        Time O(n*n!) | space O(n*n!)
        n! calls of this method and 
        O(n) times for each copy of 
        permutation.
        '''
    
        if idx == len(arr)-1:
            # copy takes O(n) times
            perms.append(tuple(arr[:]))
        else:
            # below creates each possible swap of first given
            # number with all other positions
            # so for each num from list, all combinations are checked
            # because in recuremcy call, again the second, third, ... etc.
            # places are swapped and recurency call is called again for those situations           
            for idx_2 in range(idx, len(arr)):
                swap(idx, idx_2, array)
                count_perm(arr, perms, idx+1)
                swap(idx, idx_2, array)

        return perms

    return count_perm(array, [], 0)
