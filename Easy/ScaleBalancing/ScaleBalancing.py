'''
Scale Balancing from Coderbyte
December 2020 Jakub Kazimierski
'''

from itertools import combinations

def ScaleBalancing(strArr):
    '''
    Have the function ScaleBalancing(strArr) 
    read strArr which will contain two elements, 
    the first being the two positive integer weights 
    on a balance scale (left and right sides) 
    and the second element being a list of available 
    weights as positive integers. 
    
    Your goal is to determine if you can balance the scale 
    by using the least amount of weights from the list, 
    but using at most only 2 weights. 
    
    For example: if strArr is ["[5, 9]", "[1, 2, 6, 7]"]
    then this means there is a balance scale with a weight 
    of 5 on the left side and 9 on the right side. 
    
    It is in fact possible to balance this scale by adding a 6 to 
    the left side from the list of weights and adding a 2 to the right 
    side. Both scales will now equal 11 and they are perfectly balanced. 
    
    Your program should return a comma separated string of the weights 
    that were used from the list in ascending order, so for this example 
    your program should return the string 2,6

    There will only ever be one unique solution and the list of available 
    weights will not be empty. It is also possible to add two weights 
    to only one side of the scale to balance it. 
    If it is not possible to balance the scale then your 
    program should return the string not possible.
    '''

    try:    

        left, right = min(eval(strArr[0])), max(eval(strArr[0]))
        avail_weights = eval(strArr[1])
        for weight in avail_weights:
            if weight + left == right:
                return str(weight)
            
        for index_I in range(0, len(avail_weights)):
            for index_II in range(0, len(avail_weights)):
                if index_I == index_II:
                    continue
                else:
                    if left + avail_weights[index_I] + avail_weights[index_II] == right \
                        or left + avail_weights[index_I] == right + avail_weights[index_II] \
                            or left + avail_weights[index_II] == right + avail_weights[index_I]:
                                return "{},{}".format(min(avail_weights[index_I],avail_weights[index_II]), \
                                                        max(avail_weights[index_I],avail_weights[index_II]))
                
        return "not possible"

    except(AttributeError, TypeError):
        return -1

