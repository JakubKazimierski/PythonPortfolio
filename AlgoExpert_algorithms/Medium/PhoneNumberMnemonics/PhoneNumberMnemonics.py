'''
Phone Number Mnemonics from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def phoneNumberMnemonics(phoneNumber):
    '''    
    [first look at attached in this directory graphic]

    Almost every digit is associated with some letters in the alphabet; 
    this allows certain phone numbers to spell out actual words. 
    For example, the phone number 8464747328 can be written as
    timisgreat; similarly, the phone number 2686463 can be written
    as antoine or as ant6463.

    It's important to note that a phone number doesn't represent
    a single sequence of letters, but rather multiple combinations
    of letters. For instance, the digit 2 can represent three different
    letters (a, b, and c). 
    
    A mnemonic is defined as a pattern of letters, ideas, or associations
    that assist in remembering something. Companies oftentimes use a mnemonic
    for their phone number to make it easier to remember.

    Given a stringfield phone number of any non-zero length, write a function
    that returns all mnemonics for this phone number, in any order.

    For this problem, a valid mnemonic may only contain letters and the digits
    0 and 1. In other words, if a digit is able to be represented by a letter,
    then it must be. Digits 0 and 1 are the only two digits that don't have
    letter representations on the keypad.

    Note that you should rely on the keypad ilustrated above for digit-letter
    associations.
    '''

    # digits at input are represented as string
    dict_digits = { "1" : "1", "2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz", "0" : "0" }

    output = []

    def code_numbers(number, string_repr):
        '''
        Recurency method, calls itself
        in order to make all possible
        string representations of given
        number.

        Time O(4^n * n) | space O(4^n * n)
        n - digits in number
        Worst case 4 letters represents one number
        Also building each of string representations 
        takes n time.
        '''
        digit = number[0]
        representation = dict_digits[digit]
        cutted_number = number[1:]
                
        for char in representation:
            new_string = string_repr
            new_string += char

            if cutted_number != "":
                code_numbers(cutted_number, new_string)
            else:                
                output.append(new_string)
            
    code_numbers(phoneNumber, "")

    return output
