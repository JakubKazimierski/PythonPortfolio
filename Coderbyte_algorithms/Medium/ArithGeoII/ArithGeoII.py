'''
Arith Geo II from Coderbyte
December 2020 Jakub Kazimierski
'''

def ArithGeoII(arr):
    '''
    Have the function ArithGeoII(arr) 
    take the array of numbers stored in 
    arr and return the string "Arithmetic" 
    if the sequence follows an arithmetic 
    pattern or return "Geometric" if it follows 
    a geometric pattern. If the sequence doesn't 
    follow either pattern return -1. An arithmetic 
    sequence is one where the difference between 
    each of the numbers is consistent, where as in 
    a geometric sequence, each term after the first is 
    multiplied by some constant or common ratio. 
    
    Arithmetic example: [2, 4, 6, 8] and 
    Geometric example: [2, 6, 18, 54]. 
    Negative numbers may be entered as parameters, 0 
    will not be entered, and no array will contain all 
    the same elements.
    '''
    
    isArith = "true"
    isGeo = "true"

    arith_diff = arr[1] - arr[0]
    
    geo_diff = arr[1] / arr[0]  

    elem_arith_sequence = arr[0]
    elem_geo_sequence = arr[0]
    for elem in arr:
        if elem != elem_arith_sequence:
            isArith = "false"
        if elem != elem_geo_sequence:
            isGeo = "false"

        elem_geo_sequence *= geo_diff
        elem_arith_sequence += arith_diff

    if isArith == "true":
        return "Arithmetic"

    if isGeo == "true":
        return "Geometric"    

    return "-1"