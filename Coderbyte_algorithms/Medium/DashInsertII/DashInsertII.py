'''
Dash Insert II from Coderbyte
December 2020 Jakub Kazimierski
'''

import re

def DashInsertII(num):
    '''
    Have the function DashInsertII(num) 
    insert dashes ('-') between each two 
    odd numbers and insert asterisks ('*') 
    between each two even numbers in str. 
    
    For example: if str is 4546793 the output 
    should be 454*67-9-3. 
    Don't count zero as an odd or even number.
    '''
    

    num = str(num)
    
    # ?= matches at the current position, 
    # but it will not consume any characters for the match. 
    # E.g. the regex a(?=b) will match an a followed by b, 
    # but won't return the b as part of the match.
    
    # \1 mean first bracketed expression \- is inserted after this expression  
    num = (re.sub(r'([13579])(?=([13579]))',r'\1-',num))
    num = (re.sub(r'([2468])(?=([2468]))',r'\1*',num))

    return num

    '''
    # more algorithmic method

    str_num = str(num)
    output = [str_num[0]]

    for elem in str_num[1:]:
        if int(elem) != 0 and int(output[-1]) != 0: 
            if int(output[-1]) % 2 == 0 and int(elem) % 2 == 0:
                output.extend(["*", elem])
            elif int(output[-1]) % 2 == 1 and int(elem) % 2 == 1:
                output.extend(["-", elem])
            else:
                output.append(elem)
        else:
            output.append(elem)

    return "".join(output)
    '''        