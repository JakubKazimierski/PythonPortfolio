'''
String Expression from Coderbyte
December 2020 Jakub Kazimierski
'''

def StringExpression(strParam):
    '''
    Have the function StringExpression(str) 
    read the str parameter being passed which will 
    contain the written out version of the numbers 0-9 
    and the words "minus" or "plus" and convert the 
    expression into an actual final number written out 
    as well. 
    
    For example: if str is "foursixminustwotwoplusonezero" 
    then this converts to "46 - 22 + 10" which evaluates to 
    34 and your program should return the final string threefour. 
    If your final answer is negative it should include the word "negative."
    '''

    dictionary = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',\
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'plus': '+', 'minus': '-'}

    dictionary_rev = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five',\
        '6':'six', '7':'seven', '8':'eight', '9':'nine', '-':'negative'}

    value = ""
    elem = ""
    for char in strParam:
        elem += char
        if elem in dictionary:
            value += dictionary[elem]
            elem = ""

    value = str(eval(value))

    output = ""
    for elem in value:
        if elem in dictionary_rev:
            output += dictionary_rev[elem]

    return output        