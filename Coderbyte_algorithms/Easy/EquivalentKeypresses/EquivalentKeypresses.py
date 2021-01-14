'''
Equivalent Keypresses from Coderbyte
December 2020 Jakub Kazimierski
'''

def EquivalentKeypresses(strArr):
    '''
    Have the function EquivalentKeypresses(strArr) 
    read the array of strings stored in strArr which 
    will contain 2 strings representing two comma separated 
    lists of keypresses. Your goal is to return the string 
    true if the keypresses produce the same printable string 
    and the string false if they do not. A keypress can be either 
    a printable character or a backspace represented by -B. 
    You can produce a printable string from such a string of 
    keypresses by having backspaces erase one preceding character.
    '''
    try:
       
        keys_I = strArr[0].split(",")
        keys_II = strArr[1].split(",")

        if keys_I[0] == "-B":
            keys_I[0] = ""
        
        if keys_II[0] == "-B":
            keys_II[0] = ""

        for index in range(1, len(keys_I)):
            if keys_I[index] == "-B":
                keys_I[index] = ""
                keys_I[index-1] = ""

        for index in range(1, len(keys_II)):
            if keys_II[index] == "-B":
                keys_II[index] = ""
                keys_II[index-1] = ""

        word_I = "".join(keys_I)
        word_II = "".join(keys_II)

        if word_I == word_II:
            return "true"

        return "false"

    except(TypeError):
        return -1    