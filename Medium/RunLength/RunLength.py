'''
Run Length from Coderbyte
December 2020 Jakub Kazimierski
'''

def RunLength(strParam):
    '''
    Have the function RunLength(str) 
    take the str parameter being passed and 
    return a compressed version of the string 
    using the Run-length encoding algorithm. 
    This algorithm works by taking the occurrence 
    of each repeating character and outputting that 
    number along with a single character of the repeating 
    sequence. 
    
    For example: "wwwggopp" would return 3w2g1o2p. 
    The string will not contain any numbers, punctuation, 
    or symbols.
    '''
    try:

        letters = dict.fromkeys(strParam)
        occurence_list = []
        output_string = ""

        # below iterates by keys
        for letter in letters:
            occurence_list.append(strParam.count(letter))

        for occurence, letter in zip(occurence_list, list(letters.keys())):
            output_string += str(occurence) + str(letter)

        return output_string

    except(TypeError):
        return -1