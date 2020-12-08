'''
SwapCase from Coderbyte
November 2020 Jakub Kazimierski
'''

def SwapCase(strParam):
    '''
    Have the function SwapCase(str) 
    take the str parameter and swap 
    the case of each character. 
    
    For example: if str is "Hello World" 
    the output should be hELLO wORLD. 
    Let numbers and symbols stay the way they are.
    '''

    try:
        # swapcase() changes case of each letter
        return strParam.swapcase()

    except (AttributeError, TypeError):
        return -1
