'''
Caesar Cipher Encryptor from AlgoExpert.com
January 2021 Jakub Kazimierski
'''

from string import ascii_lowercase

def caesarCipherEncryptor(string, key):
    '''
    Given a non-empty string of lowercase letters
    and a non-negative integer representing a key,
    write a function that returns a new string obtained
    by shifting every letter in the input string by k
    position in the alphabet, where k is the key.

    Note that letters should "wrap" around the alphabet;
    in other words, the letter z, shifted by one returns the
    letter a.
    '''

    letters = ascii_lowercase

    encrypted = ""
    for letter in string:
        id_letter = letters.index(letter)
        id_encrypted = (id_letter + key)%len(letters)
        encrypted +=  letters[id_encrypted]

    return encrypted
