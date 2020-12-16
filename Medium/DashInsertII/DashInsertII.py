'''
Dash Insert II from Coderbyte
December 2020 Jakub Kazimierski
'''

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