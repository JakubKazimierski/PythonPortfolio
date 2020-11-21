'''
ArithGeo from codersbyte
November 2020 Jakub Kazimierski
'''

def ArithGeo(arr):
    '''
    Have the function ArithGeo(arr) take the array 
    of numbers stored in arr and return the string 
    "Arithmetic" if the sequence follows an arithmetic pattern 
    or return "Geometric" if it follows a geometric pattern. 
    If the sequence doesn't follow either pattern return -1. 
    An arithmetic sequence is one where the difference between each of the numbers is consistent, 
    where as in a geometric sequence, each term after the first is multiplied by some constant 
    or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54]. 
    Negative numbers may be entered as parameters, 0 will not be entered, 
    and no array will contain all the same elements.
    '''
    try:


        diffArytm = arr[1] - arr[0]        
        diffGeo = arr[1]/arr[0]

        # If all elements are true
        if all(arr[i+1]-arr[i] == diffArytm for i in range(0,len(arr)-1)):
            return "Arithmetic"

        if all(arr[i+1]/arr[i] == diffGeo for i in range(0,len(arr)-1)):
            return "Geometric"

        # If none of above was true
        return -1
            
    except ZeroDivisionError:
        return -1

def _input():

    sampleList = [1,2,3,4]

    return sampleList

def _output():

    sampleString = "Arithmetic"

    return sampleString
