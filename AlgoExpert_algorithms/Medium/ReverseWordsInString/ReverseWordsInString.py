'''
Reverse Words in String from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def reverseWordsInString(string):
    '''
    Write a function that takes in a string of
    words separated by one or more whitespaces
    and returns a string that has these words 
    in reverse order. For example, given the string
    "tim is great", your function should return
    "great is tim".

    For this problem, a word can contain special 
    characters, punctuation, and numbers. The words
    in the string will be separated by one or more
    whitespaces, and the reversed string must contain
    the same whitespaces as the original string. For
    example, given the string "whitespaces 4" you 
    would be expected to return "4 whitespaces".

    Note that you're not allowed to use any built-in
    split or reverse methods/functions. However, you 
    are allowed to use a built-in join method/function.

    Also note that the input string isn't guaranteed to always
    contain words.
    '''

    # LIFO
    stack = []

    # O(n) time | O(n) space
    list_chars = list(string)
    word_container = ""
    is_word = True
    is_space = False

    # O(n) time | O(n) space
    while len(list_chars) > 0:
        char = list_chars.pop(0)

        # below remembers whitespaces, and add not whitespaces to the stack
        if char.isspace():

            if is_word:
                stack.append(word_container)
                word_container = char
            else:
                word_container += char

            is_word = False
            is_space = True
            

        # below remembers not whitespaces, and add whitespaces to the stack
        else:
            if is_space:
                stack.append(word_container)
                word_container = char
            else:
                word_container += char

            is_space = False
            is_word = True
    
    # last apended word is not seen by while loop
    stack.append(word_container)            

    # O(n) time | O(n) space
    output = "".join(word for word in reversed(stack))

    return output
