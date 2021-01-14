'''
Alphabet Run Encryption from Coderbyte
January 2021 Jakub Kazimierski
'''

def DecodeChar(out, arr, index, step):
    '''
    Appends last encrypted letter if out is not empty
    if it is empty, append first lettter of array and next last decoded.
    '''
    if len(out) == 0:
        out = chr(ord(arr[0]) - step)
    out += chr(ord(arr[index]) + step)
    return out

def AlphabetRunEncryption(strParam):
    '''
    Have the function AlphabetRunEncryption(str) 
    read the str parameter being passed which will 
    be an encrypted string and your program should output 
    the original decrypted string. The encryption being 
    used is the following: 
    
    For every character i in str up to the second to last character, 
    take the i and i+1 characters and encode them by writing the letters 
    of the alphabet, in order, that range in the same direction between 
    those chosen characters. 
    
    For example: if the original string were bo then it would be encoded as 
    cdefghijklmn, but if the string were boa then bo is encoded as cdefghijklmn 
    and oa is encoded as nmlkjihgfedcb with the final encrypted string being 
    cdefghijklmnnmlkjihgfedcb. So str may be something like the encrypted string 
    just written, and your program should decrypt it and output the original message.

    The input string will only contains lowercase characters (a...z). There are 
    also three important rules to this encryption based on specific character sequences.

    1) If the original string contains only one letter between two chosen characters, 
    such as the string ac then this would be encrypted as bR with R standing for what 
    direction in the alphabet to go in determining the original characters. The encrypted 
    string bR represents ac but the encrypted string bL represents ca (R = right, L = left).

    2) If the original string contains zero letters between two chosen characters, such as the string 
    ab then this would be encrypted as abS, with S representing the fact that no decryption is needed 
    on the two letters preceding S. For example, if the original string were aba then the encryption 
    would be abSbaS, but be careful because decrypting this you get abba, but the actual 
    original string is aba.

    3) If the original string contains a repeat of letters, such as the string acc then this 
    would be encrypted as bRcN, with N representing the fact that no change in characters occurred on 
    the character preceding N. The input string will never only be composed of repeated characters.
    '''
    
    out = ''
    step = 0
    rules = {'S' : 0, 'N' : 0, 'R' : 1, 'L' : -1}

    for index in range(1, len(strParam)):
        if strParam[index-1] in rules:
            continue

        # ord takes ascii num of char
        dist = ord(strParam[index]) - ord(strParam[index-1])
        
        if abs(dist) == 1:
            step = -1 if dist < 0 else 1

            if index == len(strParam) - 1:
                out = DecodeChar(out, strParam, index, step)

            # belows decode last letter before segment from rules
            elif strParam[index + 1] == 'N' or\
                 (index < len(strParam) - 2 and strParam[index + 2] == 'S'):
                out = DecodeChar(out, strParam, index-1, step)
        else:
            # value is provided if it is not in rules
            step = rules.get(strParam[index], step)
            out = DecodeChar(out, strParam, index-1, step)

    return out
