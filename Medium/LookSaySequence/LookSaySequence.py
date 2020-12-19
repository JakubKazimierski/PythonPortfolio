'''
Look Say Sequence from Coderbyte
December 2020 Jakub Kazimierski
'''

def LookSaySequence(num):
    '''
    Have the function LookSaySequence(num) 
    take the num parameter being passed and 
    return the next number in the sequence 
    according to the following rule: to 
    generate the next number in a sequence read 
    off the digits of the given number, counting 
    the number of digits in groups of the same digit. 
    
    For example, the sequence beginning with 1 would be: 
    1, 11, 21, 1211, ... The 11 comes from there being "one 1" 
    before it and the 21 comes from there being "two 1's" before it.
    So your program should return the next number in the sequence given num.
    '''
    
    char_to_count = str(num)[0]
    count = 1
    output = ""

    if len(str(num)) > 1:
        for char in str(num)[1:]:
            if char == char_to_count:
                count += 1
            else:
                output += str(count) + char_to_count
                char_to_count = char
                count = 1

    # last element of iteration is added here
    output += str(count) + char_to_count

    return int(output)