'''
Group Totals from Coderbyte
December 2020 Jakub Kazimierski
'''

def GroupTotals(strArr):
    '''
    Have the function GroupTotals(strArr) 
    read in the strArr parameter containing 
    key:value pairs where the key is a string 
    and the value is an integer. Your program 
    should return a string with new key:value 
    pairs separated by a comma such that each 
    key appears only once with the total values 
    summed up.

    For example: if strArr is ["B:-1", "A:1", "B:3", "A:5"] 
    then your program should return the string A:6,B:2.

    Your final output string should return the keys in alphabetical order. 
    Exclude keys that have a value of 0 after being summed up.
    '''
    
    dictionary = {}
    for pair in strArr:
        pair = pair.split(':')

        # dict.get(key, 0) 0 it's default value if value for key is missing
        dictionary[pair[0]] = dictionary.get(pair[0], 0) + int(pair[1])

    # if value != 0 return key:value
    return ','.join(f'{key}:{value}' for key, value in sorted(dictionary.items()) if value)

