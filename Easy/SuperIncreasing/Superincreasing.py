'''
Superincreasing from Coderbyte
November 2020 Jakub Kazimierski
'''

def Superincreasing(arr):
    '''
    Have the function Superincreasing(arr) 
    take the array of numbers stored in arr 
    and determine if the array forms a superincreasing 
    sequence where each element in the array is greater 
    than the sum of all previous elements. 
    The array will only consist of positive integers. 
    
    For example: if arr is [1, 3, 6, 13, 54] then your 
    program should return the string "true" because it 
    forms a superincreasing sequence. 
    If a superincreasing sequence isn't formed, 
    then your program should return the string "false"
    '''

    try:
        
        for i in range(1, len(arr)):
            if arr[i] <= sum(arr[0:i]):
                return "false"

        return "true"

    except TypeError:
        return -1


def _input():

    exampleInput =  [1, 3, 6, 13, 54]

    return exampleInput

def _output():

    exampleOutput = "true"

    return exampleOutput  