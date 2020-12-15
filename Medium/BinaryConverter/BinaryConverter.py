'''
Binary Converter from Coderbyte
December 2020 Jakub Kazimierski
'''

def BinaryConverter(strParam):
    '''
    Have the function BinaryConverter(str) 
    return the decimal form of the binary value. 
    For example: if 101 is passed return 5, or if 
    1000 is passed return 8.
    '''

    # simplest solution
    #output = int(strParam, 2)
    
    output = 0
    reversedStr = strParam[::-1]
    for index in range(0,len(reversedStr)):
        output += (2**index)*int(reversedStr[index])
    
    return output    