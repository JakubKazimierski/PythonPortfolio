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
        #Below splits words into list
        words = strParam.split(" ")
        #By default we assume each letter appear once
        most_repeated = 1
        #If each letter appear once answer is -1
        answer = -1

        #I assume complexity is O(n*m^2) where n is number of words and m is amount of letters in word
        for word in words:
            #Below traverses letters in each word
            for i in word:            
                #count() method returns the number of occurrences of a substring
                if word.count(i) > most_repeated:
                    #Assign new most common value if new value is larger than previous one
                    most_repeated = word.count(i)
                    #answer becames word with most common amount of repeated letters
                    #then type of ansew changes from int to string
                    answer = word

        return answer

    #catch exception
    except (AttributeError, TypeError):
        return -2
    