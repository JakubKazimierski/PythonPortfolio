'''
SwapCase from Coderbyte
November 2020 Jakub Kazimierski
'''

def SwapCase(strParam):
    '''
    take the str parameter and swap
    the case of each character
    then return changed string
    '''

    try:
        #strings in python are immutable so 
        #use new one
        strParamOutput = ""

        #iterate over strParam
        #complexity is O(n)
        for i in strParam:
            #check if letter is lower or upper case
            #complexity of built in isupper() and islower() O(1)
            if i.isupper():
                #and assign changed letter to output
                strParamOutput += i.lower()
            elif i.islower():
                strParamOutput += i.upper()
            else:
                #if character is not alphabetic leave at it is
                strParamOutput += i 

        return strParamOutput

    except TypeError:
        #catch wrong type of input
        return -1    