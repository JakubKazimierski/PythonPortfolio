'''
Unittests for MultiplicativePersistence.py
November 2020 Jakub Kazimierski
'''

import unittest
import MultiplicativePersistence


class test_MultiplicativePersistence(unittest.TestCase):
    '''
    class contains unittests for MultiplicativePersistence.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        test if output is proper
        e.g for 39 it should be 3
        '''
        output = MultiplicativePersistence.MultiplicativePersistence(39)
        self.assertEqual(output, 3)


    def test_OneDigitInput(self):
        '''
        check if for one digit in input
        output is 0
        '''
        output = MultiplicativePersistence.MultiplicativePersistence(9)
        self.assertEqual(output, 0)

    def test_WrongInputType(self):
        '''
        check if for wrong input type
        output is -1
        '''
        output = MultiplicativePersistence.MultiplicativePersistence("9")
        self.assertEqual(output, -1)


    def test_NegativeIntigerInput(self):
        '''
        check if for negative inut intiger
        output is -1
        '''
        output = MultiplicativePersistence.MultiplicativePersistence(-9)
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    main method of unittests
    '''
    unittest.main()