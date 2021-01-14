'''
Serial Number from Coderbyte
December 2020 Jakub Kazimierski
'''

import re

def SerialNumber(strParam):
    '''
    Have the function SerialNumber(strParam) 
    take the str parameter being passed 
    and determine if it is a valid serial 
    number with the following constraints:

    1. It needs to contain three sets each with three digits 
        (1 through 9) separated by a period.
    2. The first set of digits must add up to an even number.
    3. The second set of digits must add up to an odd number.
    4. The last digit in each set must be larger than the two
        previous digits in the same set.

    If all the above constraints are met within the string, then
    your program should return the string true, otherwise your 
    program should return the string false. 
    
    For example: if str is "224.315.218" then 
    your program should return "true".
    '''
    
    sets = re.split(r'\.', strParam)

    # first condition
    if len(sets) != 3:
        return "false"

    for elem_set in sets:
        if len(elem_set) != 3:
            return "false"

        for elem in elem_set:
            if elem.isdigit() != True:
                return "false"    
        
        # fourth condition
        if elem_set[2] <= elem_set[1] or elem_set[2] <= elem_set[0]:
            return "false"      

    # second condition
    if sum(int(elem) for elem in sets[0]) % 2 != 0:
        return "false" 

    # third condition
    if sum(int(elem) for elem in sets[1]) % 2 != 1:
        return "false" 

    return "true"