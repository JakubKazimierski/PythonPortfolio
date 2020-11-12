'''
Unittests for MeanMode.py
November 2020 Jakub Kazimierski
'''

import unittest
import MeanMode

class test_MeanMode(unittest.TestCase):
    '''
    class contains unittests
    for MeanMode.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        check if for array where mean is equal to mode
        output is 1
        '''
        output = MeanMode.MeanMode([4, 4, 4, 6, 2])
        self.assertEqual(output, 1)

    def test_TypeInput(self):
        '''
        check if for wrongType input
        output is "Wrong Type Input"
        '''
        output = MeanMode.MeanMode(["4", "4", "4", "6", "2"])
        self.assertEqual(output, "Wrong Type Input")


    #endregion


if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()    
