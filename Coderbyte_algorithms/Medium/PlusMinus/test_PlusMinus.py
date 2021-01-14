'''
Unittests for PlusMinus.py
December 2020 Jakub Kazimierski
'''

import unittest
import PlusMinus

class test_PlusMinus(unittest.TestCase):    
    '''
    Class with unittests for PlusMinus.py
    '''

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        output = PlusMinus.PlusMinus(35132)
        self.assertEqual(output, "-++-")

   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()