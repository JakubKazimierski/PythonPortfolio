'''
Unittests for Bracket Matcher from Coderbyte
Jakub Kazimierski October 2020
'''

import unittest
import BracketMatcher

class test_BracketMatcher(unittest.TestCase):
    '''
    Class contains unittests
    for BracketMatcher.py
    '''

    #region Unittests
    def test_NoBrackets(self):
        '''
        Ckecks if there is no brackets in input
        output is equal 1 (because 0 is even number of brackets).
        '''
        output = BracketMatcher.BracketMatcher("withoutBrackets")
        self.assertEqual(output, 1)
    
    def test_NoEqualAmountOfBrackets(self):
        '''
        Checks if number of brackets doesnt match
        even number, output is equal to 0.
        '''
        output = BracketMatcher.BracketMatcher("(witho(utBr)ackets")
        self.assertEqual(output, 0)
    
    def test_OneTypeOfBrackets(self):
        '''
        Checks if for only one type of brackets
        in input, output is 0.
        '''
        output = BracketMatcher.BracketMatcher("w)it)houtBr)ackets")
        self.assertEqual(output, 0)
        
    def test_EvenNumberOfBrackets(self):
        '''
        Checks if for even number of brackets, where each "(" bracket
        match ")" bracket output is equall to 1.
        '''
        output = BracketMatcher.BracketMatcher("(((w)it)houtBr)ackets")
        self.assertEqual(output, 1)

    def test_EvenNumberOfBracketsMixed(self):
        '''
        Checks if for even number of brackets, where at least
        one "(" bracket does not match with ")" bracket, output is equal to 0. 
        '''
        output = BracketMatcher.BracketMatcher("the color re(d))()(()")
        self.assertEqual(output, 0)
    #endregion

if __name__ == "__main__":
    '''
    Main method for unit tests.
    '''
    unittest.main()