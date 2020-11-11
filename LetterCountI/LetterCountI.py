'''
Letter Count I from codersbyte
November 2020 Jakub Kazimierski
'''


def LetterCountI(strParam):
    '''
    method returns word witch most repeated 
    amount of letters
    if letters dont repeat in any word return -1
    '''
    
    try:
        #to get rid of spaces and make list of words
        words = strParam.split(" ")
        #default we assume each letter appear once
        most_repeated = 1
        #if each letter appear once answer is -1
        answer = -1

        #i assume complexity is O(n^2)
        #traverse list of words
        for word in words:
            #traverse letters in each word
            for i in word:            
                #count() method returns the number of occurrences of a substring
                if word.count(i) > most_repeated:
                    #assign new most common value if new is larger than previous one
                    most_repeated = word.count(i)
                    #answer becames word with most common amount of repeated letters
                    #in that case
                    #and also here comes type change of answer (from int to string)
                    answer = word

        return answer

    #catch exception
    except Exception:
        return -2
    