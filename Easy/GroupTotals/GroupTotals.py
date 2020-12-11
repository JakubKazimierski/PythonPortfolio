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
    
    # elements which will be added to first of it's key
    appended = []
    # elements with value 0 or 1 which mean visited or not
    key_val_arr = []
    # list of lists with elements if the same key
    corresponding_values = []
    # final list with elements having summed up values
    output_list = []

    for elem in strArr:
        key_val_arr.append([elem.split(":"), 0])


    for indexI in range(0, len(key_val_arr)-1):
        # below matches as visited
        key_val_arr[indexI][1] = 1
        # below appends elements having the same key and apeended elements go to list appended
        for indexII in range(indexI + 1 , len(key_val_arr)):
            # key_val_arr[indexI][0][0] mean e.g "B" from ["B:1", 0]
            if key_val_arr[indexII][1] == 0 and key_val_arr[indexI][0][0] == key_val_arr[indexII][0][0]:
                key_val_arr[indexI].append(key_val_arr[indexII][0])
                appended.append(key_val_arr[indexII])

    # take only elements which were not appended                
    for elem in key_val_arr:
        if elem not in appended:
            elem.pop(1)
            corresponding_values.append(elem)        

    # sum values of corresponding keys, and delete those which value summed up to 0
    for elem in corresponding_values:
        sum_val = 0
        key = ""
        for val in elem:
            key = val[0]
            sum_val += int(val[1])
    
        if sum_val != 0:
            output_list.append(key + ":" + str(sum_val))
    
    
    return ",".join(sorted(output_list))    