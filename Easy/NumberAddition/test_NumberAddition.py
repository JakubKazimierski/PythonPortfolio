'''
Unittests for NumberAddition.py
November 2020 Jakub Kazimierski
'''

import unittest
import NumberAddition

class test_NumberAddition(unittest.TestCase):
    '''
    Class contains unittests for NumberAddition.py
    '''

    #region Unittests
    def test_SimpleExpectedOutput(self):
        '''
        Checks if numbers from string are summed up.
        '''
        output = NumberAddition.NumberAddition("3 7Number9")
        self.assertEqual(output, 19)
    
    def test_NumberOfManyDigits(self):
        '''
        Checks if for numbers concatenated from many 
        digits output sum is correct.
        '''
        output = NumberAddition.NumberAddition("7Nu44mbaer9")
        self.assertEqual(output, 60)
    
    def test_WrongTypeInput(self):
        '''
        Checks if for wrong input type alghoritm returns proper error.
        '''
        output = NumberAddition.NumberAddition(7)
        self.assertEqual(output, -1)


    #endregion


if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()    