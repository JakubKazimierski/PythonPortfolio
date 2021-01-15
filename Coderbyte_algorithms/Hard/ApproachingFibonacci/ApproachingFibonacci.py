'''
Approaching Fibonacci from Coderbyte
January 2021 Jakub Kazimierski
'''

def ApproachingFibonacci(arr):
    '''
    Have the function ApproachingFibonacci(arr) 
    take the arr parameter being passed which will 
    be an array of integers and determine the smallest 
    positive integer (including zero) that can be added 
    to the array to make the sum of all of the numbers in 
    the array add up to the next closest Fibonacci number. 
    
    For example: if arr is [15, 1, 3], then your program should 
    output 2 because if you add up 15 + 1 + 3 + 2 you get 21 which 
    is the closest Fibonacci number.
    '''
    

    sum_num = sum(arr)

    n_0 = 1
    n_1 = 1
    n_2 = n_1 + n_0
    while n_2 < sum_num:

        # below counts next fibonacci numbers
        n_2 = n_1 + n_0
        n_0 = n_1
        n_1 = n_2

    dif_next = abs(n_1 - sum_num)

    return dif_next
