'''
Alphabet Run Encryption from Coderbyte
January 2021 Jakub Kazimierski
'''

from string import ascii_lowercase

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
    
    from_char = ""
    count_letters = 0
    converted = []
    decreasing = False
    increasing = False
    for char_id in range(1, len(strParam)):        

        if from_char == "":
            from_char = strParam[char_id-1]

        id_letter = ascii_lowercase.index(from_char)

        # first char cannot be uppercase
        if strParam[char_id] == 'R':
            decrypted_letter = ascii_lowercase[id_letter-1]
            converted.append((decrypted_letter, 2))

        elif strParam[char_id] == 'L':
            decrypted_letter = ascii_lowercase[id_letter+1]
            converted.append((decrypted_letter, -2))
        
        elif strParam[char_id] == 'S':
            converted.append((strParam[char_id-2]+strParam[char_id-1], 0))
        
        elif strParam[char_id] == 'N':        
            converted.append((strParam[char_id-1], 0))
        
        else:
            
            # if next letter is next in alphabet
            if strParam[char_id] > strParam[char_id-1]:
                decrypted_letter = ascii_lowercase[id_letter-1]
                count_letters += 1
                increasing = True    
                if char_id == len(strParam)-1:
                    # count from char +1 and index of last decrypted letter +1
                    converted.append((decrypted_letter, count_letters+1+1))
            
            elif strParam[char_id] < strParam[char_id-1]:
                decrypted_letter = ascii_lowercase[id_letter+1]    
                count_letters -= 1
                decreasing = True    
                if char_id == len(strParam)-1:
                    converted.append((decrypted_letter, count_letters-1-1))

            else:
                if increasing:
                    # save decrypted first letter, and counted letters
                    converted.append((decrypted_letter, count_letters+1+1))
                if decreasing:
                    converted.append((decrypted_letter, count_letters-1-1))

                decreasing = False
                increasing = False    
                count_letters = 0
                from_char = ""

    output = ""
    for conv in converted:
        letter_id = ascii_lowercase.index(conv[0])
        if conv[1] != 0:
            if len(output) > 0 and output[-1] == conv[0]:
                output += ascii_lowercase[letter_id + conv[1]] 
            else:
                output += conv[0] + ascii_lowercase[letter_id + conv[1]] 
        else:
            # case: abSbaS = aba not abba
            if len(conv[0]) == 2 and output[-1] == conv[0][0]:
                output += conv[0][1]
            else:
                output += conv[0]

    return output
