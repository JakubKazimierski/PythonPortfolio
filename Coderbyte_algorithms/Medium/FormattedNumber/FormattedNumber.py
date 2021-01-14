'''
Formatted Number form Coderbyte
December 2020 Jakub Kazimierski
'''

def FormattedNumber(strArr):
    '''
    Have the function FormattedNumber(strArr) 
    take the strArr parameter being passed, 
    which will only contain a single element, 
    and return the string true if it is a valid 
    number that contains only digits with properly 
    placed decimals and commas, otherwise return the 
    string false. 
    
    For example: if strArr is ["1,093,222.04"] then your 
    program should return the string true, but if the input 
    were ["1,093,22.04"] then your program should return the 
    string false. The input may contain characters other than digits.
    '''

    # only left side of point '.' is checked
    if strArr[0].count(".") == 1:
        left = strArr[0].split(".")[0]
    elif strArr[0].count(".") == 0:
        left = strArr[0]
    else:
        return "false"

    # check if coma is inserted at each 4th place after 3 digits
    place_count = 0
    for elem in left[::-1]:
        if elem.isdigit():
            place_count += 1
        elif elem == ",":
            if place_count == 3:
                place_count = 0
            else:
                return "false"
        else:
            return "false"         
    
    # if no comma was inserted
    if place_count > 3:
        return "false"    

    return "true"
