'''
Unittests for ThreeNumbers.py
December 2020 Jakub Kazimierski
'''

import unittest
import ThreeNumbers

class test_ThreeNumbers(unittest.TestCase):
    '''
    Class contains unittests for
    ThreeNumbers.py
    '''

    #region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if output is as expected.
        '''
        output = ThreeNumbers.ThreeNumbers("2hell6o3 wor6l7d2")
        self.assertEqual(output, "true")

    def test_FalseOutput(self):
        '''
        Checks if output is equal false for adjacent digits in input.
        '''
        output = ThreeNumbers.ThreeNumbers("21aa3a ggg4g4g6ggg")
        self.assertEqual(output, "false")

    def test_WrongInput(self):
        '''
        Checks if output is equal -1 for wrong input.
        '''
        output = ThreeNumbers.ThreeNumbers(12)
        self.assertEqual(output, -1)


    #endregion

if __name__ == "__main__":
    '''
    Main method of unittest class.
    '''
    unittest.main()