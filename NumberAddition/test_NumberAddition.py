'''
Unittests for NumberAddition.py
November 2020 Jakub Kazimierski
'''

import unittest
import NumberAddition

class test_NumberAddition(unittest.TestCase):
    '''
    class contains unittests for NumberAddition.py
    '''

    #region Unittests
    def test_SimpleExpectedOutput(self):
        '''
        check if fro simple input alghoritm works
        properly
        '''
        output = NumberAddition.NumberAddition("7Number9")
        self.assertEqual(output, 16)
    
    def test_NumberOfManyDigits(self):
        '''
        check if for numbers concatenate from many 
        digits input alghoritm works
        properly
        '''
        output = NumberAddition.NumberAddition("7Nu44mber9")
        self.assertEqual(output, 60)
    
    def test_WrongTypeInput(self):
        '''
        check if for wrong input type
        alghoritm return proper error
        '''
        output = NumberAddition.NumberAddition(7)
        self.assertEqual(output, -1)


    #endregion


if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()    