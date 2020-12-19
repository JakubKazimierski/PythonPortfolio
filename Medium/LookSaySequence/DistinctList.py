'''
Distinct List from Coderbyte
December 2020 Jakub Kazimierski
'''

def DistinctList(arr):
    '''
    Have the function DistinctList(arr) 
    take the array of numbers stored in 
    arr and determine the total number of 
    duplicate entries. 
    
    For example if the input is [1, 2, 2, 2, 3] 
    then your program should output 2 because there 
    are two duplicates of one of the elements.
    '''
    
    return len(arr) - len(set(arr))