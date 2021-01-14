'''
String Changes from Coderbyte
December 2020 Jakub Kazimierski
'''

def StringChanges(strParam):
    '''
    Have the function StringChanges(str) 
    take the str parameter being passed, 
    which will be a string containing letters 
    from the alphabet, and return a new string 
    based on the following rules. Whenever a capital
    M is encountered, duplicate the previous character
    (then remove the M), and whenever a capital N is 
    encountered remove the next character from the string 
    (then remove the N). All other characters in the string 
    will be lowercase letters. 
    
    For example: "abcNdgM" should return "abcgg". 
    The final string will never be empty.
    '''
    
    try:
        characters = list(strParam)

        if characters[0]=="M":
            characters[0] = ""
        if characters[-1]=="N":
            characters[-1] = ""

        for index in range(1, len(characters)):
    
            if characters[index] == "M":
                characters[index] = characters[index-1]
    
            if characters[index-1] == "N":
                characters[index] = ""
                characters[index-1] = ""

        return "".join(characters)

    except(TypeError):
        return -1    