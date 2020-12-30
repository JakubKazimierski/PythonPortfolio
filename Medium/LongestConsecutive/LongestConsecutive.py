'''
Longest Consecutive from Coderbyte
December 2020 Jakub Kazimierski
'''

def LongestConsecutive(arr):
    '''
    Have the function LongestConsecutive(arr) 
    take the array of positive integers stored 
    in arr and return the length of the longest 
    consecutive subsequence (LCS). An LCS is a 
    subset of the original list where the numbers 
    are in sorted order, from lowest to highest, and 
    are in a consecutive, increasing order. 
    The sequence does not need to be contiguous 
    and there can be several different subsequences. 
    
    For example: if arr is [4, 3, 8, 1, 2, 6, 100, 9] 
    then a few consecutive sequences are [1, 2, 3, 4], and 
    [8, 9]. For this input, your program should return 4 
    because that is the length of the longest consecutive 
    subsequence.
    '''
    
    sorted_arr = list(set(sorted(arr)))

    lca = 1
    count = 1
    for elem_id in range(1, len(sorted_arr)):
        if sorted_arr[elem_id] == sorted_arr[elem_id-1] + 1:
            count += 1
            # if till last elem sequence was consecutive
            if elem_id == len(sorted_arr)-1:
                if count > lca:
                    lca = count
        else:
            if count > lca:
                lca = count
            count = 1    

    return lca