'''
Unittests for SimpleAdding
October 2020 Jakub Kazimierski
'''

import unittest
import SImpleAdding

class test_SImpleAdding(unittest.TestCase):
    '''
    Class contains unittests for SimpleAdding.py
    '''

    #region Unittests
    def test_ProperOutput(self):
        '''
        Checks if output is proper sum from 1 to num.
        '''
        output = SImpleAdding.SimpleAdding(12)
        self.assertEqual(output, 78)

    def test_NotProperInput(self):
        '''
        Checks if output is -1 when type of input is wrong.
        '''
        output = SImpleAdding.SimpleAdding("12")
        self.assertEqual(output, -1)
    #endregion

if __name__ == "__main__":
    '''
    Main method for unittests class.
    '''
    unittest.main()