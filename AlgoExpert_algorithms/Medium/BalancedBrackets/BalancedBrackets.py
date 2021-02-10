'''
Balanced Brackets from AlgoExpert.io
February 2021 Jakub Kazimierski
'''

def balancedBrackets(string):
    '''
    Write a function that takes in
    a string made up of brackets '(',
    '[', '{', ')', ']', and '}', and other
    optional characters. The function should return
    a boolean representing whether the string is balanced
    with regards to brackets.

    A string is said to be balanced if it has as many opening
    brackets of certain type as it has closing brackets of that
    type and if no bracket is unmatched. Note that an opening bracket
    can't match a corresponding closing bracket that comes before it,
    and similarly, a closing bracket can't match a corresponding opening
    bracket that comes after it. Also, brackets can't overlap each other
    as in [(]).
    '''

    # looking in dict O(1) time | space O(1)
    dict_brackets = { '(' : ')', '{' : '}', '[' : ']' }
    # looking in opening brackets list O(1) time | space O(1)
    opening_br = ['(', '{', '[' ]
    # looking in closing brackets list O(1) time | space O(1)
    closing_br = [')', '}', ']' ]
    # stack push and pop O(1) time | O(1) space
    stack = []

    # traversing whole input string takes O(n) time | O(n) space
    # using described above method for lists and dict
    for char in string:
        if len(stack) == 0:
            if char in closing_br:
                return False

        if char in opening_br:
            stack.append(char)
        elif char in closing_br:
            if dict_brackets[stack[-1]] == char:
                stack.pop()
            else:
                return False    
        
    return True if len(stack) == 0 else False