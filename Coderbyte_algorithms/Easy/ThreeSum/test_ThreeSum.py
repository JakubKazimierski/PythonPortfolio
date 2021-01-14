'''
Unittests for ThreeSum.py
December 2020 Jakub Kazimierski
'''

import unittest
import ThreeSum

class test_ThreeSum(unittest.TestCase):
    '''
    Class contains unittests for
    ThreeSum.py
    '''

    #region Unittests 
    def test_ExpectedOutput(self):
        '''
        Checks if output is as expected.
        '''
        output =ThreeSum.ThreeSum([8, 2, 1, 4, 10, 5, -1, -1])
        self.assertEqual(output, "true")

    def test_FalseOutput(self):
        '''
        Checks if output is equal "false".
        '''
        output =ThreeSum.ThreeSum([12, 3, 1, -5, -4, 7])
        self.assertEqual(output, "false")


    def test_WrongInput(self):
        '''
        Checks if output is equal -1 if input is wrong.
        '''
        output = ThreeSum.ThreeSum(2)
        self.assertEqual(output, -1)

    #endregion

if __name__ == "__main__":
    '''
    Main method of unittest class.
    '''
    unittest.main()