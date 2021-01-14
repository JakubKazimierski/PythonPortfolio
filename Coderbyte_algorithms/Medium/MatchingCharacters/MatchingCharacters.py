'''
Matching Characters from Coderbyte
December 2020 Jakub Kazimierski
'''

def MatchingCharacters(strParam):
    '''
    Have the function MatchingCharacters(str) 
    take the str parameter being passed and determine 
    the largest number of unique characters that exists 
    between a pair of matching letters anywhere in the string. 
    
    For example: if str is "ahyjakh" then there are only two pairs 
    of matching letters, the two a's and the two h's. Between the pair 
    of a's there are 3 unique characters: h, y, and j. Between the h's 
    there are 4 unique characters: y, j, a, and k. So for this example 
    your program should return 4.

    Another example: if str is "ghececgkaem" then your program should return 
    5 because the most unique characters exists within the farthest pair of e 
    characters. The input string may not contain any character pairs, and in 
    that case your program should just return 0. The input will only consist 
    of lowercase alphabetic characters.
    '''
    
    try:
        lenghts = []
        for index in range(0, len(strParam)-1):
            unique = set()
            for look_id in range(index+1, len(strParam)):
                if strParam[look_id] != strParam[index]:
                    unique.add(strParam[look_id])
                else:
                    lenghts.append(len(unique))
                    # in array can be more same letters
                    # so continue process with appended to set same letter
                    unique.add(strParam[look_id])

        if len(lenghts) != 0:
            return max(lenghts)

        return 0    
    except(IndexError):
        return 0    