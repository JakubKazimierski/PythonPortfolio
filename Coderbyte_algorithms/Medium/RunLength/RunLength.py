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

        char_occurences = []
        # below remembers previous element
        memory = strParam[0]
        # below counts occurences
        counter = 0
        for char_id in range(0, len(strParam)):
            if strParam[char_id] == memory:
                counter += 1
                
                # if it is last index and previous was the same
                if char_id == len(strParam)-1:
                    char_occurences.append(str(counter) + memory)
            else:
                if char_id == len(strParam)-1:
                    # if it is last index and previous was different
                    char_occurences.append(str(counter) + memory)
                    char_occurences.append(str(counter) + strParam[char_id])
                else:
                    char_occurences.append(str(counter) + memory)

                # reset counter    
                counter=1

            memory = strParam[char_id] 


        return "".join(char_occurences)

    except(TypeError):
        return -1