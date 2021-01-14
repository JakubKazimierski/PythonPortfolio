'''
Longest Increasing Sequence from Coderbyte
December 2020 Jakub Kazimierski
'''

from itertools import combinations

def LongestIncreasingSequence(arr):
    '''
    Have the function LongestIncreasingSequence(arr) 
    take the array of positive integers stored in arr 
    and return the length of the longest increasing 
    subsequence (LIS). A LIS is a subset of the original 
    list where the numbers are in sorted order, from lowest 
    to highest, and are in increasing order. The sequence does 
    not need to be contiguous or unique, and there can be several 
    different subsequences. 
    
    For example: if arr is [4, 3, 5, 1, 6] then a possible LIS is [3, 5, 6], 
    and another is [1, 6]. For this input, your program should return 3 
    because that is the length of the longest increasing subsequence.
    '''
    
    increasing_seq = []
    for length in range(1, len(arr)):
        # combinations create sets with occurence in array order
        for seq in combinations(arr, length):
            if list(seq) == sorted(list(seq)) and\
                 len(set(seq)) == len(list(seq)) :
                increasing_seq.append(seq)

    max_seq = max(increasing_seq, key=len)
    return len(max_seq)