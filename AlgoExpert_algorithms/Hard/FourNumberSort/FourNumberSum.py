'''
Four Number Sum from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def fourNumberSum(array, targetSum):
    '''
    Write a function that takes in a non-empty
    array of distinct integers and an integer representing
    a target sum. The function should find all 
    quadruplets in the array that sum up to the target 
    sum and return a two-dimensional array of all these
    quadruplets in no particular order.

    If no four numbers sum up to the target sum, 
    the function should retun an empty array.
    '''

    # Time avg O(n^2), worst O(n^3) | space O(n^2)
    allPairSums = {}
    quadruplets = []

    for idx in range(1, len(array)-1):
        # find missing pair in right iteration
        # pairs of numbers
        for idx_r in range(idx+1, len(array)):
            currSum = array[idx] + array[idx_r]
            diff = targetSum - currSum

            if diff in allPairSums:
                for pair in allPairSums[diff]:
                    quadruplets.append(pair + [array[idx], array[idx_r]])   

        # appending first pair, when found in left iteration
        # prevents from repeating quadruplets
        for idx_l in range(0, idx):
            currSum = array[idx] + array[idx_l]

            if currSum not in allPairSums:
                allPairSums[currSum] = [[array[idx_l], array[idx]]]
            else:
                allPairSums[currSum].append([array[idx_l], array[idx]])        


    return quadruplets