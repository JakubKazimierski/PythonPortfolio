'''
Simple SAT from Coderbyte
January 2021 Jakub Kazimierski
'''

from itertools import product

def SimpleSAT(strParam):
    '''
    Have the function SimpleSAT(str) 
    read str which will be a string 
    consisting of letters, parenthesis, 
    logical operators and tilde's representing a 
    Boolean formula. 
    
    For example: str may be "(a&b)|c" which means
    (a AND b) OR c. Your program should output the 
    string yes if there is some arrangement of replacing 
    the letters with TRUE or FALSE in such a way that 
    the formula equates to TRUE. If there is no possible 
    way of assigning TRUE or FALSE to the letters, then your 
    program should output the string no. In the example above, 
    your program would return yes because a=TRUE, b=TRUE and c=FALSE 
    would make the formula TRUE. 
    
    Another example: if str is "((a&c)&~a)" which means 
    ((a AND c) AND NOT a) then your program should output no 
    because it is not possible to assign TRUE or FALSE values 
    to the letters to produce a TRUE output.

    A Boolean formula will always have at most 5 letters, 
    i.e. a, b, c, d and e. A tilde will never appear outside 
    of a parenthesis, i.e. ~(a&b).
    '''
    
    dictionary = {'&' : ' and ', '|' : ' or ', '~' : ' not '}

    variables = []
    for elem in strParam:
        if elem.isalpha() and elem not in variables:
            variables.append(elem)

    combinations = list(product(range(2), repeat=len(variables)))


    # below tries all possible combinations of True and False
    for comb in combinations:
        var_dict = {}
        # below creates letter : bool combinations dictionary            
        for letter, value in zip(variables, comb):
            if value == 0:
                bool_var = 'False'
            else:
                bool_var = 'True'    

            var_dict.update({ letter : bool_var })

        # below evaluates combinations
        output = ""
        for elem in strParam:
            if elem in dictionary.keys():
                output += dictionary[elem]
            elif elem in var_dict.keys():
                output += var_dict[elem]    
            else:
                output += elem

        # if true return yes
        if eval(output):
            return 'yes'                

    return 'no'
