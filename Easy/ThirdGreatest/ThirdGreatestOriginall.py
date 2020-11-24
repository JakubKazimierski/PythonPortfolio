'''
Third Greatest from Coderbyte
November 2020 Jakub Kazimierski
'''

def ThirdGreatestOriginall(strArr):
    '''
    take array of strings and return third longest
    '''

    try:

        # it is somwhere between O(n) O(n^2)
        #check if strings not contain forbidden input signs
        for i in strArr:
            for j in i:
                if j.isalpha() !=True and j != " ":
                    return -1

        #work on bufor of given parameter
        words = strArr  
        #sort new list by length in reverse order
        words.sort(reverse= True, key = len)


        #return third greatest
        return words[2]

    #check if input type is correct
    except TypeError:
        return -1

