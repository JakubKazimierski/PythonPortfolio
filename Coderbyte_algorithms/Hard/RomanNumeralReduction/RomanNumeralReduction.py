'''
Roman Numeral Reduction from Coderbyte
January 2021 Jakub Kazimierski
'''

def RomanNumeralReduction(strParam):
    '''
    Have the function RomanNumeralReduction(str) 
    read str which will be a string of roman numerals 
    in decreasing order. The numerals being used are: 
    I for 1, V for 5, X for 10, L for 50, C for 100, D for 500 and M for 1000. 
    Your program should return the same number given 
    by str using a smaller set of roman numerals. 
    
    For example: if str is "LLLXXXVVVV" this is 200, 
    so your program should return CC because this is 
    the shortest way to write 200 using the roman numeral 
    system given above. If a string is given in its 
    shortest form, just return that same string.
    '''
    
    dictionary = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 }

    reverse_dict = {1000 : 'M', 900: 'CM', 500 : 'D', 400 : 'CD', 100 : 'C', 90 : 'XC', 50 : 'L',\
     40 : 'XL', 10 : 'X', 9 : 'IX',  5 : 'V', 4 : 'IV', 1 : 'I'}

    int_val = 0

    # below converts Romanian input to decimal
    for char_id in range(1, len(strParam)):
        if dictionary[strParam[char_id]] > dictionary[strParam[char_id-1]]:
            int_val -= dictionary[strParam[char_id-1]]
        else:
            # if first value wasn't substraction
            if int_val == 0:
                int_val += dictionary[strParam[0]]
        int_val += dictionary[strParam[char_id]]

    # below converts decimal to proper Romanian
    output = ""
    for key, value in reverse_dict.items():
        division = int_val // key

        if division == 0:
            continue

        for _ in range(division):
            output += value

        int_val = int_val - division*key


    return output    