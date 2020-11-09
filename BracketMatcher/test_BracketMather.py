'''
test for bracket matcher from coderbyte
Jakub Kazimierski 2020
'''

import unittest
import BracketMatcher


class test_BracketMatcher(unittest.TestCase):
    '''
    class with unit tests
    for BracketMatcher method
    1 is for correct output
    0 is for wrong output
    '''

    #region Unittests
    def test_NoBrackets(self):
        '''
        consider 0 as even number
        so string without brackets
        should return correct output
        '''
        output = BracketMatcher.BracketMatcher("withoutBrackets")
        self.assertEqual(output, 1)
    
    def test_NoEqualAmountOfBrackets(self):
        '''
        when brackets doesnt match
        outpunt should be wrong
        '''
        output = BracketMatcher.BracketMatcher("(witho(utBr)ackets")
        self.assertEqual(output, 0)
    
    def test_OneTypeOfBrackets(self):
        '''
        for oe type of brackets
        output should be wrong
        '''
        output = BracketMatcher.BracketMatcher("w)it)houtBr)ackets")
        self.assertEqual(output, 0)
        
    def test_EvenNumberOfBrackets(self):
        '''
        for even number of bracket matching each other
        output should be corrrect
        '''
        output = BracketMatcher.BracketMatcher("(((w)it)houtBr)ackets")
        self.assertEqual(output, 1)

    def test_EvenNumberOfBracketsMixed(self):
        '''
        when number of brackets are even
        but in wrong order (brackets dont match each other)
        e.g )( output should be wrong
        '''
        output = BracketMatcher.BracketMatcher("the color re(d))()(()")
        self.assertEqual(output, 0)
    #endregion

if __name__ == "__main__":
    '''
    main method for unit tests
    '''
    unittest.main()