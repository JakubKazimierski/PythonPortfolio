'''
Binary Reversal from Coderbyte
November 2020 Jakub Kazimierski
'''

import math

def BinaryReversal(strParam):
    '''
    Have the function BinaryReversal(str) 
    take the str parameter being passed, 
    which will be a positive integer, take
    its binary representation 
    (padded to the nearest N * 8 bits), 
    reverse that string of bits, and then 
    finally return the new reversed string 
    in decimal form. 
    
    For example: if str is "47" then the binary 
    version of this integer is 101111 but we pad it to be 00101111. 
    
    Your program should reverse this binary string which 
    then becomes: 11110100 and then finally return 
    the decimal version of this string, which is 244.
    '''

    if type(strParam) == str:

        binaryForm_withoud_padding = "{:0b}".format(int(strParam))

        # below divides lenght of bin form by 8, and ceils to nearest integer
        # in order to check what size N from N*8 has to be 
        padding_lenght = int(math.ceil(len(binaryForm_withoud_padding)/8))

        binaryForm = "{:0{width}b}".format(int(strParam), width = 8*padding_lenght)

        # below returns decimal format of reversed binary number in string format
        return int(binaryForm[::-1], 2)

    else:
        return -1

