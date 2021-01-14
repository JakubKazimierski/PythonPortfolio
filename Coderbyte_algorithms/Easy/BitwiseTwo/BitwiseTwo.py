'''
BitwiseTwo from Coderbyte
December 2020 Jakub Kazimierski
'''

def BitwiseTwo(strArr):
    '''
    Have the function BitwiseTwo(strArr) 
    take the array of strings stored in strArr, 
    which will only contain two strings of equal 
    length that represent binary numbers, 
    and return a final binary string that 
    performed the bitwise AND operation on both strings. 
    
    A bitwise AND operation places a 1 in the new string 
    where there is a 1 in both locations in the binary strings, 
    otherwise it places a 0 in that spot. For example: if strArr is 
    ["10111", "01101"] then your program should return the string "00101"
    '''
    
    try:

        # below changes values into binary format, first string which represents binary into integer base 10
        # and later this integer based 10 into it's binary representation with "0b" at the beginning, & is and in binary
        val = bin(int(strArr[0], 2) & int(strArr[1], 2))[2:].zfill(len(strArr[0]))
        return val

    except (AttributeError, TypeError):
        return -1
        
