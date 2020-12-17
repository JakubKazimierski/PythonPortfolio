'''
String  Reduction from Coderbyte
December 2020 Jakub Kazimierski
'''

def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

def StringReduction(strParam):
    '''
    Have the function StringReduction(str) 
    take the str parameter being passed and 
    return the smallest number you can get through 
    the following reduction method. The method is: 
    Only the letters a, b, and c will be given in str 
    and you must take two different adjacent characters 
    and replace it with the third. For example "ac" can be 
    replaced with "b" but "aa" cannot be replaced with anything. 
    This method is done repeatedly until the string cannot be 
    further reduced, and the length of the resulting string is 
    to be outputted.

    For example: if str is "cab", then "ca" can be reduced to "b" 
    and you get "bb" (you can also reduce it to "cc"). 
    The reduction is done so the output should be 2. 
    If str is "bcab", "bc" reduces to "a", so you have "aab", 
    then "ab" reduces to "c", and the final string "ac" is reduced 
    to "b" so the output should be 1.
    '''
    
    letters = ['a','b','c']

    reducable = True

    list_str_param = list(strParam)
    
    # temporary list of reduced elements
    trans_list = []

    while reducable == True:

        while len(list_str_param) > 0:
            # pair of letters to eventually reduce
            temp_pair = []

            temp_pair.append(list_str_param.pop(0))
            temp_pair.append(list_str_param.pop(0))

            # if those are different letters
            if len(set(temp_pair)) > 1:
                # swap with third different
                swap_with = Diff(letters, temp_pair)[0]

                # add reduce elem to list of reduced elements
                trans_list.append(swap_with)    
            else:
                trans_list.extend(temp_pair)

        # override old list with list of reduced elements
        list_str_param = trans_list
        # clear new list
        trans_list = []
        
        # if list contains different letters
        if len(set(list_str_param)) > 1:
            reducable = True
        else:
            reducable = False


    return len(list_str_param)