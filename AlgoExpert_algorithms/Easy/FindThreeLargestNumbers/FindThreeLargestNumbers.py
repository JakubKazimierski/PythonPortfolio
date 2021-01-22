'''
Find Three Largest Numbers from AlgoExpert.com
January 2021 Jakub Kazimierski
'''

def findThreeLargestNumbers(array):
    '''
    Write a function that takes in an array of at least 
    three integers and, without sorting the input array,
    returns a sorted array of the three largest integers
    in the input array.

    The function should return duplicate integers if
    necessary; for example, it should return [10, 10, 12]
    for an input of [10, 5, 9, 10, 12].
    '''
    
    largest = [-1*float("inf"), -1*float("inf"), -1*float("inf")]

    # time O(n) | space O(1)
    for elem in array:
        if elem >= largest[2]:           
            largest[0], largest[1] = largest[1], largest[2]
            largest[2] = elem
        elif elem >= largest[1]:
            largest[0], largest[1] = largest[1], elem
        elif elem >= largest[0]:
            largest[0] = elem


    return largest