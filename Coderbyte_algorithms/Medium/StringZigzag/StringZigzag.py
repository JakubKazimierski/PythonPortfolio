'''
String Zigzag from Coderbyte
December 2020 Jakub Kazimierski
'''

def StringZigzag(strArr):
    '''
    Have the function StringZigzag(strArr) 
    read the array of strings stored in strArr, 
    which will contain two elements, the first some 
    sort of string and the second element will be a 
    number ranging from 1 to 6. The number represents 
    how many rows to print the string on so that it forms 
    a zig-zag pattern. 
    
    For example: if strArr is ["coderbyte", "3"] 
    then this word will look like the following if you print 
    it in a zig-zag pattern with 3 rows:

    c      r       e
     o   e   b   t
       d       y
    
    Your program should return the word formed by 
    combining the characters as you iterate through each row, 
    so for this example your program should return the string 
    creoebtdy.
    '''
    
    rows = int(strArr[1])
    word = strArr[0]
    output = ['']*rows

    row = 0
    increment_row = False
    for char in word:
        output[row] += char
        # at borders of rows change direction of incrementing
        # for decrementing or from decrementing to incrementing (zig zag)
        if row == 0 or row == rows-1:
            increment_row = not increment_row
        if rows>1:
            row += 1 if increment_row else -1   

    return ''.join(output)         
