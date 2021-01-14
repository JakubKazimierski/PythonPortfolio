'''
Unittests for MeanModeFaster.py
November 2020 Jakub Kazimierski
'''

import unittest
import MeanModeFaster

class test_MeanModeFaster(unittest.TestCase):
    '''
    Class contains unittests for MeanModeFaster.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if mean is equal to mode output is 1.
        '''
        output = MeanModeFaster.MeanModeFaster([4, 4, 4, 6, 2])
        self.assertEqual(output, 1)

    def test_TypeInput(self):
        '''
        Check if for wrongType input output is "Wrong Type Input".
        '''
        output = MeanModeFaster.MeanModeFaster(["4", "4", "4", "6", "2"])
        self.assertEqual(output, "Wrong Type Input")

    #endregion

if __name__ == "__main__":
    '''
    Main method for unittests.
    '''
    unittest.main()
