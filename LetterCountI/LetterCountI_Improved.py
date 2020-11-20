'''
Letter Count I from codersbyte
November 2020 Jakub Kazimierski
'''


def LetterCountI(strParam):
    '''
    Have the function LetterCountI(str) 
    take the str parameter being passed 
    and return the first word with the 
    greatest number of repeated letters. 
    For example: "Today, is the greatest day ever!" 
    should return greatest because it has 2 e's (and 2 t's) 
    and it comes before ever which also has 2 e's. 
    If there are no words with repeating letters return -1. 
    Words will be separated by spaces.
    '''
    
    try:

        #region Commentary
        #The filter() method filters the given sequence with the help 
        #of a function (lambda) that tests each element in the sequence to be true or not.
        #set() is math set it means it contains no repeated elements
        #so if shorter is set, that mean more letters are repeated, so word from which
        #shortest set is created is word with most repeated letter
        #complexity is O(n*1*1)=O(n) where n is number of words, O(1) is complexity of making set
        #because sets in python are implemented as hashtables, and also len() function complexity
        # is O(1)   
        #endregion

        output=list(filter(lambda x: len(set(x))<len(x), strParam.split(' ')))
        if len(output)>0:
            return output[0]
        else:
            return -1

    #catch exception
    except (AttributeError, TypeError):
        return -2
    