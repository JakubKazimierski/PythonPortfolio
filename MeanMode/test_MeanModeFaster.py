'''
Unittests for MeanModeFaster.py
November 2020 Jakub Kazimierski
'''

import unittest
import MeanModeFaster

class test_MeanModeFaster(unittest.TestCase):
    '''
    class contains unittests
    for MeanModeFaster.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        check if for array where mean is equal to mode
        output is 1
        '''
        output = MeanModeFaster.MeanModeFaster([4, 4, 4, 6, 2])
        self.assertEqual(output, 1)

    def test_TypeInput(self):
        '''
        check if for wrongType input
        output is "Wrong Type Input"
        '''
        output = MeanModeFaster.MeanModeFaster(["4", "4", "4", "6", "2"])
        self.assertEqual(output, "Wrong Type Input")

    #endregion

if __name__ == "__main__":
    '''
    main method for unittests
    '''
    unittest.main()
