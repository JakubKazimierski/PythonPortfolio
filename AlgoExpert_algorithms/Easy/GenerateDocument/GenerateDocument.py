'''
Generate Document from ALgoExpert.io
March 2021 Jakub Kazimierski
'''

def generateDocument(characters, document):
    '''
    You're given a string of available charaacters
    and a string representing a document that you need
    to generate. Write a function that determines if 
    you can generate the document using the available
    characters. If you can generate the document, your function
    should return True; otherwise it should return False.

    You're only able to generate the document if the frequency
    of unique characters in the characters string is greater
    tha or equal to the frequency of unique characters in the document
    string. For examle, if you're given characters = "abcabc"
    and document = "aabbccc" you cannot generate the document because
    you're missing one c.

    The document that you need to create may contain any characters,
    including special characters, capital letters, numbers
    and spaces. 

    Note you can aways generate the empty string ("")
    '''

    # base case

    if len(document) > len(characters):
        return False

    # Time O(n) | Space O(1)
    for char in set(document):
        if document.count(char) > characters.count(char):
            return False

    return True            