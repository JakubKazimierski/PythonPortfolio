'''
Third Greatest from Coderbyte
November 2020 Jakub Kazimierski
Parsing input is changed than in originall task
i think it is more challenging (a litte bit)
'''


def ThirdGreatest(strArr):
    '''
    take the string stored in strArr
    and return the third largest word within it
    index where word start defines if it is greater than
    other string with same amount of letters
    The array will have at least three strings
    and each string will only contain letters.
    '''

    try:
            
        #check if type of string is correct
        #it can contain only letters and spaces
        for i in strArr:
            if i.isalpha() != True:
                if i != " ":
                    return -1


        #split words by spaces
        words = strArr.split(" ")
        #sort by length, first word with same length as nexr will be first in this array
        #so order is correct
        words.sort(reverse = True, key = len)
        
        #return third longest element 
        return words[2]

    #assert correct type
    except TypeError:
        return -1