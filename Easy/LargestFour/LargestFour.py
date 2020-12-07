'''
Largest Four from Coderbyte
December 2020 Jakub Kazimierski
'''

def LargestFour(arr):
    '''
    Have the function LargestFour(arr) 
    take the array of integers stored in arr, 
    and find the four largest elements and return 
    their sum. For example: 
    if arr is [4, 5, -2, 3, 1, 2, 6, 6] 
    then the four largest elements in this array are 
    6, 6, 4, and 5 and the total sum of these numbers is 21, 
    so your program should return 21. 
    If there are less than four numbers in the array 
    your program should return the sum of all 
    the numbers in the array.
    '''
    try:
        if len(arr) < 4:
            return sum(arr)
        else:
            largest_list = []
            # below sums up 4 largest elements
            for _ in range(4):
                largest_list.append(arr.pop(arr.index(max(arr))))

            return sum(largest_list)
    except(AttributeError, TypeError):
        return -1
        
def _input():

  exampleInp = "example text"

  return exampleInp

def _output():

  exampleOut = "false"

  return exampleOut