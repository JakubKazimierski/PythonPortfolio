'''
Reverse Polish Notation from Coderbyte
January 2021 Jakub Kazimierski
'''

def ReversePolishNotation(strParam):
    '''
    Have the function ReversePolishNotation(str) 
    read str which will be an arithmetic expression 
    composed of only integers and the operators: +,-,* and / 
    and the input expression will be in postfix notation 
    (Reverse Polish notation), an example: (1 + 2) * 3 would be

    1 2 + 3 * in postfix notation. Your program should determine 
    the answer for the given postfix expression. 
    
    For example: if str is 2 12 + 7 / then your program should output 2.
    '''
  
    arr = []
    for char in strParam.split(" "):
        if char.isnumeric():
            arr.append(char)
        else:
            num_2 = arr.pop()
            num_1 = arr.pop()
            arr.append(eval(f"{num_1}{char}{num_2}"))
 
    return arr[0]

